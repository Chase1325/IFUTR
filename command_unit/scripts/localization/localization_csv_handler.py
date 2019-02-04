#Populate CSV Files in structured format with localization data

############################   LIBRARIES   ############################
import datetime

#CSV library
import csv as csv

#Populate CSV with localization data
#Inputs: ({Pos.x, Pos.y, Pox.z}, anchor distance [mm], {true.x, true.y, true.z}, {mean, var, std, {err.x, err.y, err.z}})
def csv_handler(data, anchorSpace, testLocale, stats):
    date = datetime.datetime.now()

    fileName = ('{}_{}_{}_Anch={}_Test={}_{}_{}.csv').format(date.year,
                                                             date.month, date.day,
                                                             anchorSpace, testLocale[0],
                                                             testLocale[1],testLocale[2])

    with open(fileName, 'w') as writeFile:
        writer = csv.writer(writeFile)

        #Make Headers
        writer.writerow("True X, True Y, True Z, Mean X, Mean Y, Mean Z, Mean Mag, Var X, Var Y, Var Z, Var Mag, Std X, Std Y, Std Z, Std Mag, Err X, Err Y, Err Z, Err Mag")
