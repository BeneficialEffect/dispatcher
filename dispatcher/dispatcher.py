
# The main call dispatcher class.

class Dispatcher:
    def __init__(self, agents):
        # Agents expects a list of agents
        self.agents = agents

    def schedule_call(self, customerid):
        flag = False
        for agent in self.agents:
            if agent.available:
                agent.begincall(customerid)
                flag = True
                break

        if flag:
            return agent.name
        else:
            return flag
