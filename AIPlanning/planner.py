import os
import time
from pddl.formatter import domain_to_string, problem_to_string

from domain import Domain
from problem import Problem

domain = Domain().create()

domain_file = open("resources/domain.pddl", "w")
domain_file.write(domain_to_string(domain))
domain_file.close()

while True:
    problem = Problem().create( domain=domain,
                                set_light=5, set_humidity=15, set_inside_temp=15, set_water_level=5, set_outside_temp=5,
                                set_is_raining=False,
                                set_force_light=False, set_force_window=False, set_force_cooler=False, set_force_water=False,
                                light_on_status=True, windows_open_status=True, air_cooler_on_status=True, water_spender_on_status=True)

    problem_file = open("resources/problem.pddl", "w")
    problem_file.write(problem_to_string(problem))
    problem_file.close()

    os.system(".\\metric-ff-crossplatform-main\\ff-v2.1.exe -o resources/domain.pddl -f resources/problem.pddl -s 0 > resources/plan.txt")

    with open("resources/plan.txt", 'r') as file:
        step_found = False
        for line in file:
            if step_found:
                if "time spent" in line:
                    break
                if "REACH-GOAL" in line:
                    break
                print(line.strip())  
            elif "step" in line:
                print(line.strip())  
                step_found = True

    time.sleep(3)
