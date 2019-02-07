#!/usr/bin/env python

import rospy
import pypozyx

from localization.IPozyx import IPozyx
from localization.IPozyx2 import IPozyx2
from time import sleep

from pypozyx import (POZYX_POS_ALG_UWB_ONLY, POZYX_3D, Coordinates, POZYX_SUCCESS, PozyxConstants, version,
                     DeviceCoordinates, PozyxSerial, get_first_pozyx_serial_port, SingleRegister, DeviceList, PozyxRegisters)
from pythonosc.udp_client import SimpleUDPClient

from pypozyx.tools.version_check import perform_latest_version_check

from command_unit.srv import *

def initialize():
    rospy.init_node('UAV', anonymous=False)


def run_IPAS():
    pass

def localize_serviceHandler(request):
    print('Starting the handler')
    #Initialize the pozyx interface
    check_pypozyx_version = True
    if check_pypozyx_version:
        perform_latest_version_check()

    # shortcut to not have to find out the port yourself
    serial_port = get_first_pozyx_serial_port()
    print(serial_port)
    if serial_port is None:
        print("No Pozyx connected. Check your USB cable or your driver!")


    remote_id = 0x683e                 # remote device network ID
    remote = False                   # whether to use a remote device
    if not remote:
        remote_id = None

    # enable to send position data through OSC
    use_processing = False

    # configure if you want to route OSC to outside your localhost. Networking knowledge is required.
    ip = "127.0.0.1"
    network_port = 8888

    osc_udp_client = None
    if use_processing:
        osc_udp_client = SimpleUDPClient(ip, network_port)

    # necessary data for calibration, change the IDs and coordinates yourself according to your measurement
    anchors = rospy.get_param('/anchorpose')
    anchors = [DeviceCoordinates(0x6110, 1,
                                      Coordinates(anchors.get('0x6110')[0],
                                                  anchors.get('0x6110')[1],
                                                  anchors.get('0x6110')[2])),
                    DeviceCoordinates(0x6115, 1,
                                      Coordinates(anchors.get('0x6115')[0],
                                                  anchors.get('0x6115')[1],
                                                  anchors.get('0x6115')[2])),
                    DeviceCoordinates(0x6117, 1,
                                      Coordinates(anchors.get('0x6117')[0],
                                                  anchors.get('0x6117')[1],
                                                  anchors.get('0x6117')[2])),
                    DeviceCoordinates(0x611e, 1,
                                      Coordinates(anchors.get('0x611e')[0],
                                                  anchors.get('0x611e')[1],
                                                  anchors.get('0x611e')[2]))]

    # positioning algorithm to use, other is PozyxConstants.POSITIONING_ALGORITHM_TRACKING
    algorithm = PozyxConstants.POSITIONING_ALGORITHM_UWB_ONLY
    # positioning dimension. Others are PozyxConstants.DIMENSION_2D, PozyxConstants.DIMENSION_2_5D
    dimension = PozyxConstants.DIMENSION_3D
    # height of device, required in 2.5D positioning
    height = 1000

    pozyx = PozyxSerial(serial_port)
    r = IPozyx2(pozyx, osc_udp_client, anchors, algorithm, dimension, height, remote_id)
    r.setup()
    #while True:
    #    r.loop()


    #pozyx = IPozyx(anchors)

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

    return localize_serviceResponse(x_buff,y_buff,z_buff)

def run_Localize():
    # while(rospy.get_param('/lightswitch')==True):
    print('Waiting for a call to the service')
    #Wait for client to request service
    serv = rospy.Service('localize_serv', localize_service, localize_serviceHandler)
    print('Ready for call to service')
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
