#Generate a PDF report from Localization Tests

############################   LIBRARIES   ############################
#CSV library
import csv as csv

#Math Tools
from itertools import product, combinations
import numpy as np
import math as math
import pandas as pd

#Matplot Libraries for Graphics and PDF generation
import matplotlib as m
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from matplotlib.backends.backend_pdf import PdfPages as pdf
import matplotlib.style

#Shapely Graphic Libraries
from shapely.geometry.point import Point
from shapely import affinity
