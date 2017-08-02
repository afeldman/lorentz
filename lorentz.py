#!/usr/bin/env python3

import numpy as np
from scipy import integrate

trajectories = 2
stepCnt = 1000000

def lorenz_attractor( x_y_z, t0, sigma=10.0, roh=28.0, beta=8./3.):
    x,y,z = x_y_z
    return [sigma*(y - x), roh*x - y - x*z, x*y - beta*z]

np.random.seed(1)
x0 = np.random.uniform(-15,15,(trajectories, 3))

t = np.linspace(0, 4, stepCnt)
x_t = np.asarray([integrate.odeint(lorenz_attractor, x0i, t)
                  for x0i in x0], dtype=np.float32)
