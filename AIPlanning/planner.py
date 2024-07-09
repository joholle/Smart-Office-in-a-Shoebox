import os
from pddl.formatter import domain_to_string, problem_to_string

from AIPlanning.domain import Domain
from AIPlanning.problem import Problem

class Planner:
    def __init__(self):
        self.domain = Domain().create()
        domain_file = open("resources/domain.pddl", "w")
        domain_file.write(domain_to_string(self.domain))
        domain_file.close()

    def update_problem(self, 
                       set_light, set_humidity, set_inside_temp, set_water_level, set_outside_temp,
                       set_is_raining,
                       set_force_light, set_force_window, set_force_cooler, set_force_water,
                       light_on_state, windows_open_state, air_cooler_on_state, water_spender_on_state
                       ):
        problem = Problem().create( domain=self.domain,
                                set_light=set_light, set_humidity=set_humidity, set_inside_temp=set_inside_temp, set_water_level=set_water_level, set_outside_temp=set_outside_temp,
                                set_is_raining=set_is_raining,
                                set_force_light=set_force_light, set_force_window=set_force_window, set_force_cooler=set_force_cooler, set_force_water=set_force_water,
                                # state: 
                                light_on_state=light_on_state, windows_open_state=windows_open_state, air_cooler_on_state=air_cooler_on_state, water_spender_on_state=water_spender_on_state
                                )

        problem_file = open("resources/problem.pddl", "w")
        problem_file.write(problem_to_string(problem))
        problem_file.close()

    def solve(self):
        os.system(".\\AIPlanning\\metric-ff-crossplatform-main\\ff-v2.1.exe -o resources/domain.pddl -f resources/problem.pddl -s 0 > resources/plan.txt")

        actions = []

        with open("resources/plan.txt", 'r') as file:
            step_found = False
            for line in file:
                if step_found:
                    if "time spent" in line:
                        break
                    if "REACH-GOAL" in line:
                        break
                    if ":" not in line:
                        break
                    actions.append(line.strip()[line.strip().find(":")+2:])
                elif "step" in line:
                    actions.append(line.strip()[line.strip().find(":")+2:])
                    step_found = True
        
        return actions