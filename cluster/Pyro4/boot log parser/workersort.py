from __future__ import print_function
import Pyro4

class sortparse(object):
    def __init__(self):
        self.sentence = {}

    def sortkan(self, hasil1, hasil2):
        hasil2 = dict((x, y) for x, y in hasil2)
        for freq in hasil1:
            if freq[0] in hasil2:
                hasil2[freq[0]] = hasil2[freq[0]] + freq[1]
            else:
                hasil2[freq[0]] = freq[1]

        hasil2 = sorted(hasil2.items(), key=lambda x: x[1], reverse=True)
        print(hasil2)
        return hasil2

def main():
    prosessort = sortparse()
    daemon = Pyro4.Daemon(host="danang")
    ns = Pyro4.naming.locateNS()
    uri = daemon.register(prosessort)
    ns.register("log.sort", uri)
    print("Server ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()