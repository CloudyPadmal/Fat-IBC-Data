import matplotlib.pyplot as plt
import numpy as np

PACKETS = 200
# Incase there is no plot in the right-most graph, swap the two nodes and see if it works
PhantomNode2 = '67b5.5e11.0074.1200'
PhantomNode1 = '0f2a.7d13.0074.1200'

def extractPacketData(filename):
  """
  This method will take a file of packet readings as input and go through each line.
  If any line has the IP address defined above, it will fill in the points array with
  the corresponding RSSI value and another array with sequence number

  There will be four arrays returned at last, two with RSSI readings and two with seq.
  """
  file_node_lines = filename.readlines()
  node_points_h1 = []
  node_seq_h1 = []
  node_points_h2 = []
  node_seq_h2 = []

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
    
  return (node_points_h1, node_seq_h1, node_points_h2, node_seq_h2)

Ev1 = open('Eaves-1.txt', 'r')
Ev2 = open('Eaves-2.txt', 'r')
Ev3 = open('Eaves-3.txt', 'r')
Ev4 = open('Eaves-4.txt', 'r')
Ph1 = open('Phantom-1.txt', 'r')
Ph2 = open('Phantom-2.txt', 'r')

(P1_E1, S_P1_E1, P2_E1, S_P2_E1) = extractPacketData(Ev1)
(P1_E2, S_P1_E2, P2_E2, S_P2_E2) = extractPacketData(Ev2)
(P1_E3, S_P1_E3, P2_E3, S_P2_E3) = extractPacketData(Ev3)
(P1_E4, S_P1_E4, P2_E4, S_P2_E4) = extractPacketData(Ev4)
(_, _, P2_P1, S_P2_P1) = extractPacketData(Ph1)
(P1_P2, S_P1_P2, _, _) = extractPacketData(Ph2)

f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, sharey=True)

f.suptitle('RSSI Measurements', fontweight='bold')

ax1.scatter(S_P1_E1, P1_E1, s=10, label='from node 1')
ax1.plot([np.mean(P1_E1) for _ in range(PACKETS)], label='node 1 mean')
ax1.scatter(S_P2_E1, P2_E1, s=10, label='from node 2')
ax1.plot([np.mean(P2_E1) for _ in range(PACKETS)], label='node 2 mean')
ax1.set_xlim(0, PACKETS)
ax1.legend()
ax1.set_title('Eaves 01')
ax1.set_xlabel('Sequence number')
ax1.set_ylabel('RSSI (dBm)')

ax2.scatter(S_P1_E2, P1_E2, s=10, label='from node 1')
ax2.plot([np.mean(P1_E2) for _ in range(PACKETS)], label='node 1 mean')
ax2.scatter(S_P2_E2, P2_E2, s=10, label='from node 2')
ax2.plot([np.mean(P2_E2) for _ in range(PACKETS)], label='node 2 mean')
ax2.set_xlim(0, PACKETS)
ax2.legend()
ax2.set_title('Eaves 02')
ax2.set_xlabel('Sequence number')

ax3.scatter(S_P1_E3, P1_E3, s=10, label='from node 1')
ax3.plot([np.mean(P1_E3) for _ in range(PACKETS)], label='node 1 mean')
ax3.scatter(S_P2_E3, P2_E3, s=10, label='from node 2')
ax3.plot([np.mean(P2_E3) for _ in range(PACKETS)], label='node 2 mean')
ax3.set_xlim(0, PACKETS)
ax3.legend()
ax3.set_title('Eaves 3')
ax3.set_xlabel('Sequence number')

ax4.scatter(S_P1_E4, P1_E4, s=10, label='from node 1')
ax4.plot([np.mean(P1_E4) for _ in range(PACKETS)], label='node 1 mean')
ax4.scatter(S_P2_E4, P2_E4, s=10, label='from node 2')
ax4.plot([np.mean(P2_E4) for _ in range(PACKETS)], label='node 2 mean')
ax4.set_xlim(0, PACKETS)
ax4.legend()
ax4.set_title('Eaves 4')
ax4.set_xlabel('Sequence number')

ax5.scatter(S_P1_P2, P1_P2, s=10, label='from node 1')
ax5.plot([np.mean(P1_P2) for _ in range(PACKETS)], label='node 1 mean')
ax5.scatter(S_P2_P1, P2_P1, s=10, label='from node 2')
ax5.plot([np.mean(P2_P1) for _ in range(PACKETS)], label='node 2 mean')
ax5.set_xlim(0, PACKETS)
ax5.legend()
ax5.set_title('In-body')
ax5.set_xlabel('Sequence number')

ax1.grid(True, axis='y', alpha=0.35)
ax2.grid(True, axis='y', alpha=0.35)
ax3.grid(True, axis='y', alpha=0.35)
ax4.grid(True, axis='y', alpha=0.35)
ax5.grid(True, axis='y', alpha=0.35)
plt.show()
