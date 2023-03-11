import random
class cat():
    def __init__(self, name, chill):
        self.chill = chill
        self.name = name
    def sleep(self):
        print("cat sleep")
        self.chill += 1

    def jump(self):
        print("cat jumping")
        self.chill -= 0.5
    def chill(self):
        print("cat chill")
        self.chill += 2
    def run(self):
        print("cat runing")
        self.chill -= 1




