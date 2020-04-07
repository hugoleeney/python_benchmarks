import struct

from timer import timer


# 4.3
with timer('read 1000000 x 10 from binary'):
    ints_read = 0
    with open('trials/t_1000000bin/trials0.bin', 'rb') as file:
        data = file.read()
        instruct = "Q" * ((len(data) ) // 8)
        d = struct.unpack("!"+instruct , data)
        iss = 0
        for i in d:
            iss += 1
