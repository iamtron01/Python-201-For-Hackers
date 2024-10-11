def print_out(a):
    print("Outer: {}".format(a))
    def print_in():
        print("\tInner: {}".format(a))
    return print_in

f = print_out("test")
f()