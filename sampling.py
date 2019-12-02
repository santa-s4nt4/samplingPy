import pyaudio
import wave

'''
iAudio = pyaudio.PyAudio()
for x in range(0, iAudio.get_device_count()): 
    print(iAudio.get_device_info_by_index(x))
'''

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'sample.wav'
iDeviceIndex = 1

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2 ** 11
audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    input_device_index=iDeviceIndex,
                    frames_per_buffer=CHUNK)

input('Press Any key to record for 5 seconds. Please tell me your name.')
print('Recording...')
frames = []
for i in range(1, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print('Finished recording!')

stream.stop_stream()
stream.close()
audio.terminate()
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
