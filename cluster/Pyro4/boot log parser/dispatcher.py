# This is the code that visits the warehouse.
from __future__ import print_function
import sys
import os
import time

import Pyro4
import Pyro4.util

if sys.version_info < (3, 0):
    input = raw_input

sys.excepthook = Pyro4.util.excepthook

class Proses(object):
    def __init__(self):
        self.filenya = os.listdir("../filenya/.")
        self.list1 = self.filenya[((len(self.filenya)/2)):]
        self.list2 = self.filenya[:(len(self.filenya)/2)]

    def baca1(self, Log):
        for files in self.list1:
            print(files)
            for line in open("../filenya/"+files).xreadlines():
                cek = line.split()
                cek = " ".join(cek[4:])
                Log.hitung(cek)

    def baca2(self, Log):
        for files in self.list2:
            print(files)
            for line in open("../filenya/"+files).xreadlines():
                cek = line.split()
                cek = " ".join(cek[4:])
                Log.hitung(cek)

    def ambil(self, Log):
        return Log.setor()

def main():
    Log1 = Pyro4.Proxy("PYRONAME:log.satu")
    Log2 = Pyro4.Proxy("PYRONAME:log.dua")

    pro1 = Proses()
    pro2 = Proses()

    tstart = time.time()

    pro1.baca1(Log1)
    pro2.baca2(Log2)
    hasil1 = pro1.ambil(Log1)
    hasil2 = pro2.ambil(Log2)

    sortparse = Pyro4.Proxy("PYRONAME:log.sort")
    hasil = sortparse.sortkan(hasil1, hasil2)

    i = 0
    while i < 10:
        print(hasil[i])
        i = i + 1

    tend = time.time()
    print("Total elapsed time: %d msec" % ((tend-tstart)*1000))

if __name__=="__main__":
    main()

