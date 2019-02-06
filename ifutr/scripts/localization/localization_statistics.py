#Script for finding the statistics of localization data

#Math Tools
from itertools import product, combinations
import numpy as np
import math as math
import pandas as pd

class SampleStats:
    def __init__(self, data):
        self.data = [np.asarray(data.posx), np.asarray(data.posy), np.asarray(data.posz)]

        self.mean = [np.mean(self.data[0]), np.mean(self.data[1]), np.mean(self.data[2])]
        self.mean_mag = np.linalg.norm(self.mean)

        self.var = [np.var(self.data[0]), np.var(self.data[1]), np.var(self.data[2])]
        self.var_mag = np.linalg.norm(self.var)

        self.std = [np.std(self.data[0]), np.std(self.data[1]), np.std(self.data[2])]
        self.std_mag = np.linalg.norm(self.std)

        self.err = np.asarray([0, 0, 0])
        self.err_mag = 0

    def getData(self):
        return self.data

    def getMean(self):
        return self.mean

    def getMeanMag(self):
        return self.mean_mag

    def getVar(self):
        return self.var

    def getVarMag(self):
        return self.var_mag

    def getStd(self):
        return self.std

    def getStdMag(self):
        return self.std_mag

    def setErr(self, init):
        self.err = np.asarray([np.absolute(self.mean[0]-init[0]),
                               np.absolute(self.mean[1]-init[1]),
                               np.absolute(self.mean[2]-init[2])])
        self.err_mag = np.linalg.norm(self.err)

    def getErr(self):
        return self.err

    def getErrMag(self):
        return self.err_mag
