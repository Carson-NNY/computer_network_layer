
# CSEE 4119 Spring 2025, Assignment 3
## Guanhong Liu
## GitHub username: Carson-NNY

---

## Overview

This program implements the **Distance Vector Routing (DVR)** protocol as specified in the requirement. Each node maintains a distance vector table and exchanges its minimum-cost routes(dv) with neighbors over a simulated TCP network. 

---

## Files

- **`dvr.py`**: Main program implementing the DVR protocol.
- **`network.py`**: serves as a proxy for the DV routing program
- **`README.md`**: This file.
- **`TESTING.md`**: test cases and their outputs.
- **`log_<node_id>.txt`**: Log file containing DV updates recorded by a node.

---

### Installation Guide:

To set up the environment for running the project, follow these installation steps.

**Prerequisites**
Having **Python 3** installed on your system.

**Required Dependencies**
### **1. Install Python Package Manager (pip)**
If `pip` is not installed, install it first.
```sh
sudo apt-get update
sudo apt install python3-pip
pip install opencv-python
sudo apt install libgl1-mesa-glx
```

## Usage

### 1. Start the network simulator
```sh
python3 network.py 5000 topology.dat
```

### 2. Start all the nodes (expected number of dvr.py instances is the number of nodes is defined in `topology.dat` )
```
python3 dvr.py 127.0.0.1 5000
```

Each node connects to the network simulator and begins routing updates.

---

## How It Works

### Initialization

1. Each node receives an initial cost message from the network in the format:

   ```
   <node_id>. <neighbor_1>:<cost_1>,<neighbor_2>:<cost_2>,...
   ```

2. The `initialize_dv_table()` function parses this message into a distance vector table (`dv_table`) and computes an initial distance vector (`dv`).


### Distance Vector Updates

- Nodes listen for incoming messages using `listen_podcast()`.
- Upon receiving a message:
  - The message is parsed using `parse_msg()`.
  - The DV table is updated via `update_dv_table()`.
  - If any cost is improved, the node recomputes and broadcasts its new DV.
- Timeout: If no message is received for 10 seconds, the node assumes convergence and exits.


### Functions:

- **`initialize_dv_table(init_costs)`**  
  Parses the initial cost message and builds the initial DV table.

- **`get_dv(node_id, dv_table)`**  
  Extracts the minimum-cost path and next hop for each destination from the DV table.

- **`serialize_dv_msg(dv, node_id)`**  
  Converts the DV into a string for sending, without a delimiter.

- **`serialize_dv_msg2(dv, node_id)`**  
  Same as above but appends `&` as a delimiter for streaming.

- **`parse_msg(raw_msg)`**  
  Parses a received message into the sender’s ID and its DV.

- **`update_dv_table(node_id, dv_table, neighbor_dv, neighbor_id)`**  
  Updates the DV table using a neighbor's DV; returns `True` if updated.

- **`receive_message(net_interface)`**  
  Reads a length-prefixed message from the network. (Unused helper.)

- **`listen_podcast(net_interface, node_id, dv_table)`**  
  Listens for DV updates, updates table if needed, and rebroadcasts.

- **`log_updates(dv, node_id)`**  
  Logs the current DV to a file for monitoring.

---


## Assumptions

- The network simulator provides the correct initial cost format.
- All nodes are connected in a bidirectional topology.
- There is no packet loss or corruption in this simulation.



---

