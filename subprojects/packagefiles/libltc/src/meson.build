install_headers('ltc.h')

ltc_incs = include_directories('.')

libltc = library('ltc',
  'ltc.c', 'decoder.c', 'encoder.c', 'timecode.c',
  include_directories: [ltc_incs],
  dependencies: [libm],
  version: libversion,
  darwin_versions: macosversion,
  vs_module_defs: 'libltc.def',
  install: true)

ltc_dep = declare_dependency(
  include_directories: [ltc_incs],
  dependencies: libm,
  link_with: libltc)

ltc_builddir = meson.current_build_dir()