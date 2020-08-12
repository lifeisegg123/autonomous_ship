# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "autonomous_ship: 4 messages, 0 services")

set(MSG_I_FLAGS "-Iautonomous_ship:/home/ubuntu/catkin_ws/src/autonomous_ship/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(autonomous_ship_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg" NAME_WE)
add_custom_target(_autonomous_ship_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autonomous_ship" "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg" ""
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg" NAME_WE)
add_custom_target(_autonomous_ship_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autonomous_ship" "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg" ""
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg" NAME_WE)
add_custom_target(_autonomous_ship_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autonomous_ship" "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg" ""
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg" NAME_WE)
add_custom_target(_autonomous_ship_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autonomous_ship" "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autonomous_ship
)
_generate_msg_cpp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autonomous_ship
)
_generate_msg_cpp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autonomous_ship
)
_generate_msg_cpp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autonomous_ship
)

### Generating Services

### Generating Module File
_generate_module_cpp(autonomous_ship
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autonomous_ship
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(autonomous_ship_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(autonomous_ship_generate_messages autonomous_ship_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_cpp _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_cpp _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_cpp _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_cpp _autonomous_ship_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autonomous_ship_gencpp)
add_dependencies(autonomous_ship_gencpp autonomous_ship_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autonomous_ship_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autonomous_ship
)
_generate_msg_eus(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autonomous_ship
)
_generate_msg_eus(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autonomous_ship
)
_generate_msg_eus(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autonomous_ship
)

### Generating Services

### Generating Module File
_generate_module_eus(autonomous_ship
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autonomous_ship
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(autonomous_ship_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(autonomous_ship_generate_messages autonomous_ship_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_eus _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_eus _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_eus _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_eus _autonomous_ship_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autonomous_ship_geneus)
add_dependencies(autonomous_ship_geneus autonomous_ship_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autonomous_ship_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autonomous_ship
)
_generate_msg_lisp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autonomous_ship
)
_generate_msg_lisp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autonomous_ship
)
_generate_msg_lisp(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autonomous_ship
)

### Generating Services

### Generating Module File
_generate_module_lisp(autonomous_ship
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autonomous_ship
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(autonomous_ship_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(autonomous_ship_generate_messages autonomous_ship_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_lisp _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_lisp _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_lisp _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_lisp _autonomous_ship_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autonomous_ship_genlisp)
add_dependencies(autonomous_ship_genlisp autonomous_ship_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autonomous_ship_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autonomous_ship
)
_generate_msg_nodejs(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autonomous_ship
)
_generate_msg_nodejs(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autonomous_ship
)
_generate_msg_nodejs(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autonomous_ship
)

### Generating Services

### Generating Module File
_generate_module_nodejs(autonomous_ship
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autonomous_ship
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(autonomous_ship_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(autonomous_ship_generate_messages autonomous_ship_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_nodejs _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_nodejs _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_nodejs _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_nodejs _autonomous_ship_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autonomous_ship_gennodejs)
add_dependencies(autonomous_ship_gennodejs autonomous_ship_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autonomous_ship_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship
)
_generate_msg_py(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship
)
_generate_msg_py(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship
)
_generate_msg_py(autonomous_ship
  "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship
)

### Generating Services

### Generating Module File
_generate_module_py(autonomous_ship
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(autonomous_ship_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(autonomous_ship_generate_messages autonomous_ship_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/motorValue.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_py _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/gps.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_py _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/lidar.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_py _autonomous_ship_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/autonomous_ship/msg/imu.msg" NAME_WE)
add_dependencies(autonomous_ship_generate_messages_py _autonomous_ship_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autonomous_ship_genpy)
add_dependencies(autonomous_ship_genpy autonomous_ship_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autonomous_ship_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autonomous_ship)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autonomous_ship
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(autonomous_ship_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autonomous_ship)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autonomous_ship
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(autonomous_ship_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autonomous_ship)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autonomous_ship
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(autonomous_ship_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autonomous_ship)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autonomous_ship
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(autonomous_ship_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autonomous_ship
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(autonomous_ship_generate_messages_py std_msgs_generate_messages_py)
endif()
