import numpy as np
import matplotlib.pyplot as plt

"""
Describes nozzle calculations pertaining to geometry of nozzles, involving 
converging, diverging and throat sections.

Takes necessary r values, z and converts to cartesian coordinates
"""

def nozzle_envelope_diverging(rt,re,z,l):
    """
    Takes throat radius, exhaust radius, length of diverging section
    to calculate envelope that diverging nozzle section follows (R(z))
    parameters:
    rt (float) : throat radius
    re (float) : exhaust radius
    z (float) : z distance from throat
    l (float) : length of diverging section
    """

    return (rt + (re - rt)*(z/l)**2)

def nozzle_envelope_converging(rt,rc,z,l):
  
  
    """
    Takes throat radius, chamer radius, length of diverging section
    to calculate envelope that diverging nozzle section follows (R(z))
    parameters:
    rt (float) : throat radius
    re (float) : chamber radius
    z (float) : z distance from throat
    l (float) : length of diverging section
    """

    s = np.asarray(z) / l  # 0 → 1
    r = rc - (rc - rt) * s**2
    return np.clip(r, 0.0, None)  # avoid negative radius if inputs are extreme

def total_nozzle(rt,re,rc,z,l):
    
    a = nozzlecalculations.nozzle_envelope_converging(rt,rc,z,l)
    b = nozzlecalculations.nozzle_envelope_diverging(rt,re,z,l)

    return a,b

def nozzle_to_cartesian(rt, rc, re, l_converging, l_diverging, n_theta=50, n_z=100):
    """
    Converts the converging and diverging nozzle envelope radii into
    full 3D Cartesian coordinates (X, Y, Z).

    Parameters:
    rt : float
        Throat radius
    rc : float
        Chamber radius
    re : float
        Exit radius
    l_converging : float
        Length of converging section
    l_diverging : float
        Length of diverging section
    n_theta : int, optional
        Number of angular divisions around the axis (default 50)
    n_z : int, optional
        Number of points along z in each section (default 100)

    Returns:
    X, Y, Z : np.ndarray
        Cartesian coordinate arrays for the full nozzle surface.
    """

    # Create z arrays for each section
    z_conv = np.linspace(-l_converging, 0, n_z)
    z_div = np.linspace(0, l_diverging, n_z)
    
    # Get corresponding radius profiles
    r_conv = nozzle_envelope_converging(rt, rc, z_conv + l_converging, l_converging)
    r_div = nozzle_envelope_diverging(rt, re, z_div, l_diverging)

    # Combine the two sections into one continuous profile
    z_full = np.concatenate((z_conv, z_div))
    r_full = np.concatenate((r_conv, r_div))

    # Create angular coordinates
    theta = np.linspace(0, 2*np.pi, n_theta)

    # Meshgrid for surface revolution
    Z, TH = np.meshgrid(z_full, theta)
    R = np.tile(r_full, (n_theta, 1))

    # Convert to Cartesian coordinates
    X = R * np.cos(TH)
    Y = R * np.sin(TH)

    return X, Y, Z

    





    



