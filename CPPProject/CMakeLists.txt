cmake_minimum_required(VERSION 3.15)

# Название проекта
project(SegmentTreeLibrary LANGUAGES CXX)

# Установить стандарт C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Определить имя библиотеки в зависимости от платформы
if (WIN32)
    set(LIBRARY_NAME "libsegment_tree.dll")
else ()
    set(LIBRARY_NAME "libsegment_tree.so")
endif ()

# Указать исходные файлы
set(SOURCES
    src/segment_tree.cpp
    src/segment_tree.h
)

# Создать библиотеку
add_library(${LIBRARY_NAME} SHARED ${SOURCES})

# Указать, куда устанавливать библиотеку
set_target_properties(${LIBRARY_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)

# Опции для Windows (dll)
if (WIN32)
    target_compile_definitions(${LIBRARY_NAME} PRIVATE EXPORTING_DLL)
endif ()

# Опции для Linux (so)
if (UNIX)
    target_compile_options(${LIBRARY_NAME} PRIVATE -fPIC)
endif ()

# Тесты (если нужны)
enable_testing()
