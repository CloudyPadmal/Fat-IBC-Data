import matplotlib.pyplot as plt
import numpy as np

order = [1, 2, 3, 4, 5, 6]
order_ = ['01#02', '01#03', '01#04', '02#03', '02#04', '03#04']

readings = [[-102.97440037676186, 3.418163283943891, -102.18044531144895, 3.367122233981684, -99.76084113089848, 3.0877734329553417, -98.36947461687396, 2.9532453393865223], [-102.90051123368761, 3.590050230312948, -102.15699979837355, 3.903536841167783, -99.69821751658513, 3.390680063107285, -97.83463430632995, 3.3880843144991712], [-103.49701590235263, 3.159515617461766, -101.4536958695485, 3.1402292159593332, -99.91327236397171, 3.3720705525173225, -99.17943372626313, 3.000527823406684], [-103.34450128861022, 3.33063822662008, -101.80446734074046, 3.6205255177398215, -100.16267629991161, 3.6237710127767153, -99.26984187319447, 3.2008401316463195],[-103.31024139004442, 3.6000640794188143, -102.59705291738553, 3.5003271089207786, -100.50637203650852, 3.3072174440428177, -97.69486621290199, 3.194116836173274], [-103.11342382009389, 3.470857101818307, -102.16454039908407, 3.683583884012709, -99.77071863228049, 3.925176045560076, -98.34634577950806, 3.118270692417858]]

e01mean = []; e01std = []
e02mean = []; e02std = []
e03mean = []; e03std = []
e04mean = []; e04std = []

for r in readings: # antenna combination
    e01mean.append(r[0])
    e01std.append(r[1])
    e02mean.append(r[2])
    e02std.append(r[3])
    e03mean.append(r[4])
    e03std.append(r[5])
    e04mean.append(r[6])
    e04std.append(r[7])


fig = plt.figure()
fig.suptitle('Comparison of RSSI measurements for implantable antenna pairs', fontweight='bold', y=0.95)

alls = plt.subplot2grid((4, 2), (0, 0), rowspan=4)
ax2 = plt.subplot2grid((4, 2), (0, 1), colspan=1)
ax3 = plt.subplot2grid((4, 2), (1, 1), colspan=1)
ax4 = plt.subplot2grid((4, 2), (2, 1), colspan=1)
ax5 = plt.subplot2grid((4, 2), (3, 1), colspan=1)

axes = [ax2, ax3, ax4, ax5]

for a in axes:
    a.set_xticks(order)
    a.set_xticklabels(order_)
    a.set_ylim([-107, -94])

a1 = alls.errorbar(y=e01mean, x=order, yerr=e01std, capsize=5)
a2 = alls.errorbar(y=e02mean, x=order, yerr=e02std, capsize=5)
a3 = alls.errorbar(y=e03mean, x=order, yerr=e03std, capsize=5)
a4 = alls.errorbar(y=e04mean, x=order, yerr=e04std, capsize=5)
alls.set_xticks(order)
alls.set_xticklabels(order_)
alls.set_ylim([-107, -94])
alls.set_xlabel('Antenna combination')
alls.set_ylabel('RSSI (dBm)')
alls.legend(['Antenna 01', 'Antenna 02', 'Antenna 03', 'Antenna 04'], loc='upper center')
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

ax2.errorbar(y=e01mean, x=order, yerr=e01std, capsize=5, color=cycle[0])
ax2.scatter(x=order[np.argmin(e01std)], y=e01mean[np.argmin(e01std)], s=40, color=cycle[0], marker='s')
ax2.yaxis.set_label_position('right')
ax2.set_ylabel('Antenna 01')
ax3.errorbar(y=e02mean, x=order, yerr=e02std, capsize=5, color=cycle[1])
ax3.scatter(x=order[np.argmin(e02std)], y=e02mean[np.argmin(e02std)], s=40, color=cycle[1], marker='s')
ax3.yaxis.set_label_position('right')
ax3.set_ylabel('Antenna 02')
ax4.errorbar(y=e03mean, x=order, yerr=e03std, capsize=5, color=cycle[2])
ax4.scatter(x=order[np.argmin(e03std)], y=e03mean[np.argmin(e03std)], s=40, color=cycle[2], marker='s')
ax4.yaxis.set_label_position('right')
ax4.set_ylabel('Antenna 03')
ax5.errorbar(y=e04mean, x=order, yerr=e04std, capsize=5, color=cycle[3])
ax5.scatter(x=order[np.argmin(e04std)], y=e04mean[np.argmin(e04std)], s=40, color=cycle[3], marker='s')
ax5.legend(['Minimum variance', 'Mean and Variance'], loc='lower right')
ax5.yaxis.set_label_position('right')
ax5.set_ylabel('Antenna 04')
ax5.set_xlabel('Antenna combination')

plt.show()