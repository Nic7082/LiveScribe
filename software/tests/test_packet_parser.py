"""Tests for USB CDC packet framing and checksum validation."""

import struct

from software.src.serial_listener import HEADER, AudioPacket, crc16_xor, parse_packet


def make_packet(sequence: int, samples: tuple[int, ...]) -> bytes:
    payload = struct.pack(f"<{len(samples)}H", *samples)
    header = HEADER.pack(0xAA55, sequence, len(payload))
    body = header + payload
    return body + struct.pack("<H", crc16_xor(body))


def test_parse_packet_returns_pcm_samples() -> None:
    packet = parse_packet(make_packet(7, (0, 2048, 4095)))
    assert packet == AudioPacket(sequence=7, samples=(0, 2048, 4095))


def test_parse_packet_rejects_bad_checksum() -> None:
    data = bytearray(make_packet(7, (12, 34)))
    data[-1] ^= 0x01
    assert parse_packet(bytes(data)) is None


def test_parse_packet_rejects_wrong_length() -> None:
    data = make_packet(1, (12, 34))[:-1]
    assert parse_packet(data) is None
