class Character():
    def __init__(self, realname, heroname):
        self.name = realname
        self.hname = heroname

    def set_power(self,power):
        self.power = power

    def get_power(self):
        print(self.power)
    def get_name(self):
        print(self.name)
    def get_hname(self):
        print(self.hname)
    
    def get_stats(self):
        print(f"{self.name} is the hero known as {self.hname}. They have the power of {self.power}")
