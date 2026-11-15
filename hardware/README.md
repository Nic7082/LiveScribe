# LiveScribe hardware

Hardware work covers the microphone input path and the RP2040 interface. The analog front end should provide suitable microphone bias/pre-amplification and an anti-aliasing low-pass response with an 8 kHz cutoff before 16 kHz ADC sampling.

- `schematic/` — schematic source files.
- `pcb/` — PCB layout and fabrication files.
- `libraries/` — project-specific symbols and footprints.
- `bom/bom.csv` — component bill of materials.

The design folders are initialized with `.gitkeep` files until their native design files are added.
