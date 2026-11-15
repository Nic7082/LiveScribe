# LiveScribe

LiveScribe is a real-time speech-to-text system built around a Raspberry Pi Pico (RP2040). The Pico samples microphone audio at 16 kHz and streams framed PCM over USB CDC; a Python host application validates packets, processes audio features, runs speech recognition, and presents a live transcript.

## Architecture

```text
Electret microphone -> 8 kHz anti-aliasing low-pass filter -> RP2040 ADC
-> ping-pong DMA -> USB CDC PCM packets -> Python DSP -> ASR -> live transcript
```

The firmware uses 320-sample (20 ms) audio frames, with a 160-sample hop (50% overlap). Packet fields and multi-byte samples use little-endian byte order.

## Repository layout

- `firmware/` — Pico SDK firmware, ADC/DMA interface, and packet protocol.
- `software/` — Python serial, DSP, ASR, and visualization modules.
- `hardware/` — hardware documentation, design directories, and bill of materials.
- `simulations/` — filter-response and audio-feature experiments.
- `data/` and `outputs/` — local sample data and generated artifacts.

## Setup

### Firmware

Install the Raspberry Pi Pico C/C++ SDK and its toolchain, then set `PICO_SDK_PATH` to the SDK directory. Build from the firmware directory:

```sh
cd firmware
mkdir build && cd build
cmake ..
make
```

The build produces `livescribe_fw.uf2` for the Pico. Connect the board over USB and copy the UF2 file to its bootloader drive. USB stdio is enabled for CDC streaming; UART stdio is disabled.

### Host software

Use Python 3.10 or later:

```sh
python -m venv .venv
# Activate the virtual environment for your shell.
python -m pip install -r software/requirements.txt
python -m software.src.main --help
```

PyTorch and torchaudio may require installation of builds matching the host's operating system and accelerator. The modules are starter interfaces; hardware streaming and model integration remain to be implemented.

### Hardware and simulation

See `hardware/README.md` for the design folders and BOM. Install the host dependencies before running a simulation, for example:

```sh
python simulations/scripts/filter_response.py
python simulations/scripts/stft_mfcc_bench.py
```

## Team roles

The four-person team can divide ownership across these interfaces:

1. **Embedded firmware:** ADC sampling, DMA buffering, USB CDC transport, and packet framing.
2. **Hardware design:** microphone preamplifier, anti-aliasing filter, schematic, PCB, and BOM.
3. **Signal processing:** host packet ingestion, framing, STFT, and Mel/MFCC features.
4. **Speech recognition and integration:** ASR inference, live visualization, and end-to-end testing.

## Development

Python tests are under `software/tests/` and can be run with:

```sh
python -m pytest software/tests
```
