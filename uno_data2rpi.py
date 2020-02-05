import serial
import time
#setting up the serial line
ser = serial.Serial('COM7',115200)
time.sleep(2)
# Read and record the data
data =[]
                       # empty list to store the data
for i in range(50):
b = ser.readline()
string_n = b.decode()
string = string_n.rstrip() # remove \n and \r
flt = float(string)        # convert string to float
print(flt)
data.append(flt)           # add to the end of data list
time.sleep(0.1)
# wait (sleep) 0.1 seconds

ser.close()
# show the data

for line in data:
    print(line)