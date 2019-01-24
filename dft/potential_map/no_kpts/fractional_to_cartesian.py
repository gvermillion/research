import numpy as np
import os,sys

def get_fractional_to_cartesian_matrix(a, b, c, alpha, beta, gamma, angle_in_degrees=True):
    """
    Return the transformation matrix that converts fractional coordinates to
    cartesian coordinates.

    Parameters
    ----------
    a, b, c : float
        The lengths of the edges.
    alpha, gamma, beta : float
        The angles between the sides.
    angle_in_degrees : bool
        True if alpha, beta and gamma are expressed in degrees.

    Returns
    -------
    r : array_like
        The 3x3 rotation matrix. ``V_cart = np.dot(r, V_frac)``.
    
    Source
    ------

    https://gist.githubusercontent.com/Bismarrck/a68da01f19b39320f78a/raw/45430f73fba90e9f1a73c9982adb6991276d09e0/frac_cart.py

    """
    if angle_in_degrees:
        alpha = np.deg2rad(alpha)
        beta = np.deg2rad(beta)
        gamma = np.deg2rad(gamma)
    cosa = np.cos(alpha)
    sina = np.sin(alpha)
    cosb = np.cos(beta)
    sinb = np.sin(beta)
    cosg = np.cos(gamma)
    sing = np.sin(gamma)
    volume = 1.0 - cosa**2.0 - cosb**2.0 - cosg**2.0 + 2.0 * cosa * cosb * cosg
    volume = np.sqrt(volume)
    r = np.zeros((3, 3))
    r[0, 0] = a
    r[0, 1] = b * cosg
    r[0, 2] = c * cosb
    r[1, 1] = b * sing
    r[1, 2] = c * (cosa - cosb * cosg) / sing
    r[2, 2] = c * volume / sing
    return r

a = 9.20800018
b = 9.20800018
c = 9.18799973

alpha = 90
beta = 90
gamma = 120

r = get_fractional_to_cartesian_matrix(a,b,c,alpha,beta,gamma)

frac = np.array([0,0,0])
cart = r*frac

print(cart)
