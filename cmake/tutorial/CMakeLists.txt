#
# Run the tutorial by hand
#


cmake_minimum_required(VERSION 2.6)
project(Tutorial)

option(USE_MYSQRT
        "Use our own SQRT?" on )


include (CheckFunctionExists)
check_function_exists(log HAVE_LOG)
check_function_exists(exp HAVE_EXP)
check_function_exists(printf HAVE_PRINTF)


set (CMAKE_INSTALL_PREFIX /home/eric/testcmke)

# Add version number
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 2)

# configurable header file
configure_file(
    "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
    "${PROJECT_SOURCE_DIR}/TutorialConfig.h"
    )

include_directories("${PROJECT_SOURCE_DIR}")

include_directories("${PROJECT_SOURCE_DIR}/lib")
set(EXTRA_LIBS json-c)

if (USE_MYSQRT)
    include_directories("${PROJECT_SOURCE_DIR}/my_sqrt")
    add_subdirectory(my_sqrt)
    #add_library(my_sqrt my_sqrt.c)
    set (EXTRA_LIBS ${EXTRA_LIBS} my_sqrt)
endif (USE_MYSQRT)

add_executable(Tutorial tutorial.c)
target_link_libraries(Tutorial ${EXTRA_LIBS})


install (TARGETS Tutorial DESTINATION bin)
#install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h" DESTINATION include)


# build a CPack driven installer package
include (InstallRequiredSystemLibraries)
set (CPACK_RESOURCE_FILE_LICENSE  
         "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set (CPACK_PACKAGE_VERSION_MAJOR "${Tutorial_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${Tutorial_VERSION_MINOR}")
include (CPack)


