drone.takeoff()
drone.hover(1)

for i in range(4):
    drone.move_forward(50, "cm", 1)
    drone.turn_left()

drone.land()
drone.close()