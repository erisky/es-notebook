#
# Run the postgre by hand
#


cmake_minimum_required(VERSION 2.6)
project(postgre)


include (CheckFunctionExists)
check_function_exists(log HAVE_LOG)
check_function_exists(exp HAVE_EXP)
check_function_exists(printf HAVE_PRINTF)


# Add version number
set (postgre_VERSION_MAJOR 1)
set (postgre_VERSION_MINOR 2)

# configurable header file
configure_file(
    "${PROJECT_SOURCE_DIR}/postgreConfig.h.in"
    "${PROJECT_SOURCE_DIR}/postgreConfig.h"
    )

include_directories("${PROJECT_SOURCE_DIR}")


link_directories(/usr/lib/ /usr/lib/x86_64-linux-gnu/ )

set (EXTRA_LIBS ${EXTRA_LIBS} pthread pq)
add_executable(postgre postgre.c)

target_link_libraries(postgre  ${EXTRA_LIBS})


install (TARGETS postgre DESTINATION bin)
#install (FILES "${PROJECT_BINARY_DIR}/postgreConfig.h" DESTINATION include)


# build a CPack driven installer package
include (InstallRequiredSystemLibraries)
set (CPACK_RESOURCE_FILE_LICENSE  
         "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set (CPACK_PACKAGE_VERSION_MAJOR "${postgre_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${postgre_VERSION_MINOR}")
include (CPack)


