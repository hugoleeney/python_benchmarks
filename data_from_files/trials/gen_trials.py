import numpy

from trials.inc_dec import gen_pos_numbers_inc_dec



def get_trials(trial_size, num_trials):
    for i in range(num_trials):
        trial = numpy.array(gen_pos_numbers_inc_dec(trial_size, up_chance=0.5))
        yield (min(trial), numpy.mean(trial), numpy.std(trial), trial)


def gen_trials_bin(size_trial, num_trials, directory, filename, numfiles):

    for ifile in range(numfiles):
        file_and_path = os.path.join(directory, filename+str(ifile)+".bin")
        print("directory=%s file=%s"%(directory, filename))

        with open(file_and_path, 'wb') as outfile:
            trials0 = [gen_pos_numbers_inc_dec(size_trial, up_chance=0.5) for i in range(num_trials)]
            trials = [[min(trial), numpy.mean(trial), numpy.std(trial), trial] for trial in trials0]

            for t in trials:
                for number in t[3]:
                    outfile.write(number.to_bytes(8, byteorder='big', signed=False))


def gen_trials_py(size_trial, num_trials, directory, file, numfiles):

    for ifile in range(numfiles):
        file_and_path = os.path.join(directory, file+str(ifile)+".py")
        print("directory=%s file=%s"%(directory, file))
        with open(file_and_path, 'w') as outfile:
            trials0 = [gen_pos_numbers_inc_dec(size_trial, up_chance=0.5) for i in range(num_trials)]
            trials = [[min(trial), numpy.mean(trial), numpy.std(trial), trial] for trial in trials0]

            print("''' trials = [gen_pos_numbers_inc_dec(%s, up_chance=0.5) for i in range(%s)] '''"%(size_trial, num_trials), file=outfile)
            print("trials = [", file=outfile)
            for idx, t in enumerate(trials):
                if idx != len(trials)-1:
                    print(t,',', file=outfile)
                else:
                    print(t, file=outfile)
            print("]", file=outfile)

def gen_trials_py_split(size_trial, num_trials, directory, file, numfiles):

    for ifile in range(numfiles):
        with open(os.path.join(directory, file+str(ifile)+".py"), 'w') as outfile:
            trials0 = [gen_pos_numbers_inc_dec(size_trial, up_chance=0.5) for i in range(num_trials)]
            trials = [[min(trial), numpy.mean(trial), numpy.std(trial), trial] for trial in trials0]

            print("''' trials = [gen_pos_numbers_inc_dec(%s, up_chance=0.5) for i in range(%s)] '''"%(size_trial, num_trials), file=outfile)
            for idx, t in enumerate(trials):
                print("trial"+str(idx)+" = ", end='', file=outfile)
                print(t, file=outfile)
            print('trials = [', end='', file=outfile)
            for idx, t in enumerate(trials):
                print("trial"+str(idx)+", ", end='', file=outfile)
            print(']', file=outfile)


def gen_trials_json(size_trial, num_trials, directory, file, numfiles):

    for ifile in range(numfiles):
        with open(os.path.join(directory, file+str(ifile)+".json"), 'w') as outfile:
            trials0 = [gen_pos_numbers_inc_dec(size_trial, up_chance=0.5) for i in range(num_trials)]
            trials = [[min(trial), numpy.mean(trial), numpy.std(trial), trial] for trial in trials0]

            print("[", file=outfile)
            for idx, t in enumerate(trials):
                if idx != len(trials)-1:
                    print(t,',', file=outfile)
                else:
                    print(t, file=outfile)
            print("]", file=outfile)

import os
def gen_trials_json_slow(size_trial, num_trials, directory, file, numfiles):

    for ifile in range(numfiles):
        with open(os.path.join(directory, file+str(ifile)+".json"), 'w') as outfile:
            print("[", file=outfile)
            for i in range(num_trials):
                t = numpy.array(gen_pos_numbers_inc_dec(size_trial, up_chance=0.5))
                t = [min(t), numpy.mean(t), numpy.std(t), list(t)]
                if i != num_trials-1:
                    print(str(t)+',', file=outfile)
                else:
                    print(str(t), file=outfile)
            print("]", file=outfile)


if __name__ == "__main__":

    numpy.set_printoptions(threshold=numpy.inf)
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("type")
    parser.add_argument("size", type=int)
    parser.add_argument("num", type=int)
    parser.add_argument("dir")
    parser.add_argument("file")
    parser.add_argument("numfiles", type=int)
    args = parser.parse_args()
    if args.type == "json":
        gen_trials_json(args.size, args.num, args.dir, args.file, args.numfiles)
    if args.type == "json_slow":
        gen_trials_json_slow(args.size, args.num, args.dir, args.file, args.numfiles)
    elif args.type == "py":
        gen_trials_py(args.size, args.num, args.dir, args.file, args.numfiles)
    elif args.type == "py_split":
        gen_trials_py_split(args.size, args.num, args.dir, args.file, args.numfiles)
    elif args.type == "bin":
        gen_trials_bin(args.size, args.num, args.dir, args.file, args.numfiles)

    else:
        raise Exception()

