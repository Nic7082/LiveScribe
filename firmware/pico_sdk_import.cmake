if(NOT DEFINED PICO_SDK_PATH)
    if(DEFINED ENV{PICO_SDK_PATH})
        set(PICO_SDK_PATH "$ENV{PICO_SDK_PATH}")
    else()
        message(FATAL_ERROR
            "PICO_SDK_PATH is not set. Set it to the Raspberry Pi Pico SDK directory."
        )
    endif()
endif()

if(NOT EXISTS "${PICO_SDK_PATH}/external/pico_sdk_import.cmake")
    message(FATAL_ERROR
        "Pico SDK import file not found under PICO_SDK_PATH='${PICO_SDK_PATH}'."
    )
endif()

include("${PICO_SDK_PATH}/external/pico_sdk_import.cmake")
