# MultiAudioOut

Windows audio stack does allow you to target multiple audio out devices for audio playback,
This simple script uses "Stereo Mix" devices to records audio to replay into other devices.

## Requirements
 - OS: Windows (havent tested it on other OSs)
 - pipwin (required to install pyaudio on windows)
 - python3

## Setup
  - `pip3 install pipwin`
  - `pipwin install pyaudio`
  - edit main.py
    - line 23 to reflect audio mix device
    - lines 8-9 to reflect desired out devices
    - device names can be obtained using `python3 list.py`
 
 ## Run
  - run the python script `main.py`
    - `python3 main.py` 