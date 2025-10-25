import numpy as np
import matplotlib.pyplot as plt

"""
Describes nozzle calculations pertaining to geometry of nozzles, involving 
converging, diverging and throat sections.

Takes necessary r values, z and converts to cartesian coordinates
"""

def nozzle_envelope_diverging(rt, re,z,l):
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

    return (rt - (re - rt)*(z/l)**2)

def total_nozzle(rt,re,rc,z,l):
    
    a = nozzlecalculations.nozzle_envelope_converging(rt,rc,z,l)
    b = nozzlecalculations.nozzle_envelope_diverging(rt,re,z,l)

    return a,b

def nozzle_to_cartesian()




    



