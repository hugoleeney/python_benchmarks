
from timer import timer


# 12 secs
with timer('open trials_1000000x10.bin'):
    with open('trials/t_1000000bin/trials0.bin', 'rb') as file:
        for i in range(10000000):
            j = int.from_bytes(file.read(8), byteorder='big')
