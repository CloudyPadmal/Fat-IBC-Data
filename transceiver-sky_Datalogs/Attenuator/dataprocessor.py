import matplotlib.pyplot as plt
import numpy as np

class Point:
  def __init__(self, seq, rssi, lqi):
    self.seq = seq
    self.rssi = rssi
    self.lqi = lqi

Host2 = '0012.4b00.060d.b459'
Host1 = '0012.4b00.060d.b5f0'
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

Fil1 = open('At1.txt', 'r')
Fil2 = open('At2.txt', 'r')
Eves = open('Ev2.txt', 'r')

(F1_H1, F1_H2, F1_H3) = extractPacketData(Fil1)
(F2_H1, F2_H2, F2_H3) = extractPacketData(Fil2)
(F3_H1, F3_H2, F3_H3) = extractPacketData(Eves)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

f.suptitle("Transmit power @ -10dBm", fontsize="x-large")

ax1.plot(F3_H1[:79])
ax1.plot(F2_H1[:79])
ax1.legend(['RSSI @ Eaves node', 'RSSI @ Node 2'])
ax1.set_title('Transmission from Node 1')
ax1.set_xlabel('Sequence number of packet')
ax1.set_ylabel('RSSI Value')

ax2.plot(F3_H2[:79])
ax2.plot(F1_H2[:79])
ax2.legend(['RSSI @ Eaves node', 'RSSI @ Node 1'])
ax2.set_title('Transmission from Node 2')
ax2.set_xlabel('Sequence number of packet')
ax2.set_ylabel('RSSI Value')

plt.show()
