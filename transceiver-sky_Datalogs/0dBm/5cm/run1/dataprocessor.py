import matplotlib.pyplot as plt
import numpy as np

class Point:
  def __init__(self, seq, rssi, lqi):
    self.seq = seq
    self.rssi = rssi
    self.lqi = lqi

Host1 = '0012.4b00.060d.b459'
Host2 = '0012.4b00.060d.b5f0'
Host3 = '0012.4b00.11f4.8192'

KeyToLook = 'Packet Buffer =>'
PWD = ''
Range = 500

def extractPacketData(filename):
  file_node_lines = filename.readlines()
  node_points_h1 = []
  node_points_h2 = []
  node_points_h3 = []

  for line in file_node_lines:
    if (Host1 in line):
      lineAsList = line.split(' ')
      seq = lineAsList[-7]
      rssi = int(lineAsList[-4])
      lqi = int(lineAsList[-1][:2])
      p = Point(seq, rssi, lqi)
      # node_points_h1.append(p)
      node_points_h1.append(rssi)
    elif (Host2 in line):
      lineAsList = line.split(' ')
      seq = lineAsList[-7]
      rssi = int(lineAsList[-4])
      lqi = int(lineAsList[-1][:2])
      p = Point(seq, rssi, lqi)
      # node_points_h2.append(p)
      node_points_h2.append(rssi)
    elif (Host3 in line):
      lineAsList = line.split(' ')
      seq = lineAsList[-7]
      rssi = int(lineAsList[-4])
      lqi = int(lineAsList[-1][:2])
      p = Point(seq, rssi, lqi)
      # node_points_h3.append(p)
      node_points_h3.append(rssi)
    
  return (node_points_h1, node_points_h2, node_points_h3)

Fil1 = open('N1-1.txt', 'r')
Fil2 = open('N2-1.txt', 'r')
Eves = open('Ev-1.txt', 'r')

(F1_H1, F1_H2, F1_H3) = extractPacketData(Fil1)
(F2_H1, F2_H2, F2_H3) = extractPacketData(Fil2)
(F3_H1, F3_H2, F3_H3) = extractPacketData(Eves)

f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)

ax1.plot(F1_H2)
ax1.plot(F1_H3)
ax1.legend(['Node 2', 'Eaves'])
ax1.set_title('Node 1')
ax1.set_xlabel('Sequence number of packet')
ax1.set_ylabel('RSSI Value')

ax2.plot(F2_H1)
ax2.plot(F2_H3)
ax2.legend(['Node 1', 'Eaves'])
ax2.set_title('Node 2')
ax2.set_xlabel('Sequence number of packet')
ax2.set_ylabel('RSSI Value')

ax3.plot(F3_H1)
ax3.plot(F3_H2)
ax3.legend(['Node 1', 'Node 2'])
ax3.set_title('Eavesdropper')
ax3.set_xlabel('Sequence number of packet')
ax3.set_ylabel('RSSI Value')

plt.show()
