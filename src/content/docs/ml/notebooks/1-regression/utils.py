# checking Utils
import pickle
import os


def load_ans():
    if not os.path.isfile("data/answers"):
        raise Exception("Answer file not present!")
    with open("data/answers", "rb") as f:
        return pickle.load(f)


def setup_check():
    answers = load_ans()

    def check(q, ans):
        correct = pickle.loads(answers[q])
        print(correct)
        assert correct == ans

    return check
