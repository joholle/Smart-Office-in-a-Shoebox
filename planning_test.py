from AIPlanning.planner import Planner

planner = Planner()

planner.update_problem(set_light=5, set_humidity=15, set_inside_temp=15, set_water_level=5, set_outside_temp=5,
                       set_is_raining=False,
                       set_force_light=False, set_force_window=False, set_force_cooler=False, set_force_water=False,
                       light_on_state=True, windows_open_state=True, air_cooler_on_state=True, water_spender_on_state=True
                       )

print(planner.solve())