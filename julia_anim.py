#!/usr/bin/env python
# -'''- coding: utf-8 -'''-

import glob
import os
import imageio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse
import time
import calendar

class JuliaFrame():
    def __init__(self, c):
        self.c = c
        self.prisoners = []
        self.xmin = -1.5
        self.xmax =  1.5
        self.ymin = -1.5
        self.ymax =  1.5

    def findPrisoners(self, z):
        iterations = 200
        r = max(abs(self.c), 2.0)
        iz = z
        for i in range(iterations):
            if abs(iz) > r:
                return
            iz = (iz**2) + self.c
        self.prisoners.append(z)

    def save(self, filename="", fgColor="#ffffff", bgColor="#000000"):
        if len(filename) == 0:
            filename = "ja_" + str(c)

        fig = plt.figure()

        rect = [0.07, 0.07, 0.9, 0.9]
        ax = fig.add_axes([0.07, 0.07, 0.9, 0.85])
        ax.set_title(str(c))
        ax.set_xlim([self.xmin, self.xmax])
        ax.set_ylim([self.ymin, self.ymax])
        ax.set_facecolor(bgColor)

        for p in self.prisoners:
            plt.plot(p.real, p.imag, color=fgColor, marker=",")

        fig.savefig(filename)
        plt.close(fig)
        
if __name__ == "__main__":
    ts = str(calendar.timegm(time.gmtime()))

    argParser = argparse.ArgumentParser()
    argParser.add_argument('-sr', help="start real", type=float, default=0.0)
    argParser.add_argument('-si', help="start imag", type=float, default=0.0)
    argParser.add_argument('-er', help="end real", type=float, default=-0.391)
    argParser.add_argument('-ei', help="end imag", type=float, default=-0.587)

    argParser.add_argument('-frames', help="number of frames", type=int, default=60)
    argParser.add_argument('-spacesize', help="pixels in each dimension", type=int, default=64)

    argParser.add_argument('-fg', help="color of prisoner points", default="#ffffff")
    argParser.add_argument('-bg', help="color of the complex plane", default="#000000")

    argParser.add_argument('-rev', help="reverse animation (doubles frames in output gif)", action="store_true")
    argParser.add_argument('-o', help="filename", default="ja-" + ts + ".gif")

    pargs = argParser.parse_args()

    imagesDir = "ja-" + ts
    if not os.path.exists(imagesDir):
        os.mkdir(imagesDir)

    start = complex(pargs.sr, pargs.si)
    end   = complex(pargs.er, pargs.ei)

    cs = np.linspace(start, end, pargs.frames)
    for i in range(pargs.frames):
        c = cs[i] 
        jf = JuliaFrame(c)
        for imagg in np.linspace(-2.0, 2.0, pargs.spacesize):
            for reall in np.linspace(-2.0, 2.0, pargs.spacesize):
                jf.findPrisoners(complex(reall, imagg))

        jf.save(filename=imagesDir + "/ja_" + str(i) + ".png", bgColor=pargs.bg, fgColor=pargs.fg)

    filenames = glob.glob(imagesDir + "/*.png") 
    list.sort(filenames, key=lambda x: int(x.split('_')[1].strip('.png'))) 

    images = []

    for filename in filenames:
        images.append(imageio.imread(filename))

    if pargs.rev:
        list.sort(filenames, key=lambda x: int(x.split('_')[1].strip('.png')), reverse=True) 
        for filename in filenames:
            images.append(imageio.imread(filename))

    imageio.mimsave(imagesDir + "/" + pargs.o, images, fps=30)
