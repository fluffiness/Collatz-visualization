import matplotlib.pyplot as plt
import numpy as np

def collatz(init: int):
    sequence = [init]
    while init != 1:
        if (init % 2) == 0:
            init = init / 2
        else:
            init = 3 * init + 1
        sequence.append(init)
    return sequence

def collatz_curve(init: int, decay_rate: float):
    curve = [0 + 0j]
    n_iter = 0
    angle = 0
    while init != 1:
        if (init % 2) == 0:
            init = init / 2
            angle = angle - 8
            next = curve[-1] + np.exp(np.deg2rad(angle) * 1j) * (decay_rate ** n_iter)
            curve.append(next)
        else:
            init = 3 * init + 1
            angle = angle + 12
            next = curve[-1] + np.exp(np.deg2rad(angle) * 1j) * (decay_rate ** n_iter)
            curve.append(next)
        n_iter += 1
    return curve

n_inits = 1000
lower = 0
upper = 10000
decay_rate = 0.97
rng = np.random.default_rng()
inits = rng.integers(lower, high=upper, size=n_inits)

for i in inits:
    curve = np.array(collatz_curve(i, decay_rate))
    x, y = curve.real, curve.imag
    plt.plot(x, y, 'b', linewidth=0.1)

plt.axis('equal')
plt.show()

