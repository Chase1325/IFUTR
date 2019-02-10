#Populate CSV Files in structured format with localization data

############################   LIBRARIES   ############################
import datetime

#CSV library
import csv as csv
import numpy as np

#Populate CSV with localization data
#Inputs: ({Pos.x, Pos.y, Pox.z}, anchor distance [mm], {true.x, true.y, true.z}, {mean, var, std, {err.x, err.y, err.z}})
def csv_handler(stats, anchorSpace, testLocale):
    date = datetime.datetime.now()

    fileName = ('{}_{}_{}_Anch-{}_Test-{}_{}_{}.csv').format(date.year,
                                                             date.month, date.day,
                                                             anchorSpace, testLocale[0],
                                                             testLocale[1],testLocale[2])
    path = 'ifutr/scripts/localization/reports/CSV/ungenerated/'

    #Statistics variables pulled for ease of use
    data = stats.getData()
    mean = stats.getMean()
    meanMag = stats.getMeanMag()
    var = stats.getVar()
    varMag = stats.getVarMag()
    std = stats.getStd()
    stdMag = stats.getStdMag()
    err = stats.getErr()
    errMag = stats.getErrMag()
    print('about to write csv')
    print(fileName)
    with open(path+fileName, 'w') as writeFile:
        #Make our writer
        print('Made CSV File')
        writer = csv.writer(writeFile)

        message = ['DataX', 'DataY', 'DataZ', 'TrueX', 'TrueY', 'TrueZ',
                   'MeanX', 'MeanY', 'MeanZ','Mean Mag', 'Var X', 'Var Y',
                   'Var Z', 'Var Mag', 'Std X', 'Std Y', 'Std Z', 'Std Mag',
                   'Err X', 'Err Y', 'Err Z', 'Err Mag']
        writer.writerow(message)

        #Write Statistical data
        print(testLocale[0])

        message = [data[0][0],data[1][0],data[2][0],
                   testLocale[0], testLocale[1], testLocale[2],
                   mean[0],mean[1],mean[2],meanMag,var[0],var[1],var[2],varMag,
                   std[0],std[1],std[2],stdMag,err[0],err[1],err[2],errMag]

        for i in range(len(data[0])):
            if(i==0):
                writer.writerow(message)
            else:
                writer.writerow([data[0][i],data[1][i],data[2][i]])
