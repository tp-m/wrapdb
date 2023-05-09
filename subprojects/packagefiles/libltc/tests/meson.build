ltcencode = executable('ltcencode', 'ltcencode.c',
  dependencies: ltc_dep,
  include_directories: ltc_incs,
  install: false)

ltcdecode = executable('ltcdecode', 'ltcdecode.c',
  dependencies: ltc_dep,
  include_directories: ltc_incs,
  install: false)

ltcloop = executable('ltcloop', 'ltcloop.c',
  dependencies: ltc_dep,
  include_directories: ltc_incs,
  install: false)

enc_dec = find_program('enc-dec-diff.py', required: true)

#	ltcencode output.raw
# ltcdecode output.raw | diff -q $(srcdir)/expect_48k_2sec.txt -

# Add build directory of the library to the PATH manually, so
# the unit test executables can find it. Usually Meson will do
# that for us automatically, but here we're calling the executables
# via a wrapper script so it doesn't know that's needed in our case.
test_env = environment()
if host_machine.system() == 'windows'
  test_env.append('PATH', ltc_builddir)
endif

test('encode-decode-48k-2s', enc_dec,
  depends: [ltcencode, ltcdecode, libltc],
  env: test_env,
  args: [
    '--encoder=' + ltcencode.full_path(),
    '--decoder=' + ltcdecode.full_path(),
    'output-48k-2s.raw',
    files('expect_48k_2sec.txt'),
  ])

# ltcencode output.raw 192000
# ltcdecode output.raw 7680 | diff -q $(srcdir)/expect_96k_2sec.txt -

test('encode-decode-96k-2s', enc_dec,
  depends: [ltcencode, ltcdecode, libltc],
  env: test_env,
  args: [
    '--encoder=' + ltcencode.full_path(),
    '--encoder-rate=192000',
    '--decoder=' + ltcdecode.full_path(),
    '--decoder-audio-frames-per-video-frame=7680',
    'output-96k-2s.raw',
    files('expect_96k_2sec.txt'),
  ])

# ltcdecode $(srcdir)/timecode.raw 882 | diff -q $(srcdir)/timecode.txt -

test('decode', enc_dec,
  depends: [ltcencode, ltcdecode, libltc],
  env: test_env,
  args: [
    '--decoder=' + ltcdecode.full_path(),
    '--decoder-audio-frames-per-video-frame=882',
    files('timecode.raw'),
    files('timecode.txt'),
  ])

# ltcloop

test('ltcloop', ltcloop, env: test_env)