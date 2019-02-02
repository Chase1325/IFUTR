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

def initialize():
    rospy.init_node('command_unit', anonymous=False)

def run_IPAS():
    pass

def run_Localize():
    while(rospy.get_param('/lightswitch')=='on'):

        while(rospy.get_param('/localize_test/reconfigure')==False): #Set true when done sampling

            #If we set sample to true, begin a new localization test
            if(rospy.get_param('/localize_test/sample')==True):

                rospy.set_param('/localize_test/sample', False) #Reset the parameter to avoid loop

                sampleCount = 100 #Default Sample count for service
                rospy.wait_for_service('localize_service') #Wait for service to be ready
                localizeService = rospy.ServiceProxy('localize_service', localize_service)
                localizeData = localizeService(sampleCount) #Call service from UAV, stored as tuple of arrays
                #localizeData Returns: {localizeData.posx, localizeData.posy, localizeData.posz}

                #Then call function from localization report and pass in data
                #Data: LocalizeData, AnchorPositions, TestLocation
                #Goal: Generate CSV file of sample data, sample location,
                #   sample mean, sample variance, sample std, sample error

            else:
                time.sleep(1) #Sleep while waiting

        #Reset parameters for next anchor configuration and new samples
        rospy.set_param('/localize_test/reconfigure', False)
        rospy.set_param('localize_test/sample', False)

        #Call finalize report, which then takes all the accumulated data and
        #does Matplotlib to graphically output the results for configuration samples
        #Input: None
        #Goal: Use CSV data created in configuration to create graphic representation

def run_FlightTest():
    pass

def run_GroundTest():
    pass

def run_IPAS_sim():
    pass


def run():
    #System Mode ('IPAS', 'Localize', 'Flight_Test', 'Ground_Test')
    mode = rospy.get_param('/mode')

    if(mode=='IPAS'):
        run_IPAS()
        pass
    elif(mode=='Localize'):
        run_Localize()
    elif(mode=='Flight_Test'):
        run_FlightTest()
    elif(mode=='Ground_Test'):
        run_GroundTest()
    elif(mode=='IPAS_Sim'):
        run_IPAS_sim()
    else:
        print('Failed to initialize')

if __name__ == "__main__":

    initialize()
    run()
