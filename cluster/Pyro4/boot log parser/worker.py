from __future__ import print_function
import Pyro4

class Log(object):
    def __init__(self):
        self.sentence = {}

    def list_contents(self):
        return self.sentence

    def hitung(self, cek):
        print(cek)

        if (cek in self.sentence):
            self.sentence[cek] += 1
        else:
            self.sentence[cek] = 1

    def setor(self):
        return self.urut()

    def urut(self):
        sort = sorted(self.sentence.items(), key=lambda x:x[1], reverse=True)
        return sort

def main():
    log = Log()
    daemon = Pyro4.Daemon(host="danang")
    ns = Pyro4.naming.locateNS()
    uri = daemon.register(log)
    ns.register("log.satu", uri)
    print("Server ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()