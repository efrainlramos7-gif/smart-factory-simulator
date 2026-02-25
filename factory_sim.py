import time
import random

# ----------------------------
# SMART FACTORY SIMULATION
# ----------------------------

print("=== SMART FACTORY CONTROL SYSTEM ===")
print("Starting system...\n")

while True:

    # SENSE
    temperature = random.randint(60, 100)
    emergency_button = random.choice([True, False])
    door_open = random.choice([True, False])
    start_button = random.choice([True, False])

    # THINK
    if temperature > 80:
        fan = "ON"
    else:
        fan = "OFF"

    if door_open or emergency_button:
        safe = False
    else:
        safe = True

    if safe and start_button:
        conveyor = "ON"
    else:
        conveyor = "OFF"

    if not safe:
        alarm = "ON"
    else:
        alarm = "OFF"

    # ACT
    print("----- SYSTEM STATUS -----")

    print(f"Temperature: {temperature}°F")
    print(f"Door Open: {door_open}")
    print(f"Emergency Button: {emergency_button}")
    print(f"Start Button: {start_button}")

    print("-------------------------")

    print(f"Fan: {fan}")
    print(f"Conveyor: {conveyor}")
    print(f"Alarm: {alarm}")

    print("-------------------------\n")

    time.sleep(3)
