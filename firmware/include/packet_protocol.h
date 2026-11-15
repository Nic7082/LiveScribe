#ifndef LIVESCRIBE_PACKET_PROTOCOL_H
#define LIVESCRIBE_PACKET_PROTOCOL_H

#include <stdint.h>

#include "audio_config.h"

#define PACKET_MAGIC 0xAA55U
#define PACKET_MAX_PAYLOAD_BYTES (FRAME_SIZE_SAMPLES * sizeof(uint16_t))

#pragma pack(push, 1)
typedef struct {
    uint16_t magic;
    uint16_t sequence;
    uint16_t payload_length;
    uint16_t pcm_samples[FRAME_SIZE_SAMPLES];
    uint16_t crc16_xor;
} audio_packet_t;
#pragma pack(pop)

uint16_t packet_crc16_xor(const uint8_t *data, uint16_t length);

#endif
