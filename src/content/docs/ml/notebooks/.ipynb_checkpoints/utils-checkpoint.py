# checking Utils
import pickle
import os

def load_ans():
    if not os.path.isfile("answers"):
        raise Exception("Answer file not present!")
    with open("answers", "rb") as f:
        return pickle.load(f)


def setup_check():
    answers = load_ans()
    
    def check(q, ans):
        assert pickle.loads(answers[q]) == ans
    
    return check