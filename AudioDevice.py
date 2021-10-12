import pyaudio
import atexit

class AudioDevice(object):

    @staticmethod
    def get_device_index(name):
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count())[::-1]:
            if(p.get_device_info_by_index(i)['name'] == name):
                return i
        return

    def __init__(self, **kargs):
        atexit.register(self.cleanup)
        chunk = 1024
        sample_format = pyaudio.paInt32
        channels = 2
        fs = 48000

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                **kargs)

    def cleanup(self):
        if(self.stream):
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        if(self.p):
            self.p.terminate()
            self.p = None


    # Play
    def Write(self, data):
        self.stream.write(data)

    # Record
    def Read(self, data):
        self.stream.read(data)

    def is_alive(self):
        return self.stream and self.stream.is_active()

