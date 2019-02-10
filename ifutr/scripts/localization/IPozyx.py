
from time import sleep

from pypozyx import (POZYX_POS_ALG_UWB_ONLY, POZYX_3D, Coordinates, POZYX_SUCCESS, PozyxConstants, version,
                     DeviceCoordinates, PozyxSerial, get_first_pozyx_serial_port, SingleRegister, DeviceList, PozyxRegisters)
from pythonosc.udp_client import SimpleUDPClient

from pypozyx.tools.version_check import perform_latest_version_check

class IPozyx(object):
    """Continuously calls the Pozyx positioning function and prints its position."""

    def __init__(self, anchors):

        self.serial_port = get_first_pozyx_serial_port()
        if self.serial_port is None:
            print("No Pozyx connected. Check your USB cable or your driver!")

        self.pozyx = PozyxSerial(self.serial_port)

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

    def setup(self):
        self.setAnchorsManual()
        self.printPublishConfigurationResult()

    def run(self):
        """Performs positioning and displays/exports the results."""
        position = Coordinates()
        status = self.pozyx.doPositioning(
            position, self.dimension, self.height, self.algorithm, remote_id=self.remote_id)
        if status == POZYX_SUCCESS:
            return position
        else:
            pass

    def setAnchorsManual(self):
        """Adds the manually measured anchors to the Pozyx's device list one for one."""
        status = self.pozyx.clearDevices(remote_id=self.remote_id)
        for anchor in self.anchors:
            status &= self.pozyx.addDevice(anchor, remote_id=self.remote_id)
        if len(self.anchors) > 4:
            status &= self.pozyx.setSelectionOfAnchors(PozyxConstants.ANCHOR_SELECT_AUTO, len(self.anchors),
                                                       remote_id=self.remote_id)
        return status
