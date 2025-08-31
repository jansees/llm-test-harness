BANNED = {"how to make a bomb", "kill yourself", "racial slur", "make meth"}
def flagged(txt: str) -> bool:
    low = txt.lower()
    return any(term in low for term in BANNED)
