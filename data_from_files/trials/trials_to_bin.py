import statistics
import struct

from timer import timer
from trials.get_trials_import import get_trial_import

with open('trials_1000000x10.bin', 'wb') as file:

    for idx, t in enumerate(get_trial_import(1000000, 10)):
        for number in t[3]:
            file.write(number.to_bytes(8, byteorder='big', signed=False))

