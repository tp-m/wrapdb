dec_src_dir = '../opencore/codecs_v2/audio/gsm_amr/amr_nb/dec/src/'
enc_src_dir = '../opencore/codecs_v2/audio/gsm_amr/amr_nb/enc/src/'
common_src_dir = '../opencore/codecs_v2/audio/gsm_amr/amr_nb/common/src/'

amrnb_incs = include_directories(
  '../opencore/codecs_v2/audio/gsm_amr/amr_nb/dec/src',
  '../opencore/codecs_v2/audio/gsm_amr/amr_nb/common/include',
  '../opencore/codecs_v2/audio/gsm_amr/amr_nb/dec/include',
  '../opencore/codecs_v2/audio/gsm_amr/common/dec/include',
  '../opencore/codecs_v2/audio/gsm_amr/amr_nb/enc/src',
)

amrnb_args = []

# Our sources to include. There are certain sources we exclude and they are
# $(dec_src_dir)/decoder_gsm_amr.cpp
# $(dec_src_dir)/pvgsmamrdecoder.cpp
# $(enc_src_dir)/gsmamr_encoder_wrapper.cpp
# $(common_src_dir)/bits2prm.cpp
# $(common_src_dir)/copy.cpp
# $(common_src_dir)/div_32.cpp
# $(common_src_dir)/l_abs.cpp
# $(common_src_dir)/r_fft.cpp
# $(common_src_dir)/vad1.cpp
# $(common_src_dir)/vad2.cpp
opencore_amrnb_sources = files('wrapper.cpp')

if not get_option('amrnb-decoder').disabled()
  opencore_amrnb_sources += files([
    dec_src_dir + 'agc.cpp',
    dec_src_dir + 'amrdecode.cpp',
    dec_src_dir + 'a_refl.cpp',
    dec_src_dir + 'b_cn_cod.cpp',
    dec_src_dir + 'bgnscd.cpp',
    dec_src_dir + 'c_g_aver.cpp',
    dec_src_dir + 'd1035pf.cpp',
    dec_src_dir + 'd2_11pf.cpp',
    dec_src_dir + 'd2_9pf.cpp',
    dec_src_dir + 'd3_14pf.cpp',
    dec_src_dir + 'd4_17pf.cpp',
    dec_src_dir + 'd8_31pf.cpp',
    dec_src_dir + 'dec_amr.cpp',
    dec_src_dir + 'dec_gain.cpp',
    dec_src_dir + 'dec_input_format_tab.cpp',
    dec_src_dir + 'dec_lag3.cpp',
    dec_src_dir + 'dec_lag6.cpp',
    dec_src_dir + 'd_gain_c.cpp',
    dec_src_dir + 'd_gain_p.cpp',
    dec_src_dir + 'd_plsf_3.cpp',
    dec_src_dir + 'd_plsf_5.cpp',
    dec_src_dir + 'd_plsf.cpp',
    dec_src_dir + 'dtx_dec.cpp',
    dec_src_dir + 'ec_gains.cpp',
    dec_src_dir + 'ex_ctrl.cpp',
    dec_src_dir + 'if2_to_ets.cpp',
    dec_src_dir + 'int_lsf.cpp',
    dec_src_dir + 'lsp_avg.cpp',
    dec_src_dir + 'ph_disp.cpp',
    dec_src_dir + 'post_pro.cpp',
    dec_src_dir + 'preemph.cpp',
    dec_src_dir + 'pstfilt.cpp',
    dec_src_dir + 'qgain475_tab.cpp',
    dec_src_dir + 'sp_dec.cpp',
    dec_src_dir + 'wmf_to_ets.cpp',
  ])

  install_headers('interf_dec.h', subdir: 'opencore-amrnb')
else
  amrnb_args += ['-DDISABLE_AMRNB_DECODER']
endif

if not get_option('amrnb-encoder').disabled()
  opencore_amrnb_sources += files([
    enc_src_dir + 'amrencode.cpp',
    enc_src_dir + 'autocorr.cpp',
    enc_src_dir + 'c1035pf.cpp',
    enc_src_dir + 'c2_11pf.cpp',
    enc_src_dir + 'c2_9pf.cpp',
    enc_src_dir + 'c3_14pf.cpp',
    enc_src_dir + 'c4_17pf.cpp',
    enc_src_dir + 'c8_31pf.cpp',
    enc_src_dir + 'calc_cor.cpp',
    enc_src_dir + 'calc_en.cpp',
    enc_src_dir + 'cbsearch.cpp',
    enc_src_dir + 'cl_ltp.cpp',
    enc_src_dir + 'cod_amr.cpp',
    enc_src_dir + 'convolve.cpp',
    enc_src_dir + 'cor_h.cpp',
    enc_src_dir + 'cor_h_x2.cpp',
    enc_src_dir + 'cor_h_x.cpp',
    enc_src_dir + 'corrwght_tab.cpp',
    enc_src_dir + 'div_32.cpp',
    enc_src_dir + 'dtx_enc.cpp',
    enc_src_dir + 'enc_lag3.cpp',
    enc_src_dir + 'enc_lag6.cpp',
    enc_src_dir + 'enc_output_format_tab.cpp',
    enc_src_dir + 'ets_to_if2.cpp',
    enc_src_dir + 'ets_to_wmf.cpp',
    enc_src_dir + 'g_adapt.cpp',
    enc_src_dir + 'gain_q.cpp',
    enc_src_dir + 'g_code.cpp',
    enc_src_dir + 'g_pitch.cpp',
    enc_src_dir + 'hp_max.cpp',
    enc_src_dir + 'inter_36.cpp',
    enc_src_dir + 'inter_36_tab.cpp',
    enc_src_dir + 'l_abs.cpp',
    enc_src_dir + 'lag_wind.cpp',
    enc_src_dir + 'lag_wind_tab.cpp',
    enc_src_dir + 'l_comp.cpp',
    enc_src_dir + 'levinson.cpp',
    enc_src_dir + 'l_extract.cpp',
    enc_src_dir + 'lflg_upd.cpp',
    enc_src_dir + 'l_negate.cpp',
    enc_src_dir + 'lpc.cpp',
    enc_src_dir + 'ol_ltp.cpp',
    enc_src_dir + 'pitch_fr.cpp',
    enc_src_dir + 'pitch_ol.cpp',
    enc_src_dir + 'p_ol_wgh.cpp',
    enc_src_dir + 'pre_big.cpp',
    enc_src_dir + 'pre_proc.cpp',
    enc_src_dir + 'prm2bits.cpp',
    enc_src_dir + 'qgain475.cpp',
    enc_src_dir + 'qgain795.cpp',
    enc_src_dir + 'q_gain_c.cpp',
    enc_src_dir + 'q_gain_p.cpp',
    enc_src_dir + 'qua_gain.cpp',
    enc_src_dir + 's10_8pf.cpp',
    enc_src_dir + 'set_sign.cpp',
    enc_src_dir + 'sid_sync.cpp',
    enc_src_dir + 'sp_enc.cpp',
    enc_src_dir + 'spreproc.cpp',
    enc_src_dir + 'spstproc.cpp',
    enc_src_dir + 'ton_stab.cpp',
    enc_src_dir + 'vad1.cpp',
  ])

  install_headers('interf_enc.h', subdir: 'opencore-amrnb')
