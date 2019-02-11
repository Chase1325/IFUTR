#!/usr/bin/env python

import rospy
import pypozyx

from localization.IPozyx import IPozyx
from time import sleep

from pypozyx import (POZYX_POS_ALG_UWB_ONLY, POZYX_3D, Coordinates, POZYX_SUCCESS, PozyxConstants, version,
                     DeviceCoordinates, PozyxSerial, get_first_pozyx_serial_port, SingleRegister, DeviceList, PozyxRegisters)

from pypozyx.tools.version_check import perform_latest_version_check

from command_unit.srv import *

def initialize():
    rospy.init_node('UAV', anonymous=False)


def run_IPAS():
    pass

def localize_serviceHandler(request):
    print('Starting the handler')

    # necessary data for calibration,
    #change the IDs and coordinates yourself according to your measurement
    anchors = rospy.get_param('/anchorpose')

    r = IPozyx(anchors)
    r.setup()

    x_buff = []
    y_buff = []
    z_buff = []

    print('About to gather position data')
    i=0
    while(i<100):
        try:
            pos = r.run()
            x_buff.append(pos.x)
            y_buff.append(pos.y)
            z_buff.append(pos.z)

            i+=1
        except:
            pass

    #return localize_serviceResponse(x_buff,y_buff,z_buff)
    return {'posx': x_buff, 'posy': y_buff, 'posz': z_buff}
    
def run_Localize():
    print('Waiting for a call to the service')
    #Wait for client to request service
    serv = rospy.Service('localize_serv', command_unit.srv.localize_service, localize_serviceHandler)
    print('Ready for call to service')
    serv.spin()


def run_FlightTest():
    #Flight test updates drone pose inside the workspace
    #by user-sent pose commands

    pass

def run():
    #System Mode ('IPAS', 'Localize', 'Flight_Test', 'Ground_Test')
    #Selected mode determined from rosparam values
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
