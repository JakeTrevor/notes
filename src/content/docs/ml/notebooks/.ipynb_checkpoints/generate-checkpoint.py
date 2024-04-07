# This file generates the data files for this worksheet

import random
import pickle
import numpy as np

seed = 10
random.seed(seed)
np.random.seed(seed)

answers = {}

def data1():
    m = random.randint(0, 5)
    c = random.randint(0, 50)
    answers["m1"] = m
    answers["c1"] = c

    def fn(x):
        return m * x + c
        
    samples = np.random.randint(0, 100, [20])
    with open("data1.csv", "w") as f:
        f.write("x,y\n")
        for x in samples:
            f.write(f"{x},{fn(x)}\n")


def data2(): 
    m = random.randint(0, 5)
    c = random.randint(0, 50)
    answers["m2"] = m
    answers["c2"] = c

    def fn(x):
        noise = random.randint(0, 20)
        return m * x + c + noise
        
    samples = np.random.randint(0, 100, [40])
    with open("data2.csv", "w") as f:
        f.write("x,y\n")
        for x in samples:
            f.write(f"{x},{fn(x)}\n")

def make_answers():
    hidden = {key:pickle.dumps(ans) for key,ans in answers.items()}
    
    with open("answers", "wb") as f:
        pickle.dump(hidden, f)


data1()
data2()
make_answers()

