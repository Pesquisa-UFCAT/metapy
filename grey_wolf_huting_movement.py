"""Grey Wolf Hunting Movement function."""
""""""
from benchmark import sphere as sp
from benchmark import rosenbrock as ros
from benchmark import rastrigin as ras
from benchmark import ackley as ack
from benchmark import griewank as gri
from benchmark import zakharov as zak
from benchmark import easom as eas
from benchmark import michalewicz as mic
from benchmark import dixon_price as dix
from benchmark import goldstein_price as gol
from benchmark import powell as powe
from benchmark import *
import random

vector = [0]*33
n_s = 10
d = 2
x_lower = [0, 0]
x_upper = [5, 5]
fun=[sp,ros,ras,ack,gri,zak,eas,mic,dix,powe,gol]
dic={sp:0,ros:1,ras:2,ack:3,gri:4,zak:5,eas:6,mic:7,dix:8,powe:9,gol:10}

def grey_wolf_huting_movement_(of_function,x_alpha, x_beta,x_delta,x_current, t, T, d) :
    """
    Grey Wolf Hunting Movement
    :param fun: The objective function to be minimized##
    :param x_alpha: Position of the best wolf at the previous iteration
    :param x_beta: Position of the second best wolf at the previous iteration
    :param x_delta: Position of the third best wolf at the previous iteration
    :param x_current: Position of the current wolf
    :param t: Current iteration
    :param T: Total number of iterations
    :param d: Dimension of the search space

    :return: New position of the current wolf
    """
    a=2*(1-t/T)
    A=2*a*np.random.rand()-a
    C=2*np.random.rand()
    D_alpha=x_alpha.copy()
    D_beta=x_beta.copy()
    D_delta=x_delta.copy()
    for i in range(D_alpha.__len__()):
        D_alpha[i]=abs(C*x_alpha[i]-x_current[i])
    A=2*a*np.random.rand()-a
    C=2*np.random.rand()
    for i in range(D_beta.__len__()):
        D_beta[i]=abs(C*x_beta[i]-x_current[i])
    A=2*a*np.random.rand()-a
    C=2*np.random.rand()
    for i in range(D_delta.__len__()):
        D_delta[i]=abs(C*x_delta[i]-x_current[i])
    x_new=x_current.copy()
    X1=x_alpha.copy()
    X2=x_beta.copy()
    X3=x_delta.copy()
    for i in range(D_alpha.__len__()):
        A=2*a*np.random.rand()-a
        X1[i]=x_alpha[i]+A*D_alpha[i]
        A=2*a*np.random.rand()-a
        X2[i]=x_beta[i]+A*D_beta[i]
        A=2*a*np.random.rand()-a
        X3[i]=x_delta[i]+A*D_delta[i]
    for i in range(D_alpha.__len__()):
        x_new[i]=(X1[i]+X2[i]+X3[i])/3
    x_current[:]=x_new
    print()
    print(of_function(x_alpha),of_function(x_new))
    if(of_function(x_alpha)>of_function(x_new)):
        x_alpha[:]=x_new
    elif(of_function(x_beta)>of_function(x_new)):
        x_beta[:]=x_new
    elif(of_function(x_delta)>of_function(x_new)):
        x_delta[:]=x_new
    print(of_function(x_alpha),of_function(x_new))
    return x_new
