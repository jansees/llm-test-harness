import difflib

def exact(pred, ref): return pred.strip() == ref.strip()
def ratio(pred, ref): return difflib.SequenceMatcher(None, pred.strip(), ref.strip()).ratio()
def functional_pass(pred, ref, min_ratio=0.7): return exact(pred, ref) or ratio(pred, ref) >= min_ratio

'''(Add python-levenshtein to switch scoring.py to use it, but the current code uses Python’s built-in difflib.)'''