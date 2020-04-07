from timer import timer


with timer("3. import 1000000 x 100 from same file"):
    from trials.t_1000000.trials_100 import trials
    for t in trials:
        a = t[0]
print()
print("DONE")
