import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (20,8)

PACKETS = 200
SKIN_NODE = False # If there is a node placed on top of skin, change this to True
MIN_RSSI = -100
MAX_RSSI = -40

props = dict(boxstyle='round', facecolor='#cccccc', alpha=0.5)

# Incase there is no plot in the right-most graph, swap the two nodes and see if it works
PhantomNode2 = '67b5.5e11.0074.1200'
# PhantomNode1 = '0f2a.7d13.0074.1200'
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
      try:
        lineAsList = line.split(' ')
        rssi = int(lineAsList[-4])
        seq = int(lineAsList[-8])
        node_points_h1.append(rssi)
        node_seq_h1.append(seq)
      except:
        continue
    elif (PhantomNode2 in line):
      try:
        lineAsList = line.split(' ')
        rssi = int(lineAsList[-4])
        seq = int(lineAsList[-8])
        node_points_h2.append(rssi)
        node_seq_h2.append(seq)
      except:
        continue
    elif (FastRSSI in line):
      lineAsList = line.split(' ')
      rssi = int(lineAsList[-1])
      fast_rssi.append(rssi)
    
  return (node_points_h1, node_seq_h1, node_points_h2, node_seq_h2, fast_rssi)

Ev1 = open('Eaves-1.txt', 'r')
Ev2 = open('Eaves-2.txt', 'r')
Ph1 = open('Phantom-1.txt', 'r')
Ph2 = open('Phantom-2.txt', 'r')

(P1_E1, S_P1_E1, P2_E1, S_P2_E1, FR_E1) = extractPacketData(Ev1)
(P1_E2, S_P1_E2, P2_E2, S_P2_E2, FR_E2) = extractPacketData(Ev2)
(_, _, P2_P1, S_P2_P1, _) = extractPacketData(Ph1)
(P1_P2, S_P1_P2, _, _, _) = extractPacketData(Ph2)

f, ((ev1, ev2, pha), (fr1, fr2, fde)) = plt.subplots(2, 3, sharey=False)

f.suptitle('RSSI Measurements', fontweight='bold')

print(P1_E1)
print(S_P1_E1)
print(len(S_P1_E1), len(P1_E1))
prr = 'N1:' + str(round((len(P1_E1)/1),2)) + ' | N2:' + str(round((len(P2_E1)/1),2))
ev1.scatter(S_P1_E1, P1_E1, s=10, label='from node 1')
ev1.plot([np.mean(P1_E1) for _ in range(PACKETS)], label='node 1 mean')
ev1.scatter(S_P2_E1, P2_E1, s=10, label='from node 2')
ev1.plot([np.mean(P2_E1) for _ in range(PACKETS)], label='node 2 mean')
ev1.set_xlim(0, PACKETS)
ev1.set_ylim(MIN_RSSI, MAX_RSSI)
ev1.set_title('Eaves 01')
ev1.set_xlabel('Sequence number')
ev1.set_ylabel('RSSI (dBm)')
ev1.text(0.3, 0.95, prr, transform=ev1.transAxes, fontsize=8,
        verticalalignment='center', bbox=props)

prr = 'N1:' + str(round((len(P1_E2)/1),2)) + ' | N2:' + str(round((len(P2_E2)/1),2))
ev2.scatter(S_P1_E2, P1_E2, s=10, label='from node 1')
ev2.plot([np.mean(P1_E2) for _ in range(PACKETS)], label='node 1 mean')
ev2.scatter(S_P2_E2, P2_E2, s=10, label='from node 2')
ev2.plot([np.mean(P2_E2) for _ in range(PACKETS)], label='node 2 mean')
ev2.set_xlim(0, PACKETS)
ev2.set_ylim(MIN_RSSI, MAX_RSSI)
ev2.set_title('Eaves 02')
ev2.set_xlabel('Sequence number')
ev2.text(0.3, 0.95, prr, transform=ev2.transAxes, fontsize=8,
        verticalalignment='center', bbox=props)

prr = 'N1:' + str(round((len(P1_P2)/1),2)) + ' | N2:' + str(round((len(P2_P1)/1),2))
pha.scatter(S_P1_P2, P1_P2, s=10, label='from node 1')
pha.plot([np.mean(P1_P2) for _ in range(PACKETS)], label='node 1 mean')
pha.scatter(S_P2_P1, P2_P1, s=10, label='from node 2')
pha.plot([np.mean(P2_P1) for _ in range(PACKETS)], label='node 2 mean')
pha.set_xlim(0, PACKETS)
pha.set_ylim(MIN_RSSI, MAX_RSSI)
pha.set_title('In-body')
pha.set_xlabel('Sequence number')
pha.text(0.3, 0.95, prr, transform=pha.transAxes, fontsize=8,
        verticalalignment='center', bbox=props)

'''
Fast RSSI sampling plots for each eavesdropping node
'''
fr1.plot(FR_E1, 'k', label='channel rssi', alpha=0.7)
fr1.set_xlabel('Reading instance')
fr1.set_ylabel('RSSI (dBm)')

fr2.plot(FR_E2, 'k', label='channel rssi', alpha=0.7)
fr2.set_xlabel('Reading instance')

ev1.grid(True, axis='y', alpha=0.35)
ev2.grid(True, axis='y', alpha=0.35)
pha.grid(True, axis='y', alpha=0.35)

fr1.grid(True, axis='y', alpha=0.35)
fr2.grid(True, axis='y', alpha=0.35)

# The legend is kept outside as all the graphs in each row share the same wording
handles_e, labels_e = ev1.get_legend_handles_labels()
handles_f, labels_f = fr1.get_legend_handles_labels()
f.legend(handles_e + handles_f, labels_e + labels_f, loc='lower right', bbox_to_anchor=(0.85, 0.2))
f.delaxes(fde)

plt.savefig('results.png', dpi=300)

plt.show()
