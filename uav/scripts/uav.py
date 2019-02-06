#!/usr/bin/env python

import rospy
import pypozyx

import IPozyx

from command_unit.srv import localize_service, localize_serviceResponse

def initialize():
    rospy.init_node('UAV', anonymous=False)


def run_IPAS():
    pass

def localize_serviceHandler(request):
    print('Starting the handler')
    #Initialize the pozyx interface with the anchors
    anchors = rospy.get_param('/anchorpose')
    pozyx = IPozyx.IPozyx(anchors)

    x_buff = []
    y_buff = []
    z_buff = []
    
    print('About to gather position data')
    for i in range(100):
        pos = pozyx.getPosition()
        x_buff.append(pos[0])
        y_buff.append(pos[1])
        z_buff.append(pos[2])

    return localize_serviceResponse(x_buff,y_buff,z_buff)

def run_Localize():

    while(rospy.get_param('/lightswitch')==True):

	print('Waiting for a call to the service')
        #Wait for client to request service
        serv = rospy.Service('localize_serv', localize_service, localize_serviceHandler)
        rospy.spin()

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
        pass #Drone not required
    elif(mode=='IPAS_Sim'):
        pass #Drone not required
    else:
        print('Failed to initialize')

if __name__ == "__main__":

    initialize()
    run()
