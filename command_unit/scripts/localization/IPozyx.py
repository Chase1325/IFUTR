#Pozyx Interface

from pypozyx import *
from pypozyx.definitions.constants import *
from pypozyx.definitions.registers import *


class IPozyx:
    def __init__(self, anchors, dimension=POZYX_3D, algorithm=POZYX_POS_ALG_UWB_ONLY):


        self.serial_port = get_first_pozyx_serial_port()
        self.pozyx = PozyxSerial(self.serial_port)
        self.use_processing = False
        self.ip = '127.0.0.1'
        self.network_port = 8888

        self.anchors = [DeviceCoordinates(0x6110, 1,
                                          Coordinates(anchors.get('0x6110')[0],
                                                      anchors.get('0x6110')[0],
                                                      anchors.get('0x6110')[0])),
                        DeviceCoordinates(0x6115, 1,
                                          Coordinates(anchors.get('0x6115')[0],
                                                      anchors.get('0x6115')[0],
                                                      anchors.get('0x6115')[0])),
                        DeviceCoordinates(0x6117, 1,
                                          Coordinates(anchors.get('0x6117')[0],
                                                      anchors.get('0x6117')[0],
                                                      anchors.get('0x6117')[0])),
                        DeviceCoordinates(0x611e, 1,
                                          Coordinates(anchors.get('0x611e')[0],
                                                      anchors.get('0x611e')[0],
                                                      anchors.get('0x611e')[0]))]

        self.algorithm = algorithm
        self.dimension = dimension

        self.setup()
    def setup(self):
        self.setAnchorsManual()

    def setAnchorsManual(self):
            """Adds the manually measured anchors to the Pozyx's device list one for one."""
            status = self.pozyx.clearDevices()
            for a in self.anchors:
                status &= self.pozyx.addDevice(a)
            if len(self.anchors) > 4:
                status &= self.pozyx.setSelectionOfAnchors(ANCHOR_SELECT_AUTO, len(self.anchors))
            return status

    def getPosition(self):
        pos = Coordinates()
        if self.pozyx.doPositioning(pos, self.dimension, 0, self.algorithm) != POZYX_SUCCESS:
            self.print_error_code("positioning")
        #error = PositionError()
        #if self.pozyx.getPositionError(error) != POZYX_SUCCESS:
        #    log("Failed to get positioning error.")
        print(pos)
        return pos
