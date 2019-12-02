import pyaudio
import wave
from pythonosc import osc_server
from pythonosc.dispatcher import Dispatcher

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


def twHandler(unsedAddr, osc):
    print(osc)
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        input_device_index=iDeviceIndex,
                        frames_per_buffer=CHUNK)

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


IP = '192.168.1.7'
PORT = 10000

dispatcher = Dispatcher()
dispatcher.map('/tw', twHandler)

server = osc_server.ThreadingOSCUDPServer((IP, PORT), dispatcher)
print(server.server_address)
server.serve_forever()
