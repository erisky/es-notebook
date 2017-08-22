#
#  Testserver Makefile
#


cmake_minimum_required(VERSION 2.8)
project(testsever)


option(TEST_SAMPLE_OPTION "SAMPLE OPTION" OFF)


if (TEST_SAMPLE_OPTION )
    message("Do something for not sample option!")
endif(TEST_SAMPLE_OPTION)

message("OPTION TEST_SAMPLE_OPTION=${TEST_SAMPLE_OPTION}")

# Add version number
set (TESTSERVER_VERSION_MAJOR 1)
set (TESTSERVER_VERSION_MINOR 2)

option(BUILD_UTHASH_EXAMPLE "Build the UTHASH example" ON) 
option(UV_IPC_USE_PIPE "Build uv echo server/client using pipe" ON)

include_directories("${PROJECT_SOURCE_DIR}")


set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pthread")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g")

set(EXTRA_LIBS)
list(APPEND EXTRA_LIBS websockets)
list(APPEND EXTRA_LIBS crypto)
list(APPEND EXTRA_LIBS ssl)
list(APPEND EXTRA_LIBS json-c)

add_executable(acp_server test-server-pthreads.c test-server-http.c test-server-dumb-increment.c )
add_executable(acp_server_no_pth test-server.c test-server-http.c test-server-dumb-increment.c test-server-file.c)
add_executable(test_client test-client.c test-server-file.c )
add_executable(file_client test-file-client.c test-server-file.c )
target_link_libraries(acp_server ${EXTRA_LIBS})
target_link_libraries(acp_server_no_pth ${EXTRA_LIBS})
target_link_libraries(test_client ${EXTRA_LIBS})
target_link_libraries(file_client ${EXTRA_LIBS})



set(UV_LIBS)
list(APPEND UV_LIBS uv)
add_executable(sample_echo sample_echo_server.c)
target_link_libraries(sample_echo ${UV_LIBS})

add_executable(test-tty test-tty.c)
target_link_libraries(test-tty ${UV_LIBS})

add_executable(uv_workq uv_workqueue.c)
target_link_libraries(uv_workq ${UV_LIBS})

add_executable(uv_signal uv_signal.c)
target_link_libraries(uv_signal ${UV_LIBS})




if (UV_IPC_USE_PIPE)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DUV_IPC_PIPE")
endif(UV_IPC_USE_PIPE)

if (BUILD_UTHASH_EXAMPLE ) 
    include_directories("${PROJECT_SOURCE_DIR}/inc/")

    add_executable(uthash_test uthash_test.c)
    add_executable(utlist_test utlist_test.c)
    add_executable(uthash_sample uthash_sample.c)
endif()



