# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_hivebot_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED hivebot_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(hivebot_FOUND FALSE)
  elseif(NOT hivebot_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(hivebot_FOUND FALSE)
  endif()
  return()
endif()
set(_hivebot_CONFIG_INCLUDED TRUE)

# output package information
if(NOT hivebot_FIND_QUIETLY)
  message(STATUS "Found hivebot: 0.0.0 (${hivebot_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'hivebot' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${hivebot_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(hivebot_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${hivebot_DIR}/${_extra}")
endforeach()
