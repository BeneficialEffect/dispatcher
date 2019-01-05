
# The main call agents class.

class Agent:
    def __init__(self, name):
        self.name = name
        self.available = True
        self.customerID = None

    # AVAILABILITY
    def begincall(self, customerid):
        self.available = False
        self.customerID = customerid

    def endcall(self):
        self.available = True
        self.customerID = None