from dispatcher import dispatcher, agents

dispatcher1 = dispatcher.Dispatcher([agents.Agent('Bob'), agents.Agent('Bill'), agents.Agent('Cyrus')])

print(dispatcher1.schedule_call(546))
print(dispatcher1.schedule_call(545))
print(dispatcher1.schedule_call(5471))
print(dispatcher1.schedule_call(5146))