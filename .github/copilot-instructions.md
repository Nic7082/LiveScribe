# LiveScribe Project Conventions

## Architecture Overview
- **Signal flow:** Electret microphone -> analog anti-aliasing low-pass filter (8 kHz cutoff) -> RP2040 ADC (16 kHz, 12-bit samples represented as 16-bit PCM) -> ping-pong DMA -> USB CDC binary stream -> Python DSP (STFT/Mel/MFCC) -> ASR -> live transcript.
- **Endianness:** Multi-byte integers and PCM samples in firmware packets and the Python serial parser are little-endian.
- Keep the firmware packet layout and host parser in sync. The payload length is measured in bytes.

## Firmware (`firmware/`)
- Target the RP2040 with the Raspberry Pi Pico C/C++ SDK and C11.
- Do not use blocking delays or `printf` inside ADC/DMA interrupt handlers.
- Keep ADC and DMA register-level logic isolated in `dma_adc_driver.c`.
- USB CDC is the raw audio transport; keep UART stdio disabled.
- Keep frame and sampling parameters centralized in `include/audio_config.h`.

## Host Software (`software/`)
- Target Python 3.10+ and use PEP 484 type annotations on all function signatures.
- Decouple serial I/O, DSP feature extraction, ASR inference, and visualization with thread-safe `queue.Queue` buffers.
- Use vectorized NumPy/SciPy operations for sample processing; avoid Python loops for array-wide transformations.
- Validate packet synchronization, lengths, and checksums before publishing audio frames.
- Keep hardware access and model loading out of module import time so utilities remain testable.

## Tests and generated files
- Add or update tests alongside changes to packet parsing, DSP, and framing.
- Keep generated plots, transcripts, model artifacts, and recordings out of source control unless explicitly required.
- Run Python tests with `python -m pytest software/tests`; build firmware from `firmware/build`.
