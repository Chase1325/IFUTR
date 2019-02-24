
from time import sleep

from pypozyx import (POZYX_POS_ALG_UWB_ONLY, POZYX_3D, Coordinates, POZYX_SUCCESS, PozyxConstants, version,
                     DeviceCoordinates, PozyxSerial, get_first_pozyx_serial_port, SingleRegister, DeviceList, PozyxRegisters)
from pythonosc.udp_client import SimpleUDPClient

from pypozyx.tools.version_check import perform_latest_version_check

import rospy
from std_msgs.msg import Int16

class IPozyx(object):
    """Continuously calls the Pozyx positioning function and prints its position."""

    def __init__(self, anchors):

        self.serial_port = get_first_pozyx_serial_port()
        if self.serial_port is None:
            print("No Pozyx connected. Check your USB cable or your driver!")

        self.pozyx = PozyxSerial(self.serial_port)
        print(self.serial_port)

        if(anchors.get('count')==4):

            self.anchors = [DeviceCoordinates(0x6110, 1,
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


        self.algorithm = PozyxConstants.POSITIONING_ALGORITHM_UWB_ONLY
        self.dimension = PozyxConstants.DIMENSION_3D
        self.height = 1000

        self.pubX = rospy.Publisher('posX', Int16, queue_size=10)
        self.pubY = rospy.Publisher('posY', Int16, queue_size=10)
        self.subZ = rospy.Subscriber('range', Int16, rangeCallback)

    def setup(self):
        self.setAnchorsManual()
        #self.printPublishConfigurationResult()

    def rangeCallback(self, msg):
        self.height = msg.data

    def run(self, height):
        """Performs positioning and displays/exports the results."""
        success=False
        while(success!=True):
            position = Coordinates()
            status = self.pozyx.doPositioning(
                position, self.dimension, height, self.algorithm)
                #position, self.dimension, self.height, self.algorithm)
                #position, self.dimension, self.height, self.algorithm, remote_id=self.remote_id)
            if status == POZYX_SUCCESS:
                success=True
                return position
            else:
                pass
                #sleep(0.025)

    def pubPozyx(self):
        #success=False
        #while(success!=True):
            position = Coordinates()
            status = self.pozyx.doPositioning(
                #position, self.dimension, height, self.algorithm)
                position, self.dimension, self.height, self.algorithm)
                #position, self.dimension, self.height, self.algorithm, remote_id=self.remote_id)
            if status == POZYX_SUCCESS:
                success=True
                self.pubX.publish(position.x)
                self.pubY.publish(position.y)
            else:
                pass
            #rospy.spin()

    def setAnchorsManual(self):
        """Adds the manually measured anchors to the Pozyx's device list one for one."""
        #status = self.pozyx.clearDevices(remote_id=self.remote_id)
        status = self.pozyx.clearDevices()
        for anchor in self.anchors:
            #status &= self.pozyx.addDevice(anchor, remote_id=self.remote_id)
            status &= self.pozyx.addDevice(anchor)
        if len(self.anchors) > 4:
            #status &= self.pozyx.setSelectionOfAnchors(PozyxConstants.ANCHOR_SELECT_AUTO, len(self.anchors), remote_id=self.remote_id)
            status &= self.pozyx.setSelectionOfAnchors(PozyxConstants.ANCHOR_SELECT_AUTO, len(self.anchors))
        return status



def PozyxProcess():
    anchors = rospy.get_param('/anchorpose')
    pozyx = IPozyx(anchors)
    pozyx.setup()
    while(rospy.get_param('/lightswitch')==True):
        pozyx.pubPozyx()
