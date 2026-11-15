# LiveScribe firmware

The firmware targets the Raspberry Pi Pico / RP2040 and uses the Raspberry Pi Pico C/C++ SDK. ADC acquisition and DMA buffering are isolated behind `include/dma_adc_driver.h`; audio frame settings live in `include/audio_config.h`.

## Build

Install the Pico SDK and supported ARM embedded toolchain, and set `PICO_SDK_PATH` to the SDK checkout. Then run:

```sh
mkdir build && cd build
cmake ..
make
```

`livescribe_fw.uf2` is generated in the build directory. USB stdio is enabled for the USB CDC data connection and UART stdio is disabled. Packet framing and ping-pong DMA handling are starter interfaces and still require implementation.
