import serial

def scan():
    available = []
    for i in range(256):
        try:
            s = serial.Serial('COM'+str(i))
            available.append( (s.portstr))

        except serial.SerialException:
            pass

    for s in available:
        print("Connextion available on : "+ s )
        message = "G0 x10"
        serialPort = serial.Serial(port = s, baudrate=115200,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        serialPort.write(message.encode())
        print("Data sended : " + message)
        line = []
        while True:
            for c in serialPort.read():
                line.append(c)
                if c == '\n':
                    print("Line: " + ''.join(line))
                    line = []
                    break
        serialPort.close()
        print("Port closed Byebye")


if __name__=='__main__':
    scan()
