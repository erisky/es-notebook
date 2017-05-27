#
# Run the tutorial by hand
#


cmake_minimum_required(VERSION 2.6)
project(Tutorial)

# Add version number
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 2)

# configurable header file
configure_file(
    "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
    "${PROJECT_SOURCE_DIR}/TutorialConfig.h"
    )

include_directories("${PROJECT_SOURCE_DIR}")

if (USE_MYSQRT)
    include_directories("${PROJECT_SOURCE_DIR}/my_sqrt")
    add_subdirectory(my_sqrt)
    #add_library(my_sqrt my_sqrt.c)
    set (EXTRA_LIBS ${EXTRA_LIBS} my_sqrt)
endif (USE_MYSQRT)

option(USE_MYSQRT
        "Use our own SQRT?" )

add_executable(Tutorial tutorial.c)
target_link_libraries(Tutorial ${EXTRA_LIBS})
