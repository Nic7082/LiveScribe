"""Audio framing and spectral feature extraction for LiveScribe."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


class DSPPipeline:
    """Convert PCM frames into windowed spectral and Mel features."""

    def __init__(self, sample_rate_hz: int = 16000) -> None:
        self.sample_rate_hz = sample_rate_hz

    def frame_audio(self, samples: NDArray[np.int16]) -> NDArray[np.float32]:
        """Frame audio with configured frame size and hop."""
        # TODO: Support arbitrary input lengths and overlapping frames.
        raise NotImplementedError

    def hamming_window(self, frames: NDArray[np.float32]) -> NDArray[np.float32]:
        """Apply a Hamming window to each frame."""
        # TODO: Use vectorized NumPy windowing.
        raise NotImplementedError

    def stft(self, samples: NDArray[np.float32]) -> NDArray[np.complex64]:
        """Compute a short-time Fourier transform."""
        # TODO: Use scipy.signal.stft with the configured sample rate.
        raise NotImplementedError

    def extract_mfcc(self, samples: NDArray[np.float32]) -> NDArray[np.float32]:
        """Extract Mel-filterbank features and MFCCs."""
        # TODO: Build Mel features and coefficients with librosa or SciPy.
        raise NotImplementedError
