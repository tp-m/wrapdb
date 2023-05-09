project('libltc', 'c',
  version: run_command(find_program('meson/get-version.py'), '--package-version', check: true).stdout().strip())

libversion = run_command('meson/get-version.py', '--libtool-version', check: true).stdout().strip()
macosversion = run_command('meson/get-version.py', '--darwin-version', check: true).stdout().strip()

# Not defining HAVE_CONFIG_H because we don't actually have anything to put into it
# add_project_arguments('-DHAVE_CONFIG_H', language: 'c')

cc = meson.get_compiler('c')

foreach header : ['stdio.h', 'stdlib.h', 'string.h', 'math.h', 'stdint.h', 'stddef.h']
  if not cc.has_header(header)
    error(f'Header <@header@> required but not found. Compiler:', cc.get_id(), cc.version())
  endif
endforeach

if cc.get_define('__BYTE_ORDER__') == ''
  if not cc.has_header('endian.h')
    add_project_arguments([
      '-D__BIG_ENDIAN__=4321',
      '-D__LITTLE_ENDIAN__=1234',
      '-D__BYTE_ORDER__=__@0@_ENDIAN__'.format(host_machine.endian().to_upper())
    ], language: 'c')
  endif
endif

libm = cc.find_library('m', required: false)

subdir('src')

if not get_option('tests').disabled()
  subdir('tests')
endif

pkg = import('pkgconfig')
pkg.generate(libltc,
  filebase: 'ltc',
  name: 'libltc',
  description: 'linear/longitudinal timecode library',
)
