install_headers(['dec_if.h', 'if_rom.h'], subdir: 'opencore-amrwb')

dec_src_dir = '../opencore/codecs_v2/audio/gsm_amr/amr_wb/dec/src/'

amrwb_incs = include_directories(
  '../opencore/codecs_v2/audio/gsm_amr/amr_wb/dec/src',
  '../opencore/codecs_v2/audio/gsm_amr/amr_wb/dec/include',
  '../opencore/codecs_v2/audio/gsm_amr/common/dec/include',
)

# Our sources to include. There are certain sources we exclude and they are
# $(dec_src_dir)/decoder_amr_wb.cpp
opencore_amrwb_sources = files([
  'wrapper.cpp',
  dec_src_dir + 'agc2_amr_wb.cpp',
  dec_src_dir + 'band_pass_6k_7k.cpp',
  dec_src_dir + 'dec_acelp_2p_in_64.cpp',
  dec_src_dir + 'dec_acelp_4p_in_64.cpp',
  dec_src_dir + 'dec_alg_codebook.cpp',
  dec_src_dir + 'dec_gain2_amr_wb.cpp',
  dec_src_dir + 'deemphasis_32.cpp',
  dec_src_dir + 'dtx_decoder_amr_wb.cpp',
  dec_src_dir + 'get_amr_wb_bits.cpp',
  dec_src_dir + 'highpass_400hz_at_12k8.cpp',
  dec_src_dir + 'highpass_50hz_at_12k8.cpp',
  dec_src_dir + 'homing_amr_wb_dec.cpp',
  dec_src_dir + 'interpolate_isp.cpp',
  dec_src_dir + 'isf_extrapolation.cpp',
  dec_src_dir + 'isp_az.cpp',
  dec_src_dir + 'isp_isf.cpp',
  dec_src_dir + 'lagconceal.cpp',
  dec_src_dir + 'low_pass_filt_7k.cpp',
  dec_src_dir + 'median5.cpp',
  dec_src_dir + 'mime_io.cpp',
  dec_src_dir + 'noise_gen_amrwb.cpp',
  dec_src_dir + 'normalize_amr_wb.cpp',
  dec_src_dir + 'oversamp_12k8_to_16k.cpp',
  dec_src_dir + 'phase_dispersion.cpp',
  dec_src_dir + 'pit_shrp.cpp',
  dec_src_dir + 'pred_lt4.cpp',
  dec_src_dir + 'preemph_amrwb_dec.cpp',
  dec_src_dir + 'pvamrwbdecoder.cpp',
  dec_src_dir + 'pvamrwb_math_op.cpp',
  dec_src_dir + 'q_gain2_tab.cpp',
  dec_src_dir + 'qisf_ns.cpp',
  dec_src_dir + 'qisf_ns_tab.cpp',
  dec_src_dir + 'qpisf_2s.cpp',
  dec_src_dir + 'qpisf_2s_tab.cpp',
  dec_src_dir + 'scale_signal.cpp',
  dec_src_dir + 'synthesis_amr_wb.cpp',
  dec_src_dir + 'voice_factor.cpp',
  dec_src_dir + 'wb_syn_filt.cpp',
  dec_src_dir + 'weight_amrwb_lpc.cpp',
])

amrwb_link_args = cxx.get_supported_link_arguments(
  '-Wl,--version-script,@0@/libopencore-amrwb.map'.format(meson.current_source_dir()),
)

libopencore_amrwb = library('opencore-amrwb',
  opencore_amrwb_sources,
  cpp_args: amr_lib_args,
  include_directories: [oscl_incs, amrwb_incs],
  link_args: amrwb_link_args,
  link_language: amr_lib_link_language,
  version: libversion,
  vs_module_defs: 'opencore-amrwb.def',
  install: true)

pkg = import('pkgconfig')
pkg.generate(libopencore_amrwb,
  filebase: 'opencore-amrwb',
  subdirs: 'opencore-amrwb',
  name: 'OpenCORE AMR-WB',
  description: 'Adaptive Multi-Rate Wideband speech codec library')

opencore_amrwb_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: libopencore_amrwb,
)
