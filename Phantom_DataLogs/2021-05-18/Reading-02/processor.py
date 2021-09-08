import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (20,8)

PACKETS = 200
SKIN_NODE = False # If there is a node placed on top of skin, change this to True

# Incase there is no plot in the right-most graph, swap the two nodes and see if it works
PhantomNode2 = '67b5.5e11.0074.1200'
PhantomNode1 = '0f2a.7d13.0074.1200'
PhantomNode1 = '3c23.5c11.0074.1200'
# RSSI readings from the RSSI register is sampled at a rate of 10e-6 seconds. Below
# line is checked as whole to avoid attempting to read incomplete log lines.
FastRSSI     = '[INFO: EavesDr   ] Fast RSSI Sampling:'

def extractPacketData(filename):
  """
  This method will take a file of packet readings as input and go through each line.
  If any line has the IP address defined above, it will fill in the points array with
  the corresponding RSSI value and another array with sequence number

  There will be four arrays returned at last, two with RSSI readings and two with seq.

  [INFO: EavesDr   ] Received 0 from 0f2a.7d13.0074.1200 [RSSI: -60 | LQI: 107]
  [INFO: EavesDr   ] Fast RSSI Sampling: -92
  """
  file_node_lines = filename.readlines()
  node_points_h1 = []
  node_seq_h1 = []
  node_points_h2 = []
  node_seq_h2 = []
  fast_rssi = []

  for line in file_node_lines:
    if (PhantomNode1 in line):
      lineAsList = line.split(' ')
      rssi = int(lineAsList[-4])
      seq = int(lineAsList[-8])
      node_points_h1.append(rssi)
      node_seq_h1.append(seq)
    elif (PhantomNode2 in line):
      lineAsList = line.split(' ')
      rssi = int(lineAsList[-4])
      seq = int(lineAsList[-8])
      node_points_h2.append(rssi)
      node_seq_h2.append(seq)
    elif (FastRSSI in line):
      lineAsList = line.split(' ')
      rssi = int(lineAsList[-1])
      fast_rssi.append(rssi)
    
  return (node_points_h1, node_seq_h1, node_points_h2, node_seq_h2, fast_rssi)

Ev1 = open('Eaves-1.txt', 'r')
Ev2 = open('Eaves-2.txt', 'r')
Ev3 = open('Eaves-3.txt', 'r')
Ev4 = open('Eaves-4.txt', 'r')
if SKIN_NODE:
  Ev5 = open('Eaves-5.txt', 'r') # This node is placed on top of skin
Ph1 = open('Phantom-1.txt', 'r')
Ph2 = open('Phantom-2.txt', 'r')

(P1_E1, S_P1_E1, P2_E1, S_P2_E1, FR_E1) = extractPacketData(Ev1)
(P1_E2, S_P1_E2, P2_E2, S_P2_E2, FR_E2) = extractPacketData(Ev2)
(P1_E3, S_P1_E3, P2_E3, S_P2_E3, FR_E3) = extractPacketData(Ev3)
(P1_E4, S_P1_E4, P2_E4, S_P2_E4, FR_E4) = extractPacketData(Ev4)
if SKIN_NODE:
  (P1_E5, S_P1_E5, P2_E5, S_P2_E5, FR_E5) = extractPacketData(Ev5)
(_, _, P2_P1, S_P2_P1, _) = extractPacketData(Ph1)
(P1_P2, S_P1_P2, _, _, _) = extractPacketData(Ph2)

if SKIN_NODE:
  f, ((ev1, ev2, ev3, ev4, ev5, pha), (fr1, fr2, fr3, fr4, fr5, fde)) = plt.subplots(2, 6, sharey=True)
else:
  f, ((ev1, ev2, ev3, ev4, pha), (fr1, fr2, fr3, fr4, fde)) = plt.subplots(2, 5, sharey=True)

f.suptitle('RSSI Measurements', fontweight='bold')

ev1.scatter(S_P1_E1, P1_E1, s=10, label='from node 1')
ev1.plot([np.mean(P1_E1) for _ in range(PACKETS)], label='node 1 mean')
ev1.scatter(S_P2_E1, P2_E1, s=10, label='from node 2')
ev1.plot([np.mean(P2_E1) for _ in range(PACKETS)], label='node 2 mean')
ev1.set_xlim(0, PACKETS)
ev1.set_title('Eaves 01')
ev1.set_xlabel('Sequence number')
ev1.set_ylabel('RSSI (dBm)')

