"""Plot the analog Bode response of an 8 kHz Sallen-Key low-pass filter."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def main() -> None:
    """Calculate and plot a second-order Butterworth Sallen-Key filter."""
    cutoff_hz = 8000.0
    resistance_ohms = 1000.0
    capacitance_f = 1.0 / (2.0 * np.pi * resistance_ohms * cutoff_hz)
    amplifier_gain = 3.0 - 1.0 / np.sqrt(2.0)

    # Equal R/C Sallen-Key components with gain set for a Butterworth response.
    numerator = [amplifier_gain]
    denominator = [
        resistance_ohms**2 * capacitance_f**2,
        resistance_ohms * capacitance_f * (3.0 - amplifier_gain),
        1.0,
    ]
    system = signal.TransferFunction(numerator, denominator)
    frequencies = np.logspace(1, 5, 800)
    frequencies, magnitude_db, phase_deg = signal.bode(system, w=2.0 * np.pi * frequencies)

    figure, (magnitude_axis, phase_axis) = plt.subplots(2, 1, sharex=True)
    magnitude_axis.semilogx(frequencies / (2.0 * np.pi), magnitude_db)
    magnitude_axis.set_ylabel("Magnitude (dB)")
    magnitude_axis.grid(True, which="both")
    phase_axis.semilogx(frequencies / (2.0 * np.pi), phase_deg)
    phase_axis.set_xlabel("Frequency (Hz)")
    phase_axis.set_ylabel("Phase (degrees)")
    phase_axis.grid(True, which="both")
    figure.suptitle("LiveScribe Sallen-Key anti-aliasing filter (fc = 8 kHz)")
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
