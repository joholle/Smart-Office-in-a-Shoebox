from pddl.pddl import PDDL
from mqtt.mqtt import MQTT
from interfaceSC import Interface
import json, time


# mqtt = MQTT("Laptop", "masterpi", "laptop_channel", "pi_channel")
# id = 0
# cycle = False
# while True:
#     if cycle:
#         mqtt.publish(str(id) + " open window")
#     else:
#         mqtt.publish(str(id) + " close window")
#     id += 1
#     cycle = not cycle
#     time.sleep(4)
# time.sleep(5)

# pddl = PDDL("AIPlanning/Domain.pddl", "AIPlanning/Problem.pddl")
# pddl.set_state(frozenset({('off', 'light1'), ('on', 'light2'), ('value-low', 'light_sensor'), ('value-low', 'light_sensor2')}))

# plan = pddl.plan()
# if plan != None:
#     for action in plan:
#         print(str(action))
        # mqtt.publish(json.loads(str(action)))

# print("DONE")


class Laptop:
    def __init__(self):
        self.mqtt = MQTT("Laptop", "masterpi", "laptop_channel", "pi_channel")
        self.id = 0

        self.interface = Interface()


if __name__ == "__main__":
    laptop = Laptop()

# Run interface
# every 5 seconds:
#   get sensor readings from arduino
#   create pddl plan by recieving info from mqtt
#   execute plan, by sending back to mqtt arduino
#   update interface