else
  amrnb_args += ['-DDISABLE_AMRNB_ENCODER']
endif

opencore_amrnb_sources += files([
  common_src_dir + 'add.cpp',
  common_src_dir + 'az_lsp.cpp',
  common_src_dir + 'bitno_tab.cpp',
  common_src_dir + 'bitreorder_tab.cpp',
  common_src_dir + 'c2_9pf_tab.cpp',
  common_src_dir + 'div_s.cpp',
  common_src_dir + 'extract_h.cpp',
  common_src_dir + 'extract_l.cpp',
  common_src_dir + 'gains_tbl.cpp',
  common_src_dir + 'gc_pred.cpp',
  common_src_dir + 'get_const_tbls.cpp',
  common_src_dir + 'gmed_n.cpp',
  common_src_dir + 'gray_tbl.cpp',
  common_src_dir + 'grid_tbl.cpp',
  common_src_dir + 'int_lpc.cpp',
  common_src_dir + 'inv_sqrt.cpp',
  common_src_dir + 'inv_sqrt_tbl.cpp',
  common_src_dir + 'l_deposit_h.cpp',
  common_src_dir + 'l_deposit_l.cpp',
  common_src_dir + 'log2.cpp',
  common_src_dir + 'log2_norm.cpp',
  common_src_dir + 'log2_tbl.cpp',
  common_src_dir + 'lsfwt.cpp',
  common_src_dir + 'l_shr_r.cpp',
  common_src_dir + 'lsp_az.cpp',
  common_src_dir + 'lsp.cpp',
  common_src_dir + 'lsp_lsf.cpp',
  common_src_dir + 'lsp_lsf_tbl.cpp',
  common_src_dir + 'lsp_tab.cpp',
  common_src_dir + 'mult_r.cpp',
  common_src_dir + 'negate.cpp',
  common_src_dir + 'norm_l.cpp',
  common_src_dir + 'norm_s.cpp',
  common_src_dir + 'overflow_tbl.cpp',
  common_src_dir + 'ph_disp_tab.cpp',
  common_src_dir + 'pow2.cpp',
  common_src_dir + 'pow2_tbl.cpp',
  common_src_dir + 'pred_lt.cpp',
  common_src_dir + 'q_plsf_3.cpp',
  common_src_dir + 'q_plsf_3_tbl.cpp',
  common_src_dir + 'q_plsf_5.cpp',
  common_src_dir + 'q_plsf_5_tbl.cpp',
  common_src_dir + 'q_plsf.cpp',
  common_src_dir + 'qua_gain_tbl.cpp',
  common_src_dir + 'reorder.cpp',
  common_src_dir + 'residu.cpp',
  common_src_dir + 'round.cpp',
  common_src_dir + 'set_zero.cpp',
  common_src_dir + 'shr.cpp',
  common_src_dir + 'shr_r.cpp',
  common_src_dir + 'sqrt_l.cpp',
  common_src_dir + 'sqrt_l_tbl.cpp',
  common_src_dir + 'sub.cpp',
  common_src_dir + 'syn_filt.cpp',
  common_src_dir + 'weight_a.cpp',
  common_src_dir + 'window_tab.cpp',
])

amrnb_link_args = cxx.get_supported_link_arguments(
  '-Wl,--version-script,@0@/libopencore-amrnb.map'.format(meson.current_source_dir()),
)

libopencore_amrnb = library('opencore-amrnb',
  opencore_amrnb_sources,
  cpp_args: [amr_lib_args, amrnb_args],
  include_directories: [oscl_incs, amrnb_incs],
  link_args: amrnb_link_args,
  link_language: amr_lib_link_language,
  version: libversion,
  vs_module_defs: 'opencore-amrnb.def',
  install: true)

pkg = import('pkgconfig')
pkg.generate(libopencore_amrnb,
  filebase: 'opencore-amrnb',
  subdirs: 'opencore-amrnb',
  name: 'OpenCORE AMR-NB',
  description: 'Adaptive Multi-Rate speech codec library')

opencore_amrnb_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: libopencore_amrnb,
)
