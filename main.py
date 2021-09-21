# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def twoNumsAvg(a,b):
    return((a+b)/2)

def test_twoNumbsAvg():
    x=twoNumsAvg(2.0,8.0)
    assert(x==5.0)

def run_all_tests():
    test_twoNumbsAvg()

def main():
    run_all_tests()