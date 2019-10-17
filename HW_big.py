import numpy as np
import TM.config as cnf
from matplotlib import pyplot as plt


def vector_X():
    x = np.arange(start=0, stop=4.0001, step=0.0001, dtype=float)
    return x
x = vector_X()
def Y_x():
    y = cnf.A * np.sin(cnf.om * x + cnf.theta_0)
    v_m, r = vp_max()
    v = np.minimum(v_m, cnf.v_max)
    S = 0
    for i in range(len(v) - 1):
        delta_v = (v[i+1] - v[i])/2
        delta_x = x[i+1] - x[i]
        if delta_v!= 0 :
            delta_t = delta_x/delta_v
        else:
            delta_t = 0
        S = S + delta_t
    print(S)
    #plt.plot(x, y)
    #plt.legend(["trajectory Y(x)"])
    #plt.xlabel('x space [0..4]')
    #plt.ylabel('Y space, depend on x')
    #plt.show()
    #return Y_x()

def v_x_best():

    v = np.minimum(vp_max(), cnf.v_max)
    print(vp_max())
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax.plot(vector_X(), v,  color="C0")
    ax.set_xlabel("x label 1", color="C0")
    ax.set_ylabel("y label 1", color="C0")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C0")


    plt.show()
   # min(cnf.v_max,
def vp_max():
    y_dot = cnf.om * cnf.A * np.cos(cnf.om * x + cnf.theta_0)
    y_dot_dot = -cnf.om * cnf.om * cnf.A * np.sin(cnf.om * x + cnf.theta_0)
    verh = np.power((1.0 + (y_dot * y_dot)), 1.5)
    niz = np.abs(y_dot_dot)
    r = verh/niz
    treck = np.sqrt(r*cnf.a_n_max)

    return treck, r

def Y_t():
    pass
def v_t():
   pass
def a_t():
    pass
def a_n():
    pass

Y_x()
#v_t()