# Meson build for opencore-amr <http://sourceforge.net/projects/opencore-amr/>
# Copyright (C) 2023 Tim-Philipp Müller <tim centricular com>
# SPDX-License-Identifier: Apache-2.0
project('opencore-amr', 'c', 'cpp', version: '0.1.6',
  meson_version: '>= 0.64.0',
  default_options: ['buildtype=debugoptimized'])

libversion = '0.0.5'

cc = meson.get_compiler('c')
cxx = meson.get_compiler('cpp')

libm = cc.find_library('m', required: false)

# Required headers
cc.has_header('stdint.h', required: true)
cc.has_header('stdlib.h', required: true)
cc.has_header('string.h', required: true)
cxx.has_header('stdbool.h', required: true)

# Required types
required_types = [
  'int16_t', 'int32_t', 'int64_t', 'int8_t',
  'uint16_t', 'uint32_t', 'uint64_t', 'uint8_t',
]

foreach type : required_types
  if not cc.has_type(type, prefix: '#include <stdint.h>')
    error(f'Need type {type} in stdint.h')
  endif
endforeach

# Required functions
if not cc.has_function('memset', prefix: '#include <string.h>')
  error('Need memset()')
endif

amr_lib_args = []
if get_option('gcc-armv5').enabled()
  amr_lib_args += ['-DPV_CPU_ARCH_VERSION=5', '-DPV_COMPILER=1']
endif

amr_lib_link_language = 'cpp'
if get_option('compile-c').enabled()
  if cxx.get_argument_syntax() == 'gcc'
    amr_lib_args += cxx.get_supported_arguments('-xc') # FIXME: '-std=c99'
  endif
  amr_lib_link_language = 'c'
endif

oscl_incs = include_directories('oscl')

subdir('amrnb')
subdir('amrwb')

if get_option('examples').allowed()
  subdir('test')
endif
