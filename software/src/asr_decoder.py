"""Sliding-window speech recognition interface."""

from __future__ import annotations

from numpy.typing import NDArray


class ASRDecoder:
    """Wrap a streaming or sliding-window automatic speech recognizer."""

    def __init__(self, model_name: str = "base.en", device: str = "cpu") -> None:
        self.model_name = model_name
        self.device = device
        self._model: object | None = None

    def load_model(self) -> None:
        """Load the selected ASR model on the configured device."""
        # TODO: Initialize the Whisper model lazily.
        raise NotImplementedError

    def transcribe(self, audio: NDArray) -> str:
        """Transcribe an audio window and return its text."""
        # TODO: Add overlapping-window inference and transcript stitching.
        raise NotImplementedError
