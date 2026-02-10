rover_status = {"Battery": 100, "Heater": "Off", "Camera": "Standby"}

print(rover_status["Battery"])

new_rover_status = {"Battery": 85, "Heater": "On", "Camera": "Standby", "Speed": 5}

print(new_rover_status["Battery"], new_rover_status["Heater"], new_rover_status["Camera"], new_rover_status["Speed"], sep=",")

mission_log = [{"Site": "Crater A", "Radiation": "Low", "Water": False},{"Site": "Dune B", "Radiation": "High", "Water": True}]

for log in mission_log:
    print(log["Site"], "has", log["Radiation"], "radiation")
