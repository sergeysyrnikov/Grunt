from MainPanelGrunt import Slider
import threading
import time
import globalValues

def start_my():
    while True:
        Slider.value += 1


if __name__ == '__main__':
    th1 = threading.Thread(target=start_my)
    th1.start()
    start_time = time.time()
    while True:
        print(Slider.value)

        if ((time.time() - start_time) > 3):
            break
    obj = Slider()
    print('Value: ', obj.value)

    qwer = obj.value

