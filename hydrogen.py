import numpy as np
def load_hydrogen_spectrum():
    spectrum = [
        269.6119,
        272.3191,
        318.7745,
        358.7270,
        370.5005,
        587.5621,
        706.5190,
        1091.292,
        1278.479 
    ]
    intensities = [
        1,
        1,
        5,
        1,
        2,
        10,
        2,
        5,
        2
    ]
    c = 3e8
    xs = np.linspace(200, 1300, 3000)
    ys = np.zeros(xs.shape)
    for i, l in zip(intensities, spectrum):
        ys += i* np.exp(-(xs-l) * (xs - l)/(2 * 40 + np.random.uniform(10)))
    
    ys += np.random.normal(0, 0.3, ys.shape)
    ys += np.exp(-(xs-400)*(xs-400)/(500**2))
    ys += np.exp(-(xs-780)*(xs-780)/(300**2))
    return xs, ys
