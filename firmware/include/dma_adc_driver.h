#ifndef LIVESCRIBE_DMA_ADC_DRIVER_H
#define LIVESCRIBE_DMA_ADC_DRIVER_H

#include <stdbool.h>
#include <stdint.h>

#include "audio_config.h"

bool dma_adc_init(void);
void dma_adc_start(void);
void dma_adc_stop(void);
const uint16_t *dma_adc_get_completed_buffer(uint8_t *buffer_index);

#endif
