"""Command-line orchestration for the LiveScribe host pipeline."""

from __future__ import annotations

import argparse
import queue
import threading

from software.src.asr_decoder import ASRDecoder
from software.src.dsp_pipeline import DSPPipeline
from software.src.serial_listener import AudioPacket, SerialListener


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", help="USB CDC serial port for the Pico.")
    parser.add_argument("--baudrate", type=int, default=921600)
    return parser


def main() -> int:
    """Start the threaded audio-to-transcript pipeline."""
    args = build_parser().parse_args()
    packet_queue: queue.Queue[AudioPacket] = queue.Queue()
    feature_queue: queue.Queue[object] = queue.Queue()
    transcript_queue: queue.Queue[str] = queue.Queue()
    stop_event = threading.Event()

    # TODO: Connect the reader, DSP, ASR, and visualization worker loops.
    _ = (args, packet_queue, feature_queue, transcript_queue, stop_event)
    _ = (DSPPipeline, ASRDecoder, SerialListener)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
