import sys
import csv
import random
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
)

class Simulator(QWidget):
    def __init__(self):
        super().__init__()
        self.SimulatorUI()

    def SimulatorUI(self):
        # VEHICLE
        self.lb1 = QLabel("Number of Vehicles")
        self.lb2 = QLabel("Length of Timestep")
        self.lb3 = QLabel("Size of Grid")
        self.lb4 = QLabel("Limit of Speed")
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.input3 = QLineEdit(self)
        self.input4 = QLineEdit(self)
        self.btnSimulateVehicle = QPushButton("Simulate Vehicles")
        self.btnSimulateVehicle.pressed.connect(self.simulate_vehicles)

        # SERVER
        self.lb5 = QLabel("Number of Servers")
        self.lb6 = QLabel("Size of Grid")
        self.lb7 = QLabel("Limit of Arrival rate")
        self.input5 = QLineEdit(self)
        self.input6 = QLineEdit(self)
        self.input7 = QLineEdit(self)
        self.btnSimulateServer = QPushButton("Simulate Servers")
        self.btnSimulateServer.pressed.connect(self.simulate_servers)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lb1)
        vbox1.addWidget(self.input1)
        vbox1.addWidget(self.lb2)
        vbox1.addWidget(self.input2)
        vbox1.addWidget(self.lb3)
        vbox1.addWidget(self.input3)
        vbox1.addWidget(self.lb4)
        vbox1.addWidget(self.input4)
        vbox1.addWidget(self.btnSimulateVehicle)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.lb5)
        vbox2.addWidget(self.input5)
        vbox2.addWidget(self.lb6)
        vbox2.addWidget(self.input6)
        vbox2.addWidget(self.lb7)
        vbox2.addWidget(self.input7)
        vbox2.addWidget(self.btnSimulateServer)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        self.setLayout(hbox)
        self.setWindowTitle("My Simulator")
        self.move(400, 100)
        self.resize(200, 200)
        self.show()

    def simulate_vehicles(self):
        self.time = datetime.now()
        self.vehicles = int(self.input1.text())
        self.timestep = int(self.input2.text())
        self.gridsize = int(self.input3.text())
        self.speedlimit = int(self.input4.text())

        f = open("simulated_vehicles.csv", "w", newline="")
        wr = csv.writer(f)
        wr.writerow(["Row Number", "Vehicle ID", "Timestamp", "Location_x", "Location_y", "Speed", "Dir"])

        row_number = 1
        for i in range(self.vehicles):
            for j in range(self.timestep):
                time = self.time + timedelta(seconds=j+1)
                data_per_vehicle = []
                data_per_vehicle.append(row_number)
                data_per_vehicle.append(i+1)
                data_per_vehicle.append(time.strftime("%Y-%m-%d %H:%M:%S"))
                data_per_vehicle.append(random.randint(1, self.gridsize))
                data_per_vehicle.append(random.randint(1, self.gridsize))
                data_per_vehicle.append(random.randint(1, self.speedlimit))
                data_per_vehicle.append(random.randint(0,3))

                wr.writerow(data_per_vehicle)
                row_number += 1

    def simulate_servers(self):
        self.servers = int(self.input5.text())
        self.gridsize = int(self.input6.text())
        self.arrivalrate = int(self.input7.text())
        f = open("simulated_servers.csv", "w", newline="")
        wr = csv.writer(f)
        wr.writerow(["Row Number", "Server ID", "Location_x", "Location_y", "Arrival Rate"])

        row_number = 1
        for i in range(self.servers):
            data_per_server = []
            data_per_server.append(row_number)
            data_per_server.append(i+1)
            data_per_server.append(random.randint(1, self.gridsize))
            data_per_server.append(random.randint(1, self.gridsize))
            data_per_server.append(random.randint(1, self.arrivalrate))

            wr.writerow(data_per_server)
            row_number += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Simulator()
    sys.exit(app.exec_())