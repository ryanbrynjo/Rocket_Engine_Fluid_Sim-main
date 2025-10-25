import matplotlib as plt
import numpy as np
import calculations as calc
import math







"""
Initialize 3D Plot Grid

"""

def init_3d_plot_grid(xlabel, ylabel, zlabel, title):
    """
    Initialize a 3D plot grid with specified labels and title.

    Parameters:
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.
    zlabel : str
        Label for the z-axis.
    title : str
        Title of the plot.
    Returns:
    fig : matplotlib.figure.Figure
        The created figure object.
    ax : matplotlib.axes._subplots.Axes3DSubplot
        The created 3D axes object.
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    return fig, ax

def plot_nozzle_cross_section(ax, x, y, z, color='b', alpha=0.5):
    """
    Plot a nozzle cross-section in 3D.

    Parameters:
    ax : matplotlib.axes._subplots.Axes3DSubplot
        The 3D axes object to plot on.
    x : array-like
        X coordinates of the nozzle cross-section.
    y : array-like
        Y coordinates of the nozzle cross-section.
    z : array-like
        Z coordinates of the nozzle cross-section.
    color : str, optional
        Color of the cross-section (default is 'b' for blue).
    alpha : float, optional
        Transparency level of the cross-section (default is 0.5).
    """

    ax.plot_trisurf(x, y, z, color=color, alpha=alpha)



    