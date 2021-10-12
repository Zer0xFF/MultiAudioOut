from AudioDevice import AudioDevice
import pyaudio
import time

print('Finding Audio Output Devices')

output_devices = []
output_devices.append(AudioDevice(output=True, output_device_index=AudioDevice.get_device_index("PL2760Q (NVIDIA High Definition Audio)")))
output_devices.append(AudioDevice(output=True, output_device_index=AudioDevice.get_device_index("PL2730H (NVIDIA High Definition Audio)")))

print(f'Found ({len(output_devices)}) Output Device(s)')

time_lag = 0
def callback(in_data, frame_count, time_info, flag):
    global time_lag
    time_lag += (time_info['current_time'] - time_info['input_buffer_adc_time'])
    for output in output_devices:
        output.Write(in_data)
    return (in_data, pyaudio.paContinue)

print('Streaming')

speaker = AudioDevice(input_device_index=AudioDevice.get_device_index("Stereo Mix (Realtek High Definition Audio)"), input=True, stream_callback=callback)

try:
    while speaker.is_alive():
        time.sleep(1)
        print(f"A/V delay: {time_lag: 0.2f} seconds", " " * 10, end='\r')
        time_lag = 0
except KeyboardInterrupt:
    pass

print('\nFinished Streaming')
