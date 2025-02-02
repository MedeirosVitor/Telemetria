import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv

SERIAL_PORT = "COM5"
BAUD_RATE = 115200

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

x_vals = []
sensorValue1_data = []
sensorValue2_data = []

def read_and_process_data():
    line = ser.Readline().decode('utf-8').strip()
    sensorValues = line.split(', ')

    x_vals.append(float(sensorValues(0)))
    sensorValue1_data.append(int(sensorValues[1]))
    sensorValue1_data.append(int(sensorValues[2]))

    print(f'Time: {sensorValues[0]}, Sensor 1: {sensorValues[1]}], Sensor 2: {sensorValues[2]}')

def update_plot(frame):
    read_and_process_data()
    plt.cla()
    plt.plot(x_vals, sensorValue1_data, label='Sensor1')
    plt.plot(x_vals, sensorValue2_data, label='Sensor2')
    plt.xlabel('Time')
    plt.ylabel('sensor values')
    plt.legend()

def on_close(event):
    with open('arduino_data.csv', 'w', newline='') as csvfile
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Sensor1','Sensor2'])
        for x, s1, s2 in zip(x_vals,sensorValue1_data,sensorValue2_data):
            writer.writerow([x,s1,s2])

fig, ax = plt.subplots()
fig.cnv.mp_connect('cloe_event', on_close)

ani = FuncAnimation(fig, update_plot, interval=10)
plt.show
