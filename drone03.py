from codrone_edu.drone import *

drone = Drone()
drone.connect()

drone.set_drone_LED(255, 0, 255, 100)
time.sleep(1)
melody = [
    # start
    (Note.F5, 100), (Note.F5, 100), (Note.F5, 200), (Note.F5, 200), (Note.F5, 200), (Note.E5, 200), (Note.D5, 200), (Note.C5, 200),

    # Hey its me its...
    (Note.C5, 600), (Note.D5, 200), (Note.C5, 600), (Note.D5, 200),
    
    # Verity
    (Note.E5, 200), (Note.D5, 200), (Note.C5, 1200),
    
    # Ask me anything
    (Note.A5, 400), (Note.A5, 400), (Note.A5, 200), (Note.E5, 400), (Note.D5, 1600),
    
    # I know about a...
    (Note.E5, 200), (Note.C5, 600), (Note.E5, 200), (Note.C5, 600), (Note.D5, 200),
    
    # Million Things
    (Note.E5, 100), (Note.E5, 100), (Note.D5, 200), (Note.C5, 1200),
    
    # Ill do everything!
    (Note.A5, 400), (Note.A5, 400), (Note.G5, 200), (Note.E5, 400), (Note.D5, 2200),
    
    # Whats the capital of France
    (Note.B5, 200), (Note.B5, 200), (Note.G5, 200), (Note.G5, 200), (Note.F5, 200), (Note.F5, 200), (Note.E5, 1000),
    
    # Oh oui oui oui, it is Paris! Merci
    (Note.D5, 200), (Note.B5, 200), (Note.B5, 200), (Note.E5, 1000), (Note.C5, 200), (Note.E5, 200), (Note.E5, 200), (Note.F5, 1000), (Note.D5, 400), (Note.C5, 400),
]

print("Playing melody...")

for note, duration in melody:
    drone.drone_buzzer(note, int(duration))


drone.set_drone_LED(255, 255, 255, 100)

print("Finished!")
drone.close()