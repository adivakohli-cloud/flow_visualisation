Flow Visualization Using Python

This project provides an interactive and modular framework to visualize 2D flow fields using different flow
types such as vortex, uniform, source, and doublet flows. It also supports user-defined velocity fields, 
and allows visualization of streamlines, pathlines, and streaklines, along with checking whether the flow
is rotational or irrotational.

Overview

Fluid flow visualization helps understand how particles move within a velocity field.
This program numerically simulates and plots three key flow representations:
Streamlines: Instantaneous flow direction at each point.
Pathlines: Trajectories of individual particles over time.
Streaklines: Locus of all particles that have passed through a specific point.
Additionally, it calculates the vorticity at a given point to determine whether the flow is rotational or
irrotational.

Features

Predefined flow types:
Vortex Flow – Rotational circular motion around origin.
Uniform Flow – Constant velocity field.
Source Flow – Radial flow outward from a point.
Doublet Flow – Flow resembling a combination of source and sink.
Custom Flow Input — Define your own u(x, y) and v(x, y) using Python/numpy syntax.
The code is robust enough to handle discontinuities in custom functions entered by the user for u(x,y) and
v(x,y), avoiding runtime overheads by making appropriate computational approximations at the concerned points.

Visualizations:
Streamlines (plot_streamlines())
Pathlines (plot_pathlines())
Streaklines (plot_streaklines())

Rotational Check: Estimates local vorticity numerically using finite differences.

Functions Summary

Function	        Description
vortex_flow(x, y)	Returns velocity components for a vortex flow.
uniform_flow(x, y)	Returns a uniform velocity field.
source_flow(x, y)	Models a point source emitting fluid radially.
doublet_flow(x, y)	Represents the superposition of a source and a sink.
plot_streamlines()	Generates a streamline plot of the velocity field.
plot_pathlines()	Simulates particle trajectories through the flow.
plot_streaklines()	Shows the streakline evolution over time from a release point.
check_rotational()	Numerically computes vorticity to check flow rotation.
get_custom_flow()	Prompts the user for symbolic u(x, y) and v(x, y) expressions and converts them to callable functions.

How to Run

Install dependencies:
pip install numpy matplotlib sympy

Run the script:
python flow_visualization.py

Choose a flow type (1–5) from the menu.

For custom flows, enter your own velocity components (e.g. u = -y, v = x).

Output Explanation

Streamlines show instantaneous flow structure.
Pathlines depict trajectories of moving particles.
Streaklines show how fluid released from a point evolves with time.
Vorticity value is printed in the console to classify the flow.

Conceptual Significance

This project bridges fluid mechanics theory and computational visualization by illustrating:
The geometric meaning of flow lines.
Particle motion interpretation.
Relationship between vorticity and flow rotation.
Analytical and graphical understanding of classical potential flows.

Dependencies:
NumPy
Matplotlib
SymPy

Author: 
Adiva Kohli

A Python-based exploration project on flow visualisation concepts for computational fluid mechanics.

