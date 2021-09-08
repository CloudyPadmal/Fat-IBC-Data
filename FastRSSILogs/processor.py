import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (20,8)

filename = 'node2-fast-rssi-10e6-ch25-withtx.txt'
logFile = open(filename, 'r')

logs = logFile.readlines()

rssi = []
signal = []
idx = []
ndx = []
for i, l in enumerate(logs):
  if ('EavesDr' in l):
    try:
      rs = int(l.split(' ')[-1])
      rssi.append(rs)
      idx.append(i)
    except:
      try:
        rs = int(l.split(' ')[-4])
        signal.append(rs)
        ndx.append(i)
      except:
        continue

plt.title('Node 2 -- 10e-6 -- CH25 - With Transmitter')
plt.ylim([-120, 0])
plt.grid(True, axis='y')
plt.plot(idx, rssi)
plt.scatter(ndx, signal, c='#F39C12')
plt.savefig(filename[:-4], dpi=300)
#plt.show()
