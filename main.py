import tgi
import time
import numpy as np
import matplotlib.pyplot as plt

mytgi = tgi.newTGI(MDmode=False)

arr = np.array([[5], [10], [20], [40]])


# mytgi.plotLines("li", np.array([[0, 0], [1, 2], [2, 4]]))
# mytgi.plotLines("li", [0, 0, 1, 2, 2, 4])
# mytgi.update()
# time.sleep(5)
li = []
# sval = 0
# while sval <= 5:
r = 0
#     tmp2 = []
while r <= 4.1:
    # val = sval
    val = 0.6
    x = 0
    tmp = []
    while x <= 28:
        val = r*val*(1-val)
        # if val != float("inf") and val != float("-inf") and val < 10000.0 and val > -10000.0:
        if val != float("inf") and val != float("-inf") and val < 2.0 and val > -2.0:
            if not (val in tmp):
                tmp.append(val)
        x += 1
    r += 0.00001
    li.append(tmp)
    # sval += 0.1
    # li.append(tmp2)

# print(li)
liput = [[], [], []]

# for x in range(len(li)):
#     for y in range(len(li[x])):
#         for z in range(len(li[x][y])):
#             liput[0].append(x)
#             liput[1].append(y)
#             liput[2].append(li[x][y][z])
for x in range(len(li)):
    for y in range(len(li[x])):
            liput[0].append(x)
            liput[1].append(li[x][y])
# print(li)

mytgi.plotDots2D("equation", liput)

while True:
    mytgi.update()
    time.sleep(0.1)

# fig = plt.figure()
# field = fig.add_subplot()

# fig.set_facecolor((0, 0, 0))
# field.set_facecolor((0, 0, 0))

# field.plot(arr)
# fig.show()
# time.sleep(5)