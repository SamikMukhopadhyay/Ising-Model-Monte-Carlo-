import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

row_num = 100
col_num = 100
num_steps = 10000


def Energy(arr,i,j):
    E = arr[i][j]*(arr[(i-1) % row_num][j] + arr[(i+1) % row_num][j] + arr[i][(j-1) % col_num] + arr[i][(j+1) % col_num])
    return E

def TotalEnergy(arr):
    En = 0
    for i in range(row_num):
        for j in range(col_num) :
            En += Energy(arr, i, j)
    return En

def initial(row_num, col_num):
    arr = 2*np.random.randint(0, 2,(row_num, col_num), int)  - np.ones((row_num, col_num), int)
    return arr

def calcmagnet(arr):
    return np.sum(arr) 

def sample(latt, num_steps, beta) :
    for k in range(num_steps):
        i = np.random.randint(0,row_num)
        j = np.random.randint(0,col_num)
        energy = Energy(latt, i, j)
        if energy < 0 :
            latt[i][j] *= -1
        elif np.random.rand() < np.exp(-2*energy*beta) :
            latt[i][j] *= -1
    return latt

def simulate(latt, T)  :
    fig = plt.figure()
    ax = plt.axes(autoscale_on = True)
    X, Y = np.meshgrid(range(row_num), range(col_num))
    plt.xlabel('Units in X axis')
    plt.ylabel('Units in Y axis')
    plt.title('2-D Ising Model using Metropolis Steps')

    def init() :
        mesh = plt.pcolormesh(X, Y, latt, cmap = plt.cm.RdBu, shading = 'auto')
        
    def update(frame) :
        sample(latt, num_steps,1/T)
        mesh = plt.pcolormesh(X, Y, latt, cmap = plt.cm.RdBu, shading = 'auto')

    anim = animation.FuncAnimation(fig, update, init_func = init(), frames = 500, interval = 5)
    '''plt.pcolormesh(X, Y, latt, cmap = plt.cm.Blues, shading = 'auto')'''
    plt.show()


if __name__  ==  '__main__':
    latt = initial(row_num, col_num)
    #anim = animation.FuncAnimation(fig, simulate, frames = 100)
    T = 1.5
    simulate(latt, T)
    
        



    
