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
        return "{:.2f}%".format(self.load())
    

server = Server()
server.add_connection("192.168.1.1")

print(server.load())
