# Introduction
[The hackrf-morse.py script](https://github.com/DSUmjham/GenCyber/blob/master/HackRF_Morse_Code/hackrf-morse.py) takes your input text, generates Morse code as both a WAV file for listening and an FM-modulated IQ file for over-the-air transmission with HackRF.



## Basic Usage
```bash
python morse_fm_cli.py --text "CQ TEST"
```

- Generates:
  - `morse_message.wav` (preview audio you can play)
  - `fm_output_8bit.iq` (for HackRF transmission)


## Transmitting Automatically
Add `--send` to directly transmit after generating the IQ file:

```bash
python morse_fm_cli.py --text "HELLO WORLD" --send
```

This will run `hackrf_transfer` and transmit your message over the air at the default frequency (100.5 MHz).

## Customizing Parameters

You can override the output filenames, transmit frequency, modulation settings, and more:

```bash
python morse_fm_cli.py \
  --text "THE QUICK BROWN FOX" \
  --wav preview.wav \
  --iq fox.iq \
  --freq 100700000 \
  --tx_rate 2000000 \
  --deviation 8000 \
  --morse_freq 700 \
  --dot 0.08 \
  --send
```

### Parameter Reference

| Argument       | Default             | Description                         |
| -------------- | ------------------- | ----------------------------------- |
| `--text`       | (required)          | The message to transmit in Morse    |
| `--wav`        | morse\_message.wav  | WAV preview filename                |
| `--iq`         | fm\_output\_8bit.iq | IQ file for HackRF transfer         |
| `--freq`       | 100500000           | Transmit frequency in Hz            |
| `--tx_rate`    | 2000000             | HackRF/IQ sample rate (Hz)          |
| `--deviation`  | 5000                | FM deviation (Hz)                   |
| `--morse_freq` | 600                 | Morse tone frequency (Hz)           |
| `--dot`        | 0.1                 | Dot duration (seconds)              |
| `--amplitude`  | 32767               | WAV tone amplitude (max=32767)      |
| `--send`       | (flag)              | If set, will transmit automatically |
| `--gain`       | 47                  | HackRF transmit gain (0–47)         |

## Listening to the Preview WAV

Play the preview file on your computer:

```bash
aplay morse_message.wav
```

Or open with your preferred audio player.

## Manual HackRF Transmission

If you generated only the `.iq` file, transmit later with:

```bash
hackrf_transfer -t fm_output_8bit.iq -f 100500000 -s 2000000 -x 47 -a 1 -R
```

## Receiving in GQRX
- Set frequency to match `--freq` (default 100.5 MHz)
- Mode: NFM (narrow FM), BW \~15 kHz, Squelch OFF, volume up