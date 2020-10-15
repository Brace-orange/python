import time
import threading

def sing():
    for i in range(4):
        print("changge----%d" %i)
        time.sleep(1)


def eat():
    print("chifan")
    time.sleep(2)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=eat)
    t1.start()
    t2.start()
    # sing()
    # eat()

if __name__ == "__main__":
    main()
