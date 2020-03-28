import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

pxB = np.array ([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 12, 13,
                  14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14])
pyB = np.array ([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                  2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                  10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
pzB = np.array ([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
pB = np.array ([ pxB, pyB, pzB ])
pA = np.copy(pB)

fig = plt.figure ()
ax = fig.add_subplot (111 , projection ='3d')

ax.plot(pB[0],pB[1],pB[2],'.')
ax.plot(pA[0],pA[1],pA[2],'.')
