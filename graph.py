#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import sys
import select
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def datafeed(delta=10):
    last_draw = 0
    xdata = []
    ydata = []
    
    while True:
        i, o, e = select.select([sys.stdin], [], [], 1)
            
        if i:
            line = sys.stdin.readline()
            if line:
                line = line
                sys.stdout.write(line)
                data = [float(a.strip()) for a in line.strip().split(",")]
                xdata.append(data[0])
                ydata.append(data[1:])

                if time.time() - last_draw > delta:
                    last_draw = time.time()
                    yield xdata, ydata
            else:
                yield xdata, ydata
                break

def main():
    line = sys.stdin.readline()
    sys.stdout.write(line)

    headers = [a.strip() for a in line.strip().split(",")]

    fig, ax = plt.subplots()
    ax.set_xlabel(headers[0])
    

    for xdata, ydata in datafeed():
        plt.cla()
        plt.plot(xdata, ydata)
        plt.legend(labels=headers[1:])
        plt.xlabel(headers[0])
        plt.show(block=False)
    plt.show()

if __name__ == "__main__":
    main()
