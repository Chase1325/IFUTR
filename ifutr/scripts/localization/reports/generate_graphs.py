import csv as csv
import matplotlib as m
import pandas as pd
import math as math
from matplotlib.backends.backend_pdf import PdfPages as pdf
import datetime
import tkFileDialog
from generate_DataMap import dataMap
from generate_Heat import heat
from generate_Table import dataTable




class SampleData(object):

    #Initialize by populating a sample with data and stats from file
    def __init__(self, file):

        self.data = [[],[],[]]
        self.true = []
        self.mean = []
        self.var = []
        self.std = []
        self.err = []

        with open(file) as fileName:
            reader = csv.reader(fileName, delimiter=',')
            line=0
            for row in reader:
                if(line>=2):
                    self.data[0].append(float(row[0]))
                    self.data[1].append(float(row[1]))
                    self.data[2].append(float(row[2]))
                    line+=1
                elif(line==1):
                    self.data[0].append(float(row[0]))
                    self.data[1].append(float(row[1]))
                    self.data[2].append(float(row[2]))
                    self.true.append(int(row[3]))
                    self.true.append(int(row[4]))
                    if(int(row[5])==10):
                        self.true.append(100)
                    else:
                        self.true.append(int(row[5]))
                    self.mean.append(float(row[6]))
                    self.mean.append(float(row[7]))
                    self.mean.append(float(row[8]))
                    self.mean.append(float(row[9])) #Mag value
                    self.var.append(float(row[10]))
                    self.var.append(float(row[11]))
                    self.var.append(float(row[12]))
                    self.var.append(float(row[13])) #Mag value
                    self.std.append(float(row[14]))
                    self.std.append(float(row[15]))
                    self.std.append(float(row[16]))
                    self.std.append(float(row[17])) #Mag value
                    self.err.append(float(row[18]))
                    self.err.append(float(row[19]))
                    self.err.append(float(row[20]))
                    self.err.append(float(row[21])) #Mag Value of XYZ... needs to be fixed
                    line+=1
                else:
                    line+=1

    def getData(self):
        return self.data

    def getTrue(self):
        return self.true

    def getMean(self):
        return self.mean

    def getVar(self):
        return self.var

    def getStd(self):
        return self.std

    def getErr(self):
        return self.err


#Setup PDF File Info
spacing=11000
date = datetime.datetime.now()
path = 'PDF/'
file='{}_{}_{}_AnchorSpacing-{}.pdf'.format(date.year, date.month, date.day, spacing)
page = pdf(path + file)

#Ask to select relevant files
file = tkFileDialog.askopenfilenames()

#Lump SampleData class into a list for entire anchor configuration
samples = []
for f in file:
    s = SampleData(f)
    samples.append(s)

dataMap_Figs = dataMap(samples, spacing) #Plot data points, standard deviations, errorbar
heat_Figs = heat(samples, spacing) #Generate error and variance heat meaps
tables = dataTable(samples) #Genearte control sample, inner perimeter, outer perimeter, and overall performance tables
for fig in dataMap_Figs:
    fig.savefig(page, format='pdf')
for fig in heat_Figs:
    fig.savefig(page, format='pdf')
for table in tables:
    table.savefig(page, format='pdf')

page.close()
