#!/usr/bin/env python3
#
# Run LTC encoder/decoder, capture decoder output and check against expected output
from __future__ import annotations
from argparse import ArgumentParser
import subprocess

if __name__ == '__main__':
    parser = ArgumentParser(description='Run LTC encoder/decoder, capturing the output and checking the diff')
    parser.add_argument('--encoder', type=str, help='Path to encoder executable')
    parser.add_argument('--encoder-rate', type=int, help='Sample rate to pass to encoder')
    parser.add_argument('--decoder', type=str, required=True, help='Path to decoder executable')
    parser.add_argument('--decoder-audio-frames-per-video-frame', type=str, help='Audio frames per video frame to pass to decoder')
    parser.add_argument('filename', type=str, help='Filename to write raw data to and/or read raw data from')
    parser.add_argument('expected_output', type=str, help='Path to text file containing the expected decoder output')

    args = parser.parse_args()

    if args.encoder:
        encoder_cmd = [args.encoder, args.filename]
        if args.encoder_rate:
            encoder_cmd += [f'{args.encoder_rate}']

        print(f'Running command {encoder_cmd}') 
        subprocess.run(encoder_cmd, check=True)
    
    decoder_cmd = [args.decoder, args.filename]
    if args.decoder_audio_frames_per_video_frame:
        decoder_cmd += [f'{args.decoder_audio_frames_per_video_frame}']

    print(f'Running command {decoder_cmd}')
    run_result = subprocess.run(decoder_cmd, check=True, capture_output=True)

    output = run_result.stdout.decode('utf-8').strip()
    output = output.replace('\r\n', '\n')
    print(f'\n--- stdout ---\n{output}\n--------------')

    errput = run_result.stderr.decode('utf-8').strip()
    print(f'\n--- stderr ---\n{errput}\n--------------')

    expected_output = ''.join(open(args.expected_output, 'r').readlines()).strip()
    print(f'\n--- Expected output ---\n{expected_output}\n--------------')

    if output != expected_output:
        raise Exception('Decoder output does not match expected output!')
