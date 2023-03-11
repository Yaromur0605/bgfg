import random
class cat():
    def __init__(self, chill):
        self.chill = chill
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
    def result(self):

     if self.chill <= 4:
         print("cat become lazy")
     elif self.chill == -5:
         print("cat not become lazy")





