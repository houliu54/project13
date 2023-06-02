"""主运行程序"""
import os
import threading
import time

lock = threading.Lock()

project_path = os.path.dirname(__file__)


class Threads(threading.Thread):
    def __init__(self,position):
        super(Threads, self).__init__()
        self.position = position

    def run(self) -> None:
        print('这是第'+str(self.position)+'个')
        # 避免死锁，threading.lock()
        lock.acquire()
        # 直接使用命令行
        os.system('cd '+project_path)
        print(os.path.basename(__file__))
        os.system('pytest')
        lock.release()
        time.sleep(10)


if __name__ == '__main__':
    # 存放所有产生的进程
    threads = []

    for i in range(2):
        th = Threads(i)
        threads.append(th)
        th.start()
    # 所有进程执行完后，退出
    for t in threads:
        t.join()
        print('.....子进程结束....')

    print('子进程运行完成，主进程这是')