#The Halting Problem
#Essentially, the Halting Problem is a problem, asking if a program will stop running, or run forever, given an input.
#Its undecidable, because there is no algorithm that generalizes all possible solutions to this problem, given different cases.
def halts(f, x):
    # Attempt to determine if function f halts on input x
    try:
        f(x)
        return True  # f halts
    except RecursionError:
        return False  # f runs forever

def loop_forever(x):
    # A function that loops forever
    while True:
        pass

def halts_example():
    # Test the halts function
    print(halts(loop_forever, 0))  # Should print False

halts_example()
