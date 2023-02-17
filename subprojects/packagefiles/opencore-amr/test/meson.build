executable('amrwb-dec',
  'amrwb-dec.c', 'wavwriter.c',
  dependencies: opencore_amrwb_dep,
  install: true)

linkboth_args = []

if not get_option('amrnb-decoder').disabled()
  executable('amrnb-dec',
    'amrnb-dec.c', 'wavwriter.c',
    dependencies: opencore_amrnb_dep,
    install: true)
else
  linkboth_args += ['-DDISABLE_AMRNB_DECODER']
endif

if not get_option('amrnb-encoder').disabled()
  executable('amrnb-enc',
    'amrnb-enc.c', 'wavreader.c',
    dependencies: opencore_amrnb_dep,
    install: true)

  executable('amrnb-enc-sine',
    'amrnb-enc-sine.c',
    dependencies: [opencore_amrnb_dep, libm],
    install: false)
else
  linkboth_args += ['-DDISABLE_AMRNB_ENCODER']
endif

# skipped: linkboth_LDFLAGS = -static
executable('linkboth',
  'linkboth.c',
  c_args: linkboth_args,
  dependencies: [opencore_amrnb_dep, opencore_amrwb_dep],
  install: false)

