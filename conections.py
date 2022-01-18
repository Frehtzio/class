#Begin Portion 2#
import random

class Server:
    
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        
        
        id = connection_load
        self.connections[connection_id] = id
        
        
        # Add the connection to the dictionary with the calculated load
       
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        #self.connections[connection_id] = 0
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for key,value in self.connections.items():
            total += round(value)


        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())    #0%
    
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]
        

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        return self.connections

        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        del self.connections[connection_id]
        # Find out the right server

        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        se = 0
        
        for server,id in self.connections.items():
            se += 1
        se == se / 50

        # Sum the load of each server and divide by the amount of servers
    
        return se

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        for connection in range(self.connections.values()):
            l.add_connection(connection)
            print(l)

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#
l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())
