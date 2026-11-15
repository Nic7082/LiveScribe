"""Benchmark a starter STFT and Mel/MFCC feature extraction workflow."""

from __future__ import annotations

import time

import librosa
import numpy as np
from scipy import signal


def main() -> None:
    """Run one STFT/MFCC pass over a generated 16 kHz test signal."""
    sample_rate_hz = 16000
    time_axis = np.arange(sample_rate_hz, dtype=np.float32) / sample_rate_hz
    audio = np.sin(2.0 * np.pi * 440.0 * time_axis).astype(np.float32)

    started_at = time.perf_counter()
    _, _, spectrum = signal.stft(
        audio,
        fs=sample_rate_hz,
        window="hamming",
        nperseg=320,
        noverlap=160,
        boundary=None,
    )
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate_hz, n_mfcc=13, n_fft=512, hop_length=160)
    elapsed_ms = (time.perf_counter() - started_at) * 1000.0
    print(f"STFT shape: {spectrum.shape}; MFCC shape: {mfcc.shape}; elapsed: {elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
