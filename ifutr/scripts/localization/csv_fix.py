import localization_csv_handler
from localization_statistics2 import SampleStats
import tkFileDialog
import csv as csv


##file = tkFileDialog.askopenfilename()
#file = '/home/chase/catkin_ws/src/IFUTR/ifutr/scripts/localization/reports/CSV/ungenerated/2019_2_18_Anch-9000_Test-500_500_10.csv'
#file = 'reports/CSV/ungenerated/2019_2_18_Anch-9000_Test-500_500_10.csv'
file = tkFileDialog.askopenfilenames()

print(file)

for f in file:

    f = f[59:]
    print(f)
    data = [[],[],[]]
    line = 0
    anchorSpacing = 11000

    true =[]
    with open(f) as fileName:
        reader = csv.reader(fileName, delimiter=',')
        for row in reader:
            if(line>=2):
                data[0].append(int(row[0]))
                data[1].append(int(row[1]))
                data[2].append(int(row[2]))
                line+=1
            elif(line==1):
                true.append(int(row[3]))
                true.append(int(row[4]))
                true.append(int(row[5]))
                line+=1
            else:
                line+=1

    print('Processed {} lines'.format(line))
    print(len(data[0]))
    print('True' + str(true))
    print(data)

    #Find data statistics
    stats = SampleStats(data) #Make the class
    stats.setErr(true)

    localization_csv_handler.csv_handler(stats, anchorSpacing, true)
