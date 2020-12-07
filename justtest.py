import numpy as np
import matplotlib.pyplot as plt
import random
walk = np.random.normal(size=1000)  # 均值mean,标准差std,数量
# walk = []
# for _ in range(1000):
#     walk.append(random.normalvariate(0, 1))
plt.figure(1)
a=plt.hist(walk, 50)  # bins直方图的柱数
plt.show()
#print(a[0])
for i in walk:
    print(i)
