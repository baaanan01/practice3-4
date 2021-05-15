import random
from itertools import count
import numpy as np

class Monte_Karlo():
    stpcnt = 100000000
    def calc(self, pntsm=10000, seed=0):
        pntsm = int(pntsm)
        random.seed(seed)
        in_circle = 0
        i = pntsm if pntsm <= Monte_Karlo.stpcnt else Monte_Karlo.stpcnt
        while i >= 0:
            x = random.random()
            y = random.random()
            if x ** 2 + y ** 2 <= 1:
                in_circle += 1
            i -= 1
        pi = 4 * in_circle / pntsm
        print('pi = {:.8f}. Total points = {} points within = {}'.format(pi, pntsm, in_circle))

    def calc_compare(self, start=10000, mul=10, stop=5):
        start = int(start)
        mul = int(mul)
        stop = int(stop)
        counts = count(1)
        for iter in counts:
            if iter > stop:
                break
            print('iter: {}'.format(iter))
            self.calc(start * mul ** iter)

    def calc_with_np(self, pntsm=10000, seed=0):
        pntsm = int(pntsm)
        pntsm = pntsm if pntsm <= Monte_Karlo.stpcnt else Monte_Karlo.stpcnt
        np.random.seed(seed)
        x_arr = np.random.random(pntsm)
        y_arr = np.random.random(pntsm)
        sq = np.add(x_arr ** 2, y_arr ** 2)
        in_circle = sq[sq <= 1]
        pi = 4 * in_circle.shape[0] / pntsm
        print('pi = {:.8f}. Total points = {} points within = {}'.format(pi, pntsm, in_circle.shape[0]))

    def calc_compare_with_np(self, start=10000, mul=10, stop=5):
        start = int(start)
        mul = int(mul)
        stop = int(stop)
        counts = count(1)
        for iter in counts:
            if iter > stop:
                break
            print('iter: {}'.format(iter))
            self.calc_with_np(start * mul ** iter)