
## CSEEW4119 Assignment 3: Distance Vector Routing

---

## 1. Data Structures
The core data structure is `dv_table`, a nested dictionary:

```python
dv_table[destination][via] = cost
```

Each key(row) is a destination node, and its value is a dictionary where each entry represents the cost to that destination via a neighbor.

This allows us to easily track and update the cost to each destination through different neighbors, and then propagate the best-known dv during the execution of the distance vector algorithm.

`dv`:

This is a another dictionary derived from `dv_table`, holding the current best-known path:

```python
dv[destination] = (min_cost, next_hop)
```

This is used for sending updates to neighbors to notify the latest shortest cost found for the current node. 

---

## 2. Packet Format

### Serialized Distance Vector Message Packet: 

Message packet exchanged between nodes are in this format:

```
<sender_id>. <dst1>:<cost1>,<dst2>:<cost2>,...,<dstN>:<costN>&
```

- `.` separates the sender from the rest of the message.
- Each `:` separates destination and cost.
- `,` separates entries.
- `&` is used as a message delimiter to handle multiple messages in a TCP buffer, otherwise there maight be cases when the node receives payload from the network and the payload may consist of multiple messages from different nodes, resulting in a parsing error.

**Example:**

```
B. A:2,C:4,D:3&
```

This indicates that node B can reach:
- A with cost 2,
- C with cost 4,
- D with cost 3.

### Packet Serialization / Deserialization

- **`serialize_dv_msg2(dv, node_id)`** creates the outbound message packet.
- **`parse_msg(raw_msg)`** processes incoming message packet and returns a tuple of `(neighbor_id, neighbor_dv)`.

---

## 3. Protocol Logic

### Initialization

Each node starts by calling `net_interface.initial_costs()`, which returns the link cost to its direct neighbors. This is parsed by `initialize_dv_table()` to build the initial `dv_table`.

### packet Sending

After initializing the table and computing the initial DV using `get_dv()`, the node serializes the DV and sends it to all neighbors using `net_interface.send()`.

```python
net_interface.send(serialize_dv_msg2(dv, node_id).encode())
```

### Message Receiving

Then we do a function  where  nodes listen for incoming messages in a loop inside `listen_podcast()`. When a message arrives:

1. It is parsed using `parse_msg()`, and get the `neighbor_id` and `neighbor_dv`, which will help us to update the `dv_table`.
2. The `dv_table` is updated with `update_dv_table()` using the received `neighbor_dv` and the `neighbor_id`.
3. If there’s any change in `dv_table`, a new DV is computed and broadcast to neighbors.
---

## 4. Convergence Detection

Instead of comparing successive DVs, this implementation uses a socket timeout (`net_interface.sock.settimeout(10)`) as a metric for convergence.
Based on the assumption of this assignment(10 nodes at most), we set `net_interface.sock.settimeout(10)` which would be long enough for the nodes 
to receive the updates from all the neighbors. If no updates are received within this time, we assume the network has converged and exit the loop.


---

## 5. Logging

DV updates are written to a log file using `log_updates(dv, node_id)`. The format for each line is:

```
<dst>:<min_cost>:<next_hop> ...
```

**Example:**

```
B:2:B C:5:B D:3:C
```

The log file is named `log_<node_id>.txt`.

We use `flush()` after every write to ensure the data is written immediately, which is critical for autograder compatibility.

and after `listen_podcast()` is called, we also log the final DV before exiting the program to make sure all we are not missing any updates to be recorded in the log file.

---



