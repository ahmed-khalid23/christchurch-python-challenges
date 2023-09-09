import numpy as np
import matplotlib.pyplot as plt

def plot(x, y, color='blue'):
    plt.figure()
    plt.plot(x, y, color)
    plt.axis('equal')
    plt.axis('off')

def circle(r=1, color='blue'):
    # r specifies radius of circle
    t_values = np.linspace(0, 2*np.pi, 200000)
    x_list = r * np.cos(t_values)
    y_list = r * np.sin(t_values) 
    plot(x_list, y_list, color)
    plt.xlim(-(r + 5), r + 5)
    plt.ylim(-(r + 5), r + 5)


def fermat_spiral():
    t = np.linspace(0, 50, 20000)
    x_pos = t ** 0.5 * np.cos(t)
    y_pos = t ** 0.5 * np.sin(t)
    x_neg = (-t ** 0.5) * np.cos(t)
    y_neg = (-t ** 0.5) * np.sin(t)
    x = np.concatenate((x_pos[::-1], x_neg))
    y = np.concatenate((y_pos[::-1], y_neg))
    plot(x, y)


def butterfly_curve():
    t = np.linspace(0, 12*np.pi, 200000)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12) ** 5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12) ** 5)
    plot(x, y)


circle(0.5, 'orange')
circle(1, 'pink')
circle(5, 'green')
circle(50, 'red')
circle(500, 'black')
plt.show()
