# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "humanoid: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ihumanoid:/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/noetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(humanoid_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg" NAME_WE)
add_custom_target(_humanoid_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "humanoid" "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(humanoid
  "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/humanoid
)

### Generating Services

### Generating Module File
_generate_module_cpp(humanoid
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/humanoid
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(humanoid_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(humanoid_generate_messages humanoid_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg" NAME_WE)
add_dependencies(humanoid_generate_messages_cpp _humanoid_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(humanoid_gencpp)
add_dependencies(humanoid_gencpp humanoid_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS humanoid_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(humanoid
  "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/humanoid
)

### Generating Services

### Generating Module File
_generate_module_eus(humanoid
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/humanoid
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(humanoid_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(humanoid_generate_messages humanoid_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg" NAME_WE)
add_dependencies(humanoid_generate_messages_eus _humanoid_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(humanoid_geneus)
add_dependencies(humanoid_geneus humanoid_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS humanoid_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(humanoid
  "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/humanoid
)

### Generating Services

### Generating Module File
_generate_module_lisp(humanoid
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/humanoid
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(humanoid_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(humanoid_generate_messages humanoid_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg" NAME_WE)
add_dependencies(humanoid_generate_messages_lisp _humanoid_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(humanoid_genlisp)
add_dependencies(humanoid_genlisp humanoid_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS humanoid_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(humanoid
  "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/humanoid
)

### Generating Services

### Generating Module File
_generate_module_nodejs(humanoid
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/humanoid
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(humanoid_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(humanoid_generate_messages humanoid_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg" NAME_WE)
add_dependencies(humanoid_generate_messages_nodejs _humanoid_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(humanoid_gennodejs)
add_dependencies(humanoid_gennodejs humanoid_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS humanoid_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(humanoid
  "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/humanoid
)

### Generating Services

### Generating Module File
_generate_module_py(humanoid
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/humanoid
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(humanoid_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(humanoid_generate_messages humanoid_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/Desktop/git_codes/Humanoid-VIT/src/humanoid/msg/Coordinates.msg" NAME_WE)
add_dependencies(humanoid_generate_messages_py _humanoid_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(humanoid_genpy)
add_dependencies(humanoid_genpy humanoid_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS humanoid_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/humanoid)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/humanoid
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(humanoid_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(humanoid_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/humanoid)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/humanoid
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(humanoid_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(humanoid_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/humanoid)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/humanoid
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(humanoid_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(humanoid_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/humanoid)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/humanoid
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(humanoid_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(humanoid_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/humanoid)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/humanoid\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/humanoid
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(humanoid_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(humanoid_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
