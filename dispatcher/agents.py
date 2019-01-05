
# The main call agents class.

class Agent:
    def __init__(self, name):
        self.name = name
        self.available = True

    # AVAILABILITY
    def begincall(self):
        self.available = False

    def endcall(self):
        self.available = True