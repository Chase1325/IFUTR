###############################################################################
#Chase St. Laurent
#Worcester Polytechnic Institute
#IPAS-ROS Project
#
#MASTER Command Node
################################################################################

#ROS Imports
import rospy
from localize_service.srv import localize_service


def run_Localize():
    while(rospy.get_param('/lightswitch')=='on'):

        #If we set sample to true, begin a new localization test
        if(rospy.get_param('/sample')==True):
            rospy.set_param('/samle', False) #Reset the parameter to avoid loop

            sampleCount = 100
            rospy.wait_for_service('localize_service')
            localizeService = rospy.ServiceProxy('localize_service', localize_service)
            localizeData = localizeService(sampleCount) #Call service from UAV, stored as tuple of arrays

            #localizeData = {localizeData.posx, localizeData.posy, localizeData.posz}

            #Then call function from localization report and pass in data
            #Data: LocalizeData, AnchorPositions, TestLocation

        else:
            time.sleep(1) #Sleep while waiting


def initialize():
    rospy.init_node('command_unit', anonymous=False)

def run():
    #System Mode ('IPAS', 'Localize', 'Flight_Test', 'Ground_Test')
    mode = rospy.get_param('/mode')

    if(mode=='IPAS'):
        #Run IPAS Algorithm
        pass
    elif(mode=='Localize'):
        run_Localize()
    elif(mode=='Flight_Test'):
        #Run Flight Test
        pass
    elif(mode=='Ground_Test'):
        #Run Ground Test
        pass
    else:
        print('Failed to initialize')

if __name__ == "__main__":

    initialize()
    run()
