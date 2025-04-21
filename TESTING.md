# CSEE 4119 Spring 2025, Assignment 3 Testing File
## name: Guanhong Liu
## GitHub username: Carson-NNY

# Testing
- For all the test results, the operation process is the same as the following:
  1. start network.py
  2. run  dvr.py (# of instances = number of nodes)
---
## **Test Case 1: 3 nodes**
### **topology.dat:**
```
A B 2
A C 2
```

### **Output for the Log_A File:**
```
B:2:B C:2:C
B:2:B C:2:C
B:2:B C:2:C
B:2:B C:2:C
B:2:B C:2:C
B:2:B C:2:C

```

### **Output for the Log_B File:**
```
A:2:A
A:2:A C:4:A
A:2:A C:4:A

```

### **Output for the Log_C File:**
```
A:2:A
A:2:A B:4:A
A:2:A B:4:A
```


## **Test Case 2: 5 nodes**
### **topology.dat:**
```
A B 5
A C 1
B C 2
B D 1
C D 4
C E 10
D E 3

```

### **Output for the Log_A File:**
```
B:5:B C:1:C
B:5:B C:1:C D:6:B
B:3:C C:1:C D:5:C E:11:C
B:3:C C:1:C D:4:C E:11:C
B:3:C C:1:C D:4:C E:11:C
B:3:C C:1:C D:4:C E:9:B
B:3:C C:1:C D:4:C E:8:C
B:3:C C:1:C D:4:C E:7:C
B:3:C C:1:C D:4:C E:7:C

```

### **Output for the Log_B File:**
```
A:5:A C:2:C D:1:D
A:5:A C:2:C D:1:D
A:3:C C:2:C D:1:D E:12:C
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D
A:3:C C:2:C D:1:D E:4:D

```

### **Output for the Log_C File:**
```
A:1:A B:2:B D:4:D E:10:E
A:1:A B:2:B D:3:B E:10:E
A:1:A B:2:B D:3:B E:10:E
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:7:D
A:1:A B:2:B D:3:B E:6:B
A:1:A B:2:B D:3:B E:6:B
A:1:A B:2:B D:3:B E:6:B
A:1:A B:2:B D:3:B E:6:B
A:1:A B:2:B D:3:B E:6:B
A:1:A B:2:B D:3:B E:6:B
A:1:A B:2:B D:3:B E:6:B
A:1:A B:2:B D:3:B E:6:B

```

### **Output for the Log_D File:**
```
B:1:B C:4:C E:3:E
B:1:B C:3:B E:3:E A:6:B
B:1:B C:3:B E:3:E A:5:C
B:1:B C:3:B E:3:E A:5:C
B:1:B C:3:B E:3:E A:5:C
B:1:B C:3:B E:3:E A:5:C
B:1:B C:3:B E:3:E A:5:C
B:1:B C:3:B E:3:E A:4:B
B:1:B C:3:B E:3:E A:4:B
B:1:B C:3:B E:3:E A:4:B
B:1:B C:3:B E:3:E A:4:B
B:1:B C:3:B E:3:E A:4:B
B:1:B C:3:B E:3:E A:4:B
B:1:B C:3:B E:3:E A:4:B
B:1:B C:3:B E:3:E A:4:B

```

### **Output for the Log_E File:**
```
C:10:C D:3:D
C:10:C D:3:D A:11:C B:12:C
C:7:D D:3:D A:11:C B:4:D
C:6:D D:3:D A:9:D B:4:D
C:6:D D:3:D A:9:D B:4:D
C:6:D D:3:D A:8:D B:4:D
C:6:D D:3:D A:8:D B:4:D
C:6:D D:3:D A:7:D B:4:D
C:6:D D:3:D A:7:D B:4:D
C:6:D D:3:D A:7:D B:4:D

```

## **Test Case 3: 10 nodes**
### **topology.dat:**
```
A B 1
A E 2
B F 5
B A 1
C D 1
C G 5
D H 2
D C 1
E A 2
E I 3
F B 5
F I 4
G C 5
G J 4
H D 2
H J 3
I F 4
I E 3
J G 4
J H 3

```

### **Output for the Log_A File:**
```
B:1:B E:2:E
B:1:B E:2:E F:6:B
B:1:B E:2:E F:6:B I:5:E
B:1:B E:2:E F:6:B I:5:E
B:1:B E:2:E F:6:B I:5:E
B:1:B E:2:E F:6:B I:5:E
B:1:B E:2:E F:6:B I:5:E
B:1:B E:2:E F:6:B I:5:E
B:1:B E:2:E F:6:B I:5:E
```

### **Output for the Log_B File:**
```
A:1:A F:5:F
A:1:A F:5:F I:9:F
A:1:A F:5:F I:9:F E:3:A
A:1:A F:5:F I:9:F E:3:A
A:1:A F:5:F I:9:F E:3:A
A:1:A F:5:F I:9:F E:3:A
A:1:A F:5:F I:6:A E:3:A
A:1:A F:5:F I:6:A E:3:A
```

### **Output for the Log_C File:**
```
D:1:D G:5:G
D:1:D G:5:G J:9:G
D:1:D G:5:G J:9:G H:3:D
D:1:D G:5:G J:9:G H:3:D
D:1:D G:5:G J:9:G H:3:D
D:1:D G:5:G J:6:D H:3:D
D:1:D G:5:G J:6:D H:3:D
D:1:D G:5:G J:6:D H:3:D
```

### **Output for the Log_D File:**
```
C:1:C H:2:H
C:1:C H:2:H G:6:C
C:1:C H:2:H G:6:C J:5:H
C:1:C H:2:H G:6:C J:5:H
C:1:C H:2:H G:6:C J:5:H
C:1:C H:2:H G:6:C J:5:H
C:1:C H:2:H G:6:C J:5:H
C:1:C H:2:H G:6:C J:5:H
C:1:C H:2:H G:6:C J:5:H
```

### **Output for the Log_E File:**
```
A:2:A I:3:I
A:2:A I:3:I F:7:I
A:2:A I:3:I F:7:I B:3:A
A:2:A I:3:I F:7:I B:3:A
A:2:A I:3:I F:7:I B:3:A
A:2:A I:3:I F:7:I B:3:A
A:2:A I:3:I F:7:I B:3:A
A:2:A I:3:I F:7:I B:3:A
A:2:A I:3:I F:7:I B:3:A
```
### **Output for the Log_F File:**
```
B:5:B I:4:I
B:5:B I:4:I E:7:I
B:5:B I:4:I E:7:I A:6:B
B:5:B I:4:I E:7:I A:6:B
B:5:B I:4:I E:7:I A:6:B
B:5:B I:4:I E:7:I A:6:B
B:5:B I:4:I E:7:I A:6:B
B:5:B I:4:I E:7:I A:6:B
B:5:B I:4:I E:7:I A:6:B
B:5:B I:4:I E:7:I A:6:B
```
### **Output for the Log_G File:**
```
C:5:C J:4:J
C:5:C J:4:J D:6:C
C:5:C J:4:J D:6:C H:7:J
C:5:C J:4:J D:6:C H:7:J
C:5:C J:4:J D:6:C H:7:J
C:5:C J:4:J D:6:C H:7:J
C:5:C J:4:J D:6:C H:7:J
C:5:C J:4:J D:6:C H:7:J
C:5:C J:4:J D:6:C H:7:J
C:5:C J:4:J D:6:C H:7:J
```
### **Output for the Log_H File:**
```
D:2:D J:3:J
D:2:D J:3:J C:3:D
D:2:D J:3:J C:3:D G:7:J
D:2:D J:3:J C:3:D G:7:J
D:2:D J:3:J C:3:D G:7:J
D:2:D J:3:J C:3:D G:7:J
D:2:D J:3:J C:3:D G:7:J
D:2:D J:3:J C:3:D G:7:J
D:2:D J:3:J C:3:D G:7:J
```
### **Output for the Log_I File:**
```
F:4:F E:3:E
F:4:F E:3:E B:9:F
F:4:F E:3:E B:9:F A:5:E
F:4:F E:3:E B:9:F A:5:E
F:4:F E:3:E B:9:F A:5:E
F:4:F E:3:E B:9:F A:5:E
F:4:F E:3:E B:6:E A:5:E
F:4:F E:3:E B:6:E A:5:E
```
### **Output for the Log_J File:**
```
G:4:G H:3:H
G:4:G H:3:H D:5:H
G:4:G H:3:H D:5:H C:9:G
G:4:G H:3:H D:5:H C:6:H
G:4:G H:3:H D:5:H C:6:H
G:4:G H:3:H D:5:H C:6:H
G:4:G H:3:H D:5:H C:6:H
G:4:G H:3:H D:5:H C:6:H
```
