# import matplotlib.pyplot as plt

# plt.plot([0,2,6,7,8,9],[1,2,3,4,5,6])
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.axis([-1,10,0,7])
# plt.show()

import matplotlib.pyplot  as  plt
import numpy as np
from random import choice

num_all = []
index = 1.5
rgb = ['b','g','r','c','m']
for i in range(5):
    a = np.arange(10)
    plt.plot(a,a*index,choice(rgb))
    index += 1
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


