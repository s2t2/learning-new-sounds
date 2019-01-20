
import pdb


import sounddevice as sd

devices = sd.query_devices() #> <class 'sounddevice.DeviceList'>
for device in devices:
    print("\n", device)




#fps = 44100 # frames per second (in the most cases this will be 44100 or 48000)
#ds = 10.5  # duration in seconds
#
#recording = sd.rec(int(ds * fps), samplerate=fps, channels=2) # blocking=True
