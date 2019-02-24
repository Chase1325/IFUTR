from time import time
from serial import Serial



class Rangefinder(object):

    def __init__(self):
        #self.serialDevice = "/dev/ttyAMA0" # default for RaspberryPi
        self.serialDevice = "/dev/serial0"
        self.connection = Serial(self.serialDevice)

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


#if __name__ == '__main__':
#    connection = Serial(serialDevice)
#    while 1:
#        measurement = getRange(connection)
#        print("distance =",measurement)
