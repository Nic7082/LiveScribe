#include "pico/stdlib.h"

#include "dma_adc_driver.h"
#include "packet_protocol.h"

int main(void)
{
    stdio_init_all();

    if (!dma_adc_init()) {
        return 1;
    }

    dma_adc_start();

    while (true) {
        /* TODO: Packetize completed DMA buffers and stream them over USB CDC. */
        tight_loop_contents();
    }
}
