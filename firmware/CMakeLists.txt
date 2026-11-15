cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(livescribe_fw C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_executable(livescribe_fw
    src/main.c
    src/dma_adc_driver.c
)

target_include_directories(livescribe_fw PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/include
)

target_link_libraries(livescribe_fw
    pico_stdlib
    hardware_adc
    hardware_dma
    hardware_irq
)

pico_enable_stdio_usb(livescribe_fw 1)
pico_enable_stdio_uart(livescribe_fw 0)
pico_add_extra_outputs(livescribe_fw)
