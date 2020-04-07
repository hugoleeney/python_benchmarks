import importlib


def get_trial_import_1(trial_size, num_trials):
    from huog.trials.t_1000000x1.trials0 import trials

    trials_returned = 0
    while trials_returned < num_trials:
        yield trials[trials_returned]
        trials_returned += 1


def get_trial_import(trial_size, num_trials):
    trials_returned = 0
    file_index = 0
    trial_package = 't_'+str(trial_size)
    while trials_returned < num_trials:
        s2 = "".join([trial_package,'.trials%s'%file_index])
        arr = importlib.import_module('.%s' % (s2), package='trials').trials
        arr_idx = 0
        while trials_returned < num_trials and arr_idx < len(arr):
            yield arr[arr_idx]
            arr_idx += 1
            trials_returned += 1
        file_index += 1


def get_trial_import_inc(trial_size, num_trials):
    trials_returned = 0
    file_index = 0
    trial_package = 't_'+str(trial_size)
    while trials_returned < num_trials:
        filename = 'trials%s'%file_index
        arr = importlib.import_module('trials.%s.%s'%(trial_package,filename)).trials
        arr_idx = 0
        while trials_returned < num_trials and arr_idx < len(arr):
            yield arr[arr_idx]
            arr_idx += 1
            trials_returned += 1
        file_index += 1
