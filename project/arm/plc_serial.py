import serial

ser = serial.Serial('COM7', 9600)

read = 0

print("Start")
print(ser.name)

ser.write(b'\03pY\04')

print("Reading")
read = ser.readline().decode('ascii')
print("Reading: ", read)

ser.close()