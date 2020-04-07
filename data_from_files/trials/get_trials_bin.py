import os

import struct


def get_trial_bin(trial_size, num_trials):
    trials_returned = 0
    file_index = 0
    while trials_returned < num_trials:

        with open(os.path.join('trials','t_'+str(trial_size)+"bin", "trials"+str(file_index)+".bin"), 'rb') as file:
            data = file.read()
            instruct = "Q" * ((len(data) ) // 8)
            arr = struct.unpack("!"+instruct , data)
            arr_idx = 0
            while trials_returned < num_trials and arr_idx < len(arr):
                yield arr[arr_idx]
                arr_idx += 1
                trials_returned += 1
        file_index += 1


def get_trial_bin_iter(trial_size, num_trials):
    trials_returned = 0
    file_index = 0
    while trials_returned < num_trials:

        with open(os.path.join('trials','t_'+str(trial_size)+"bin", "trials"+str(file_index)+".bin"), 'rb') as file:
            data = file.read()
            # instruct = "Q" * ((len(data) ) // 8)
            arr_iter = struct.iter_unpack("!Q" , data)
            for a in arr_iter:
                if trials_returned >= num_trials:
                    break
                yield a[0]
                trials_returned += 1
        file_index += 1
