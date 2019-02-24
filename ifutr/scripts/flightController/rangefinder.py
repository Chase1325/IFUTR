from time import time
from serial import Serial

serialDevice = "/dev/ttyAMA0" # default for RaspberryPi
maxwait = 3 # seconds to try for a good reading before quitting

def measure(portName):
    ser = Serial(portName, 9600, 8, 'N', 1, timeout=1)
    timeStart = time()
    valueCount = 0

    while time() < timeStart + maxwait:
        if ser.inWaiting():
            bytesToRead = ser.inWaiting()
            valueCount += 1
            if valueCount < 2: # 1st reading may be partial number; throw it out
                continue
            testData = ser.read(bytesToRead)
            if not testData.startswith(b'R'):
                # data received did not start with R
                continue
            try:
                sensorData = testData.decode('utf-8').lstrip('R')
            except UnicodeDecodeError:
                # data received could not be decoded properly
                continue
            try:
                mm = int(sensorData)
            except ValueError:
                # value is not a number
                continue
            ser.close()
            return(mm)

    ser.close()
    raise RuntimeError("Expected serial data not received")

def get_range_finder_reading(connection):
        b = connection.read(1)
        while b != b'R':
            b = connection.read(1)
        b = connection.read(1)
        num = b''
        while b != b'\r':
            num += b
            b = connection.read(1)
        if connection.in_waiting > 10:
            connection.flush()
        return int(num.decode()) // 10


if __name__ == '__main__':
    connection = Serial(serialDevice)
    while 1:
        #measurement = measure(serialDevice)
        measurement = get_range_finder_reading(connection)
        print("distance =",measurement)
