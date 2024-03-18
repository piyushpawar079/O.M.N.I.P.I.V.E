import sounddevice as sd
import numpy as np

from OMNIPIVE.Functions.input_output_functions import say

threshold = 10
Clap = False


def detect_clap(indata, frames, time, status):
    global Clap
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        say('clap detected sir.')
        Clap = True


def Listen_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)


def MainClapExe():
    while True:
        global Clap
        Listen_for_claps()
        if Clap:
            Clap = False
            return True


if __name__ == '__main__':
    MainClapExe()

