from codrone_edu.drone import *

drone = Drone()
drone.connect()

print("Battery:", drone.get_battery(), "%")

drone.takeoff()
drone.set_drone_LED(0, 255, 0, 100)
drone.hover(6)
drone.land()

drone.close()