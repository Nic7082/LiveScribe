"""Live spectrogram and transcript visualization interfaces."""

from __future__ import annotations

from collections.abc import Sequence

from numpy.typing import NDArray


class LiveVisualizer:
    """Display a rolling spectrogram alongside recognized text."""

    def __init__(self, sample_rate_hz: int = 16000) -> None:
        self.sample_rate_hz = sample_rate_hz

    def update_spectrogram(self, spectrum: NDArray) -> None:
        """Append a spectral frame to the live display."""
        # TODO: Implement a matplotlib or pyqtgraph rolling view.
        raise NotImplementedError

    def update_transcript(self, segments: Sequence[str]) -> None:
        """Refresh the displayed transcript segments."""
        # TODO: Implement live transcript rendering.
        raise NotImplementedError

    def run(self) -> None:
        """Start the visualization event loop."""
        # TODO: Keep GUI work on the GUI thread.
        raise NotImplementedError
