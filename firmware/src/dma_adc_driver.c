#include "dma_adc_driver.h"

#include "hardware/adc.h"
#include "hardware/dma.h"
#include "hardware/irq.h"

bool dma_adc_init(void)
{
    /* TODO: Configure the ADC, ping-pong DMA channels, and completion IRQ. */
    return false;
}

void dma_adc_start(void)
{
    /* TODO: Start ADC conversions and the first DMA transfer. */
}

void dma_adc_stop(void)
{
    /* TODO: Stop ADC and both DMA channels safely. */
}

const uint16_t *dma_adc_get_completed_buffer(uint8_t *buffer_index)
{
    /* TODO: Return the completed ping-pong buffer and its index. */
    (void)buffer_index;
    return 0;
}
