def get_event_date(event):
    #print(event)

    return event.date

def current_users(events):
    #print(events)
    events.sort(key = get_event_date) # ordena todo a partir de la fecha
    machines ={}
    #print(events)
    
    for event in events:
        #print(event.date)
        #print(event.type)
        if event.machine not in machines:
            machines[event.machine] = set()
            #print(machines)
        if event.type == "login":
            machines[event.machine].add(event.user)
            #print(machines)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0 :
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


class Event:
    def __init__(self,event_date,event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-29 99:99:99', 'login', 'webserver.local', 'buuu'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]
users = current_users(events)
print(users)
generate_report(users)
