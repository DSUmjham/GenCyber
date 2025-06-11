import numpy as np                        # Import NumPy for numerical operations
import scipy.io.wavfile as wav            # Import wavfile module for reading/writing WAV files
from scipy.signal import resample         # Import resample for resampling audio
import argparse                           # Import argparse for command-line argument parsing
import subprocess                         # Import subprocess for running external commands

# Morse code dictionary mapping each character to dots and dashes
MORSE_CODE_DICT = {
	'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
	'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
	'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
	'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
	'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
	'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
	'Y': '-.--',  'Z': '--..',
	'0': '-----', '1': '.----', '2': '..---', '3': '...--',
	'4': '....-', '5': '.....', '6': '-....', '7': '--...',
	'8': '---..', '9': '----.',
	' ': '/'
}

def text_to_morse(text):
	# Convert input text to Morse code string using dictionary above
	return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def generate_tone(duration, sample_rate, freq, amplitude):
	# Generate a sine wave tone of specified duration, frequency, and amplitude
	t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False) 
	wave = amplitude * np.sin(2 * np.pi * freq * t)	# Sine wave formula
	return wave.astype(np.int16)					# Return as int16 for WAV

def generate_silence(duration, sample_rate):
	# Generate an array of zeros (silence) for the specified duration
	return np.zeros(int(sample_rate * duration), dtype=np.int16)

def morse_to_audio(morse_code, sample_rate, freq, dot, dash, symbol_space, letter_space, word_space, amplitude):
	# Convert Morse code string to audio waveform array
	audio = []																# List to store audio samples
	for symbol in morse_code:												# Loop through each symbol
		if symbol == '.':
			audio.extend(generate_tone(dot, sample_rate, freq, amplitude))	# Dot: short tone
			audio.extend(generate_silence(symbol_space, sample_rate))		# Followed by short silence
		elif symbol == '-':
			audio.extend(generate_tone(dash, sample_rate, freq, amplitude))	# Dash: long tone
			audio.extend(generate_silence(symbol_space, sample_rate))		# Followed by short silence
		elif symbol == ' ':
			audio.extend(generate_silence(letter_space, sample_rate))		# Space between letters
		elif symbol == '/':
			audio.extend(generate_silence(word_space, sample_rate))			# Space between words
	return np.array(audio, dtype=np.int16)									# Return as NumPy array

def write_wavefile(filename, audio_data, sample_rate):
	# Write audio data to a WAV file with the given sample rate
	wav.write(filename, sample_rate, audio_data)

def fm_modulate(audio, wav_rate, tx_rate, deviation, iq_out):
	# FM modulate an audio array and save the result as unsigned 8-bit I/Q for HackRF
	audio = audio.astype(np.float32)												# Ensure floating point for processing
	audio -= np.mean(audio)															# Remove DC offset
	audio /= np.max(np.abs(audio))													# Normalize to [-1, 1]
	duration_sec = len(audio) / wav_rate											# Calculate duration in seconds
	num_output_samples = int(duration_sec * tx_rate)								# Total number of I/Q samples to generate
	audio_resampled = resample(audio, num_output_samples)							# Resample audio to HackRF sample rate
	dt = 1.0 / tx_rate																# Sample period for HackRF
	kf = 2 * np.pi * deviation														# FM sensitivity (radians per unit amplitude)
	audio_integral = np.cumsum(audio_resampled) * dt								# Integrate audio for phase calculation
	phase = kf * audio_integral														# Calculate instantaneous phase
	fm_signal = np.exp(1j * phase).astype(np.complex64)								# Create complex FM baseband
	fm_signal /= np.max(np.abs(fm_signal))											# Normalize FM signal amplitude
	iq_i = np.clip((np.real(fm_signal) * 127.5 + 127.5), 0, 255).astype(np.uint8)	# Convert I to unsigned 8-bit
	iq_q = np.clip((np.imag(fm_signal) * 127.5 + 127.5), 0, 255).astype(np.uint8)	# Convert Q to unsigned 8-bit
	iq_interleaved = np.empty(iq_i.size + iq_q.size, dtype=np.uint8)				# Create array for interleaved I/Q
	iq_interleaved[0::2] = iq_i														# Place I in even indices
	iq_interleaved[1::2] = iq_q														# Place Q in odd indices
	with open(iq_out, "wb") as f:
		f.write(iq_interleaved)														# Write interleaved I/Q to file
	print(f"[+] IQ file saved as {iq_out}")

def transmit(iq_file, freq, tx_rate, gain=47):
	# Run hackrf_transfer with the specified parameters to transmit the IQ file
	cmd = [
		"hackrf_transfer",
		"-t", iq_file,
		"-f", str(freq),
		"-s", str(tx_rate),
		"-x", str(gain),
		"-a", "1",
		"-R"
	]
	print(f"[*] Transmitting with: {' '.join(cmd)}")
	subprocess.run(cmd)                                           # Call HackRF transfer

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Generate Morse code audio and HackRF IQ file from text.")
	parser.add_argument("--text", required=True, help="Text to send as Morse code")
	parser.add_argument("--wav", default="morse_message.wav", help="Preview audio output WAV file")
	parser.add_argument("--iq", default="fm_output_8bit.iq", help="Output IQ file for HackRF")
	parser.add_argument("--wav_rate", type=int, default=44100, help="WAV sample rate (Hz)")
	parser.add_argument("--freq", type=int, default=100500000, help="Transmit frequency (Hz)")
	parser.add_argument("--tx_rate", type=int, default=2000000, help="IQ/HackRF sample rate (Hz)")
	parser.add_argument("--deviation", type=float, default=5000, help="FM deviation (Hz)")
	parser.add_argument("--morse_freq", type=float, default=600, help="Morse tone frequency (Hz)")
	parser.add_argument("--dot", type=float, default=0.1, help="Dot duration (s)")
	parser.add_argument("--amplitude", type=int, default=32767, help="Tone amplitude (WAV, int16)")
	parser.add_argument("--send", action="store_true", help="Transmit automatically with hackrf_transfer")
	parser.add_argument("--gain", type=int, default=47, help="HackRF TX gain (default 47)")

	args = parser.parse_args()

	# Morse timing parameters
	DASH = args.dot * 3
	SYMBOL_SPACE = args.dot
	LETTER_SPACE = args.dot * 3
	WORD_SPACE = args.dot * 7

	print(f"[*] Encoding text: '{args.text}'")
	morse = text_to_morse(args.text)
	print(f"[+] Morse: {morse}")

	# Generate Morse audio as int16
	audio_data = morse_to_audio(
		morse, args.wav_rate, args.morse_freq, args.dot, DASH,
		SYMBOL_SPACE, LETTER_SPACE, WORD_SPACE, args.amplitude
	)
	# Write preview WAV file
	write_wavefile(args.wav, audio_data, args.wav_rate)
	print(f"[+] Preview WAV saved as {args.wav}")

	# FM modulate and save IQ file
	fm_modulate(audio_data, args.wav_rate, args.tx_rate, args.deviation, args.iq)

	# If --send is given, call hackrf_transfer to transmit
	if args.send:
		transmit(args.iq, args.freq, args.tx_rate, gain=args.gain)

	print("[✓] All done!")