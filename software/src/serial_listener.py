"""Threaded USB CDC packet input and packet checksum validation."""

from __future__ import annotations

import queue
import struct
import threading
from dataclasses import dataclass

PACKET_MAGIC = 0xAA55
HEADER = struct.Struct("<HHH")
MAX_PAYLOAD_BYTES = 320 * 2


@dataclass(frozen=True)
class AudioPacket:
    """One validated frame of little-endian unsigned PCM samples."""

    sequence: int
    samples: tuple[int, ...]


def crc16_xor(data: bytes) -> int:
    """Compute CRC-16/CCITT-FALSE for packet header and payload bytes."""
    crc = 0xFFFF
    for value in data:
        crc ^= value << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return crc


def parse_packet(data: bytes) -> AudioPacket | None:
    """Parse one complete packet, returning ``None`` for malformed frames."""
    if len(data) < HEADER.size + 2:
        return None

    magic, sequence, payload_length = HEADER.unpack_from(data)
    if magic != PACKET_MAGIC or payload_length > MAX_PAYLOAD_BYTES:
        return None
    expected_length = HEADER.size + payload_length + 2
    if payload_length % 2 or len(data) != expected_length:
        return None

    expected_crc = struct.unpack_from("<H", data, len(data) - 2)[0]
    if crc16_xor(data[:-2]) != expected_crc:
        return None

    samples = struct.unpack(f"<{payload_length // 2}H", data[HEADER.size:-2])
    return AudioPacket(sequence=sequence, samples=samples)


class SerialListener(threading.Thread):
    """Background USB CDC reader that publishes validated audio packets."""

    def __init__(
        self,
        port: str,
        baudrate: int,
        output_queue: queue.Queue[AudioPacket],
        stop_event: threading.Event,
    ) -> None:
        super().__init__(name="livescribe-serial", daemon=True)
        self.port = port
        self.baudrate = baudrate
        self.output_queue = output_queue
        self.stop_event = stop_event

    def run(self) -> None:
        """Read serial bytes, resynchronize on packet magic, and enqueue frames."""
        # TODO: Implement buffered framing and pyserial connection lifecycle.
        raise NotImplementedError
