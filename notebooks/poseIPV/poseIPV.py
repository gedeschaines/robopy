#!/usr/bin/env python
# coding: utf-8

# **Demonstration of RoboPy Pose.plot() and SerialLink.plot() rendering capability using IPV (ipyvolume).**

# In[1]:


import os  # for checking values of environment variables.

""" Matplotlib imports
"""
import matplotlib
matplotlib.use('Qt4Agg')
get_ipython().run_line_magic('matplotlib', 'notebook')

""" RoboPy imports
"""
import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.pose as pose
import robopy.base.model as model


# In[2]:


# Select a Graphics Rendering package to use.

gobj = GraphicsRenderer('IPV')  # this sets graphics.gRenderer


# In[3]:


# Define some GraphicsVTK parameters whcich will be used in plot()
# method calls in following cells.

dMode = 'IPY'
limits = [-4.0, 4.0, -4.0, 4.0, -4.0, 4.0]


# In[4]:


# Plot SE3 pose using MPL and display below.

pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode=dMode, z_up=True, limits=limits)


# In[5]:


# Plot SE3 pose using VTK and display in PIL (Imagemagick) window

if 'BINDER_SERVICE_HOST' not in os.environ:
    # display this if not on MyBinder
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode='PIL', z_up=True, limits=limits)


# In[6]:


# Define a Puma506 robot model.
robot = model.Puma560()
    
# Puma560 manipulator arm pose plot using MPL and displayed below.
robot.plot(robot.qn, dispMode=dMode, z_up=False, limits=None)


# In[7]:


# Puma560 manipulator arm pose plot using MPL and displayed in PIL (Imagemagick) window

if 'BINDER_SERVICE_HOST' not in os.environ:
    # display this if not on MyBinder
    robot.plot(robot.qn, dispMode='PIL', z_up=False, limits=None)


# In[8]:


# Puma560 animation

import numpy as np

a = np.transpose(np.asmatrix(np.linspace(1, -180, 500)))
b = np.transpose(np.asmatrix(np.linspace(1, 180, 500)))
c = np.transpose(np.asmatrix(np.linspace(1, 90, 500)))
d = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))
e = np.asmatrix(np.zeros((500, 1)))
f = np.concatenate((d, b, a, e, c, d), axis=1)

# Give graphics renderer pose DisplayList to animate for all 500 poses.
#
# Note: There may be a considerable delay while all figures are generated 
#       before being passed to animation_control (noticeable here).

gIpv = GraphicsRenderer('IPV')  # sets graphics.gRenderer (to clear previous figure)
robot.animate(stances=f, unit='deg', timer_rate=60, gif="Puma560", 
                         frame_rate=30, dispMode='IPY', limits=None)


# In[ ]:




