
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd








# generate data

df = pd.read_csv('readme.csv')

data_array = np.array(df.iloc[:,:])


n_steps = 50
sigma=0.25
mu=0.5
T = np.linspace(-0, 1, n_steps)

# MADEUP DATASET
# data = {}
# data[0] = (T / 20 + 1 / (sigma * np.sqrt(2 * np.pi)) *  np.exp(-0.5 * ((T - mu) / sigma) ** 2))
# data[1] = (T / 20 + 1 / (sigma/2 * np.sqrt(2 * np.pi)) *  np.exp(-0.5 * ((T - mu*0.3) / sigma) ** 2))


# REAL DATASET
data = {}
data[0] = data_array[:,0]
data[1] = data_array[:,1]





# # plot
# ax = plt.axes(projection='3d')
# ax.plot3D(T, data[0], data[1], 'red')
# plt.show()
# print('done')


# remove points according to gradient < threshold

N = np.shape(data)


def plot3d(x,y,t, color, format):
    ax = plt.axes(projection='3d')
    if (format=='line'):
        ax = plt.axes(projection='3d')
        ax.plot3D(x,y,t, 'color')
    if (format=='dots'):
        ax.scatter3D(x,y,t, cmap='Greens');
    plt.show()






def computeNextConsecutiveGradient(data, firstIdx):
    x1 = data[0][firstIdx-1]
    y1 = data[1][firstIdx-1]
    x2 = data[0][firstIdx]
    y2 = data[1][firstIdx]
    dx = x2-x1
    dy = y2-y1
    grad =  dy/dx

    return np.abs(grad)





init = 0
filteredIdx=[]
filteredIdx.append(0)
counter = 0
i = 0








# fake
# threshold = 1.7
# max_skip = 0.12* n_steps




# generated
threshold = 2
max_skip = 0.15* n_steps


while(i < n_steps):


    r = computeNextConsecutiveGradient(data,i)
    checkpoint = i
    while(r < threshold and i < n_steps and  (i-checkpoint) < max_skip ): # evaluate gradient
        # grad is small, i.e. skip point
        i = i+1
        if (i < n_steps):
            r = computeNextConsecutiveGradient(data, i)

    if (i<n_steps):
        filteredIdx.append(i)
        i = i+1


    counter = counter +1
    print('counter: ' + str(counter))

filteredIdx.append((n_steps-1))
print(filteredIdx)
print('counter: ' + str(counter))


x_f = data[0][filteredIdx]
y_f = data[1][filteredIdx]

t_f = T[filteredIdx]

# plot3d(filtered_x1,filtered_x2,T_filtered, 'red', 'dots')




# PLOT 3D
# ax = plt.axes(projection='3d')
# ax.plot3D(data[0], data[1], T,'red')
# ax.scatter3D(x_f, y_f, t_f);

fig, (ax0) = plt.subplots(1, 1)

ax0.plot(data[0], data[1], c='red')


print("debu")
print(np.shape(t_f))
print(np.shape(y_f))

ax0.scatter(t_f, y_f, c='blue')




#PLOT 2D


plt.show()

print(np.shape(data[0]))
print(np.shape(x_f))







