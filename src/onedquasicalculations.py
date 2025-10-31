import numpy as np
import math

"""
Physical Constants
"""

R = 287.05  # Specific gas constant for air in J/(kg·K)
gamma_air = 1.4  # Specific heat ratio for air


def massflowrate(gamma,throata,stagp,stagt):
    """
    Calculate the mass flow rate through a nozzle.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    throata : float
        Throat area of the nozzle (m^2).
    stagp : float
        Stagnation pressure (Pa).
    stagt : float
        Stagnation temperature (K).

    Returns:
    float
        Mass flow rate (kg/s).
    """
    
    term1 = (gamma / (R * stagt)) ** 0.5
    term2 = stagp * throata
    term3 = ((2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1))))
    
    mfr = term1 * term2 * term3
    return mfr

"""
Mach Isentropic Relations

"""

def pressure(gamma, mach, stagp):
    """
    Calculate the static pressure from stagnation pressure and Mach number.

    Parameters: 
    gamma : float
        Specific heat ratio of the gas.
    mach : float
        Mach number.
    stagp : float
        Stagnation pressure (Pa).
    Returns:
    float
        Pressure (Pa).
    """

    pressure = stagp * (1 + ((gamma - 1) / 2) * mach ** 2) ** (-gamma / (gamma - 1))
    return pressure

def density(gamma, mach, stagr, stagt):
    """
    Calculate the static density from stagnation density, stagnation temperature, and Mach number.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach : float
        Mach number.
    stagr : float
        Stagnation density (kg/m^3).
    stagt : float
        Stagnation temperature (K).

    Returns:
    float
        Density (kg/m^3).
    """

    density = stagr * (1 + ((gamma - 1) / 2) * mach ** 2) ** (-1 / (gamma - 1))
    return density

def temperature(gamma, mach, stagt):
    """
    Calculate the static temperature from stagnation temperature and Mach number.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach : float
        Mach number.
    stagt : float
        Stagnation temperature (K).
    Returns:
    float
        Temperature (K).
    """
    temperature = stagt * (1 + ((gamma - 1) / 2) * mach ** 2) ** -1
    return temperature

def velocity(gamma, mach, stagt):
    """ 
    Calculate the velocity from Mach number and stagnation temperature.
    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach : float
        Mach number.
    stagt : float
        Stagnation temperature (K).
    Returns:
    float
        Velocity (m/s).
    """
    velocity = mach * (gamma * R * stagt) ** 0.5
    return velocity

def area_velocity_relation(gamma, mach, area_ratio):
    """
    Calculate the Mach number from area ratio using isentropic flow relations.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach : float
        Initial guess for Mach number.
    area_ratio : float
        Area ratio (A/A*).

    Returns:
    float
        Mach number.
    """
    func = lambda m: (1 / m) * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * m ** 2)) ** ((gamma + 1) / (2 * (gamma - 1))) - area_ratio
    mach_solution = np.roots([((gamma + 1) / (2 * (gamma - 1))), 0, 0, 0, (1 - area_ratio * m)])
    mach_real = [m.real for m in mach_solution if m.imag == 0 and m.real > 0]
    return mach_real[0] if mach_real else None

def area_mach_relation(gamma, mach, throata):
    """
    Calculate the area ratio (A/A*) from Mach number using isentropic flow relations.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach : float
        Mach number.
    throata : float
        Throat area (m^2).

    Returns:
    float
        Area ratio (A/A*).
    """
    area_ratio = (1 / mach) * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * mach ** 2)) ** ((gamma + 1) / (2 * (gamma - 1)))
    area = area_ratio * throata
    return area

def throat_area(mass_flow_rate, stagp, stagt, gamma):
    """
    Calculate the throat area of a nozzle given mass flow rate, stagnation pressure, stagnation temperature, and specific heat ratio.

    Parameters:
    mass_flow_rate : float
        Mass flow rate (kg/s).
    stagp : float
        Stagnation pressure (Pa).
    stagt : float
        Stagnation temperature (K).
    gamma : float
        Specific heat ratio of the gas.

    Returns:
    float
        Throat area (m^2).
    """
    term1 = mass_flow_rate / ((gamma / (R * stagt)) ** 0.5 * stagp)
    term2 = ((2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1))))
    throata = term1 / term2 
    return throata
"""
Normal Shock Relations
"""

def normal_shock_pressure_ratio(gamma, mach1):
    """
    Calculate the pressure ratio across a normal shock.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach1 : float
        Mach number before the shock.

    Returns:
    float
        Pressure ratio (P2/P1).
    """
    pratio = 1 + (2 * gamma / (gamma + 1)) * (mach1 ** 2 - 1)
    return pratio
def normal_shock_mach2(gamma, mach1):
    """
    Calculate the Mach number after a normal shock.
    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach1 : float
        Mach number before the shock.
    Returns:
    float
        Mach number after the shock.
    """
    mach2 = ((1 + ((gamma - 1) / 2) * mach1 ** 2) / (gamma * mach1 ** 2 - (gamma - 1) / 2)) ** 0.5
    return mach2

def normal_shock_mach1(gamma, mach2):
    """
    Calculate the Mach number before a normal shock.
    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach2 : float
        Mach number after the shock.
    Returns:
    float
        Mach number before the shock.
    """
    mach1 = (( (gamma - 1) * mach2 ** 2 + 2) / (2 * gamma * mach2 ** 2 - (gamma - 1))) ** 0.5
    return mach1

def normal_shock_density_ratio(gamma, mach1):
    """
    Calculate the density ratio across a normal shock.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach1 : float
        Mach number before the shock.

    Returns:
    float
        Density ratio (rho2/rho1).
    """
    dratio = ((gamma + 1) * mach1 ** 2) / ((gamma - 1) * mach1 ** 2 + 2)
    return dratio
def normal_shock_temperature_ratio(gamma, mach1):
    """
    Calculate the temperature ratio across a normal shock.
    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach1 : float
    Mach number before the shock.
    Returns:
    float
        Temperature ratio (T2/T1).
    """
    tratio = normal_shock_pressure_ratio(gamma, mach1) / normal_shock_density_ratio(gamma, mach1)
    return tratio
def normal_shock_pressure_ratio(gamma, mach1):
    """
    Calculate the pressure ratio across a normal shock.

    Parameters:
    gamma : float
        Specific heat ratio of the gas.
    mach1 : float
        Mach number before the shock.

    Returns:
    float
        Pressure ratio (P2/P1).
    """
    pratio = 1 + (2 * gamma / (gamma + 1)) * (mach1 ** 2 - 1)
    return pratio
