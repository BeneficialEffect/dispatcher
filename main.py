from dispatcher import dispatcher, agents

dispatcher1 = dispatcher.Dispatcher([agents.Agent('Bob'), agents.Agent('Bill'), agents.Agent('Cyrus')])

dispatcher1.agents[1].begincall(12)
print(dispatcher1.agents[1].available)