#!/usr/bin/env python
###############################################################################
#Chase St. Laurent
#Worcester Polytechnic Institute
#IPAS-ROS Project
#
#
#MASTER Command Node
################################################################################
import time

#ROS Imports
import rospy
from command_unit.srv import *

#Script Imports
import sys
#sys.path.insert(0, '~/catkin_ws/src/IPAS-Ros/command_unit/scripts/localization')
#import localization.localization_csv_handler as csvHandler
#import localization.localization_statistics as statsHandler
from localization import localization_csv_handler, localization_statistics
from localization.localization_statistics import SampleStats

def initialize():
    rospy.init_node('command_unit', anonymous=False)
    print('Initialized RosNode')

def run_IPAS():
    pass

def run_Localize():
    while(rospy.get_param('/lightswitch')==True):

        print('Waiting for the service')
        rospy.wait_for_service('localize_serv') #Wait for service to be ready
        print('Done waiting for the service')

        print('Creating Service Proxy')
        localizeService = rospy.ServiceProxy('localize_serv', localize_service, persistent=True)
        print('Made Service Proxy, persistent for multiple calls')

        while(rospy.get_param('/localize_test/reconfig')==False): #Set true when done sampling

            #If we set sample to true, begin a new localization test
            if(rospy.get_param('/localize_test/sample')==True):
                print('Wait for sample')
                rospy.set_param('/localize_test/sample', False) #Reset the parameter to avoid loop

                try:
                    #Call service from UAV, stored as tuple of arrays
                    #localizeData Returns:
                    #{localizeData.posx, localizeData.posy, localizeData.posz}
                    localizeData = localizeService()

                    anchorDistance = rospy.get_param('/anchorpose/size')
                    testLocale = rospy.get_param('/localize_test/testLocale')

                    #Find data statistics
                    stats = SampleStats(localizeData) #Make the class
                    stats.setErr(testLocale)

                    #Data: LocalizeData, AnchorPositions, TestLocation
                    #Goal: Generate CSV file of sample data, sample location,
                    #      sample mean, sample variance, sample std, sample error
                    localization_csv_handler.csv_handler(stats, anchorDistance, testLocale)
                except:
                    print('Fail')
            else:
                print('Waiting for /localize_test/sample to be set to True')
                time.sleep(5) #Sleep while waiting

        #Reset parameters for next anchor configuration and new samples
        rospy.set_param('/localize_test/reconfig', False)
        rospy.set_param('localize_test/sample', False)

        localizeService.close()#Close persistent connection

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