ev2.scatter(S_P1_E2, P1_E2, s=10, label='from node 1')
ev2.plot([np.mean(P1_E2) for _ in range(PACKETS)], label='node 1 mean')
ev2.scatter(S_P2_E2, P2_E2, s=10, label='from node 2')
ev2.plot([np.mean(P2_E2) for _ in range(PACKETS)], label='node 2 mean')
ev2.set_xlim(0, PACKETS)
ev2.set_title('Eaves 02')
ev2.set_xlabel('Sequence number')

ev3.scatter(S_P1_E3, P1_E3, s=10, label='from node 1')
ev3.plot([np.mean(P1_E3) for _ in range(PACKETS)], label='node 1 mean')
ev3.scatter(S_P2_E3, P2_E3, s=10, label='from node 2')
ev3.plot([np.mean(P2_E3) for _ in range(PACKETS)], label='node 2 mean')
ev3.set_xlim(0, PACKETS)
ev3.set_title('Eaves 3')
ev3.set_xlabel('Sequence number')

ev4.scatter(S_P1_E4, P1_E4, s=10, label='from node 1')
ev4.plot([np.mean(P1_E4) for _ in range(PACKETS)], label='node 1 mean')
ev4.scatter(S_P2_E4, P2_E4, s=10, label='from node 2')
ev4.plot([np.mean(P2_E4) for _ in range(PACKETS)], label='node 2 mean')
ev4.set_xlim(0, PACKETS)
ev4.set_title('Eaves 4')
ev4.set_xlabel('Sequence number')

if SKIN_NODE:
  ev5.scatter(S_P1_E5, P1_E5, s=10, label='from node 1')
  ev5.plot([np.mean(P1_E5) for _ in range(PACKETS)], label='node 1 mean')
  ev5.scatter(S_P2_E5, P2_E5, s=10, label='from node 2')
  ev5.plot([np.mean(P2_E5) for _ in range(PACKETS)], label='node 2 mean')
  ev5.set_xlim(0, PACKETS)
  ev5.set_title('Eaves Skin')
  ev5.set_xlabel('Sequence number')

pha.scatter(S_P1_P2, P1_P2, s=10, label='from node 1')
pha.plot([np.mean(P1_P2) for _ in range(PACKETS)], label='node 1 mean')
pha.scatter(S_P2_P1, P2_P1, s=10, label='from node 2')
pha.plot([np.mean(P2_P1) for _ in range(PACKETS)], label='node 2 mean')
pha.set_xlim(0, PACKETS)
# pha.legend()
pha.set_title('In-body')
pha.set_xlabel('Sequence number')

'''
Fast RSSI sampling plots for each eavesdropping node
'''
fr1.plot(FR_E1, 'k', label='channel rssi', alpha=0.7)
fr1.set_xlabel('Reading instance')
fr1.set_ylabel('RSSI (dBm)')

fr2.plot(FR_E2, 'k', label='channel rssi', alpha=0.7)
fr2.set_xlabel('Reading instance')

fr3.plot(FR_E3, 'k', label='channel rssi', alpha=0.7)
fr3.set_xlabel('Reading instance')

fr4.plot(FR_E4, 'k', label='channel rssi', alpha=0.7)
fr4.set_xlabel('Reading instance')

if SKIN_NODE:
  fr5.plot(FR_E5)
  fr5.set_xlabel('Reading instance')

ev1.grid(True, axis='y', alpha=0.35)
ev2.grid(True, axis='y', alpha=0.35)
ev3.grid(True, axis='y', alpha=0.35)
ev4.grid(True, axis='y', alpha=0.35)
if SKIN_NODE:
  ev5.grid(True, axis='y', alpha=0.35)
pha.grid(True, axis='y', alpha=0.35)

fr1.grid(True, axis='y', alpha=0.35)
fr2.grid(True, axis='y', alpha=0.35)
fr3.grid(True, axis='y', alpha=0.35)
fr4.grid(True, axis='y', alpha=0.35)

# The legend is kept outside as all the graphs in each row share the same wording
handles_e, labels_e = ev1.get_legend_handles_labels()
handles_f, labels_f = fr1.get_legend_handles_labels()
f.legend(handles_e + handles_f, labels_e + labels_f, loc='lower right', bbox_to_anchor=(0.89, 0.2))
f.delaxes(fde)

plt.savefig('results.png', dpi=300)

plt.show()
