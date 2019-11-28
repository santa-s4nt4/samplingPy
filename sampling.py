import pyaudio
import wave

RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = 'sample.wav'
iDeviceIndex = 0

FORMAT = pyaudio.pyInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2 ** 11
audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    input_device_index=iDeviceIndex,
                    frames_per_buffer=CHUNK)
