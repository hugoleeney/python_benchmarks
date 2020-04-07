from timer import timer
from trials.get_trials_bin import get_trial_bin


# 1s
with timer('read 1000000 x 10 from binary'):
    ints_read = 0
    for trial in get_trial_bin(1000000, 10):
        ints_read += 1
