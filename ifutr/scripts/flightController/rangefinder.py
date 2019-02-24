from time import time
from serial import Serial
import rospy
from std_msgs.msg import Int16


class Rangefinder(object):

    def __init__(self):
        #self.serialDevice = "/dev/ttyAMA0" # default for RaspberryPi
        self.serialDevice = "/dev/serial0"
        self.connection = Serial(self.serialDevice)
        #self.node = rospy.init_node('rangeFinder', anonymous=True)
        self.pub = rospy.Publisher('range', Int16, queue_size=10)

    def getRange(self):
            b = self.connection.read(1)
            while b != b'R':
                b = self.connection.read(1)
            b = self.connection.read(1)
            num = b''
            while b != b'\r':
                num += b
                b = self.connection.read(1)
            if self.connection.in_waiting > 10:
                self.connection.flush()

            val = int(num.decode()) // 10
            print('MASSIVE FARTS!!!' + str(val))
            return val

    def pubRange(self):
        while 1:
            b = self.connection.read(1)
            while b != b'R':
                b = self.connection.read(1)
            b = self.connection.read(1)
            num = b''
            while b != b'\r':
                num += b
                b = self.connection.read(1)
            if self.connection.in_waiting > 10:
                self.connection.flush()

            val = int(num.decode()) // 10
            #print('MASSIVE FARTS!!!' + str(val))
            self.pub.publish(val)


def RangeProcess():
    r = Rangefinder()
    while(rospy.get_param('/lightswitch')==True):
        r.pubRange()


        
#if __name__ == '__main__':
#    connection = Serial(serialDevice)
#    while 1:
#        measurement = getRange(connection)
#        print("distance =",measurement)
