""""
Columbia University - CSEE 4119 Computer Network
Assignment 3 - Distance Vector Routing

dvr.py - the Distance Vector Routing (DVR) program announces its distance vector to its neighbors and 
updates its routing table based on the received routing vectors from its neighbors
"""
import sys
import socket
import time

class NetworkInterface():
    """
    DO NOT EDIT.
    
    Provided interface to the network. In addition to typical send/recv methods,
    it also provides a method to receive an initial message from the network, which
    contains the costs to neighbors. 
    """
    def __init__(self, network_port, network_ip):
        """
        Constructor for the NetworkInterface class.

        Parameters:
            network_port : int
                The port the network is listening on.
            network_ip : str
                The IP address of the network.
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((network_ip, network_port))
        self.init_msg = self.sock.recv(4096).decode() # receive the initial message from the network
        
    def initial_costs(self): 
        """
        Return the initial message received from the network in following format:
        <node_id>. <neighbor_1>:<cost_1>,...,<neighbor_n>:<cost_n>

        node_id is the unique identifier for this node, i.e., dvr.py instance. 
        Neighbor_i is the unique identifier for direct neighbor nodes. All identifiers
        and costs are specified in the topology file.
        """
        return self.init_msg
    
    def send(self, message):
        """
        Send a message to all direct neigbors.

        Parameters:
            message : bytes
                The message to send.
        
        Returns:
            None
        """
        message_len = len(message)
        packet = message_len.to_bytes(4, byteorder='big') + message
        self.sock.sendall(packet)
    
    def recv(self, length):
        """
        Receive a message from neighbors. Behaves exactly like socket.recv()

        Parameters:
            length : int
                The length of the message to receive.
        
        Returns:
            bytes
                The received message.
        """
        return self.sock.recv(length)
    
    def close(self):
        """
        Close the socket connection with the network.
        """
        self.sock.close()



# ====================================================================================
# DV routing protocol
# ====================================================================================

def initialize_dv_table (init_costs):
    """
    Given the initial costs message in the format:
       "<node_id>. <neighbor_1>:<cost_1>,<neighbor_2>:<cost_2>,..."
    initialize both a 2D DV table and a 1D DV vector.

    The 2D table (dv_table) is a dict-of-dicts:
       dv_table[destination][via] = cost
    It initially includes:
       - A: {A: 0}  (optional, but useful for internal computation)
       - For each direct neighbor X: { X: cost_direct }

    The 1D DV vector (dv) takes the minimum cost for each destination:
       dv[destination] = (min_cost, next_hop)

    Returns:
       (node_id, dv_table) tuple.
    """
    # Parse the initial costs and create a distance vector table

    dv_table = {}
    node_id, neighbors = init_costs.split('. ')

    neighbors_pair = neighbors.strip().split(',')
    for each in neighbors_pair:
        neighbor, cost = each.split(':')
        neighbor = neighbor.strip()
        #  dv_table[neighbor] as destination, {neighbor: ...} as via
        dv_table[neighbor] = {neighbor: int(cost.strip())}
    return node_id, dv_table


def get_dv (node_id, dv_table):
    """
    Given a distance vector table, return a 1D distance vector.
    The 1D distance vector store the minimum cost for each destination:
       dv[destination] = (min_cost)

    Returns:
         dv : dict
              The distance vector.
    """
    dv = {}
    for dst in dv_table:
        min_cost, next_hop = min((cost, next_hop) for next_hop, cost in dv_table[dst].items())
        dv[dst] = (min_cost, next_hop)
    return dv

def serialize_dv_msg(dv, node_id):
    """
    Given a distance vector, serialize it into a string format:
       "<node_id>. <destination_1>:<cost_1>,<destination_2>:<cost_2>,..."

    Parameters:
        dv : dict
            The distance vector.
        node_id : str
            The unique identifier for this node.

    Returns:
        str
            The serialized distance vector message.
    """
    msg = f"{node_id}. "
    for dst, (min_cost, next_hop) in dv.items():
        msg += f"{dst}:{min_cost},"
    return msg[:-1] # remove the last comma


def serialize_dv_msg2(dv, node_id):
    msg = f"{node_id}. "
    for dst, (min_cost, next_hop) in dv.items():
        msg += f"{dst}:{min_cost},"
    msg = msg[:-1]  # remove the trailing comma
    return msg + "&"  # append a newline as a delimiter


def parse_msg(raw_msg):
    """
    Parse the received message from the network. The message is in the format:
       "<node_id>. <destination_1>:<cost_1>,<destination_2>:<cost_2>,..."
    """
    # Parse the received message
    # Update the distance vector table and vector based on the received message
    neighbor_id, dv_msg = raw_msg.split('. ')

    dv = {}
    for item in dv_msg.strip().split(','):
        dst, cost = item.split(':')
        dv[dst] = int(cost.strip())
    return neighbor_id, dv

def update_dv_table(node_id, dv_table, neighbor_dv, neighbor_id):
    """
    Update the distance vector table based on the received message.

    Parameters:
        node_id : str
            The unique identifier for this node.
        dv_table : dict
            The distance vector table.
        dv : dict
            The received distance vector.
        neighbor_id : str
            The unique identifier for the neighbor node.

    Returns:
        bool
            True if the dv table was updated, False otherwise.
    """

    updated = False
    # first get the direct cost to the neighbor which just sent us the message
    direct_cost_to_neighbor = dv_table[neighbor_id][neighbor_id]
    for dst, cost in neighbor_dv.items():
        if dst == node_id:
            continue

        if dst not in dv_table:
            dv_table[dst] = {}

        # check the lowest cost to reach the destination
        # dv_table[dst].get(neighbor_id) either has a old cost or is empty
        old_cost = dv_table[dst].get(neighbor_id, float('inf'))
        new_cost = cost + direct_cost_to_neighbor
        if new_cost < old_cost:
            dv_table[dst][neighbor_id] = new_cost
            updated = True

    return updated

def receive_message(net_interface):
    header = net_interface.recv(4)
    if not header:
        return None  # connection closed

    data_len = int.from_bytes(header, byteorder='big')
    data = net_interface.recv(data_len)
    if not data:
        return None

    return data.decode()


def listen_podcast(net_interface, node_id, dv_table):
    """
    Listen for incoming messages from the network. This is a blocking call.
    """
    net_interface.sock.settimeout(3)  # if no message is received in 5 seconds, we found the shortest path, exit the loop
    while True:
        try:
            # raw_msg = receive_message(net_interface)
            buffer = net_interface.recv(4096).decode()
            if not buffer:
                break
            # Split the buffer into messages
            while "&" in buffer:
                raw_msg, buffer = buffer.split("&", 1)
                # Parse the received message
                neighbor_id, neighbor_dv = parse_msg(raw_msg)
                print(f"Received distance vector from neighbor {neighbor_id}: {neighbor_dv}")
                # Update the distance vector table and vector based on the received message
                need_update = update_dv_table(node_id, dv_table, neighbor_dv, neighbor_id)
                if need_update:
                    # Update the distance vector
                    dv = get_dv(node_id, dv_table)
                    msg = serialize_dv_msg2(dv, node_id)
                    print(f"??????========DV update ready to be sent to neighbors: {msg}")
                    net_interface.send(msg.encode())
                    log_updates(dv, node_id)  # log the updates

        except socket.timeout:
            print("No updates in 5 seconds, found the shortest path and exiting.")
            break

def log_updates(dv, node_id):
    """
    Log the updates to the log file

    Parameters:
        dv : dict
            The distance vector.
        node_id : str
            The unique identifier for this node.
    """
    log_content = ""
    for dst, (min_cost, next_hop) in dv.items():
        log_content += f"{dst}:{min_cost}:{next_hop} "
    log_content = log_content[:-1]

    log_file = open(f"log_{node_id}.txt", "a")
    log_file.write(log_content + "\n")
    log_file.flush()
    log_file.close()


if __name__ == '__main__':
    network_ip = sys.argv[1] # the IP address of the network
    network_port = int(sys.argv[2]) # the port the network is listening on
 
    net_interface = NetworkInterface(network_port, network_ip) # initialize the network interface

    # get the initial costs to your neighbors to help initialize your vector and table. Format is:
    # <node_id>. <neighbor_1>:<cost_1>,...,<neighbor_n>:<cost_n>
    init_costs = net_interface.initial_costs()

    print( "Initial costs before parsing: ", init_costs)
    # Initialize the distance vector table and vector
    node_id, dv_table = initialize_dv_table(init_costs)

    print( "Initializing distance vector...")
    dv= get_dv(node_id, dv_table) # get the distance vector message
    log_updates(dv, node_id) # log the updates

    msg = serialize_dv_msg2(dv, node_id) # serialize the distance vector message
    print( "DV ready to be sent to neighbors: ", msg)


    net_interface.send(msg.encode()) # send the distance vector to neighbors


    # Listen for incoming messages from the network
    listen_podcast(net_interface, node_id, dv_table)
    # Found the shortest path, exit the loop


    # Close the interface with the network
    net_interface.close()