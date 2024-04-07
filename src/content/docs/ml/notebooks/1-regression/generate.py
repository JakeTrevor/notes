# This file generates the data files for this worksheet

import random
import pickle
import numpy as np
import os.path as path
import os


seed = 20
random.seed(seed)
np.random.seed(seed)

answers = {}


def p(leaf):
    BASE_DIR = path.dirname(path.abspath(__file__))
    return path.join(BASE_DIR, leaf)


def setup():
    data_dir = p("data")
    if not path.exists(data_dir):
        os.makedirs(data_dir)


def loss(xs, ys, model):
    # as a nice one-liner
    return sum([(y - model(x)) ** 2 for (x, y) in zip(xs, ys)]) / len(xs)


def data1():
    m = random.randint(0, 5)
    c = random.randint(0, 50)
    answers["m1"] = m
    answers["c1"] = c

    def fn(x):
        return m * x + c

    samples = np.random.randint(0, 100, [20])
    with open(p("./data/data1.csv"), "w+") as f:
        f.write("x,y\n")
        for x in samples:
            f.write(f"{x},{fn(x)}\n")


# implement your model for theory 1
def model1(x: int) -> int:
    return 2 * x + 20


# implement your model for theory 2
def model2(x: int) -> int:
    return 5 * x + 9


def data2():
    m = random.randint(0, 5)
    c = random.randint(0, 50)
    answers["m2"] = m
    answers["c2"] = c

    def fn(x):
        noise = random.randint(0, 20)
        return m * x + c + noise

    xs = np.random.randint(0, 100, [40])

    ys = [fn(x) for x in xs]

    with open(p("./data/data2.csv"), "w+") as f:
        f.write("x,y\n")
        for x, y in zip(xs, ys):
            f.write(f"{x},{y}\n")

    answers["loss1"] = loss(xs, ys, model1)
    answers["loss2"] = loss(xs, ys, model2)


def make_answers(answers):
    hidden = {key: pickle.dumps(ans) for key, ans in answers.items()}

    with open(p("./data/answers"), "wb+") as f:
        pickle.dump(hidden, f)


setup()
data1()
data2()
make_answers(answers)
