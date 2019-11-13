import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold'
#         }
# matplotlib.rc('font', **font)

# my_font =font_manager.FontProperties(fname="C:\Windows\Fonts\Microsoft YaHei UI")
my_font =font_manager.FontProperties(fname="C:\Windows\Fonts\Arial")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

_x = list(x)[::3]
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# plt.xticks(_x, _xtick_labels[::3], rotation=45)
plt.xticks(_x, _xtick_labels[::3], rotation=45,fontproperties=my_font)

plt.show()
