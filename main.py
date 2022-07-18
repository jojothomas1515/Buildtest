import timeit

def timeer():
    for i in range(1000000):
        print("thank you")

if __name__ == '__main__':
    start = timeit.timeit()
    timeer()
    end = timeit.timeit()
    print(end-start)

