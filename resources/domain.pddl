(define (domain office_room)
    (:requirements :conditional-effects :disjunctive-preconditions :equality :fluents :negative-preconditions :strips :typing)
    (:predicates (air_cooler_on) (cooler_action_done) (force_cooler) (force_light) (force_water) (force_window) (is_raining) (light_action_done) (light_on) (no_action_possible) (water_action_done) (water_spender_on) (window_action_done) (windows_open))
    (:functions (humidity) (inside_temp) (light) (outside_temp) (water_level))
    (:action close_window
        :parameters ()
        :precondition (or (and (< (humidity) 10) (< (inside_temp) 10) (windows_open)) (and (is_raining) (windows_open)))
        :effect (and (not (windows_open)) (window_action_done))
    )
     (:action fill_up_water
        :parameters ()
        :precondition (and (= (water_level) 0) (not (water_spender_on)))
        :effect (and (water_spender_on) (water_action_done))
    )
     (:action force_close_window
        :parameters ()
        :precondition (and (windows_open) (force_window))
        :effect (and (not (windows_open)) (window_action_done))
    )
     (:action force_off_light
        :parameters ()
        :precondition (and (light_on) (force_light))
        :effect (and (not (light_on)) (light_action_done))
    )
     (:action force_on_light
        :parameters ()
        :precondition (and (not (light_on)) (force_light))
        :effect (and (light_on) (light_action_done))
    )
     (:action force_open_window
        :parameters ()
        :precondition (and (not (windows_open)) (force_window))
        :effect (and (windows_open) (window_action_done))
    )
     (:action force_turn_off_cooler
        :parameters ()
        :precondition (and (air_cooler_on) (force_cooler))
        :effect (and (not (air_cooler_on)) (cooler_action_done))
    )
     (:action force_turn_on_cooler
        :parameters ()
        :precondition (and (not (air_cooler_on)) (force_cooler))
        :effect (and (air_cooler_on) (cooler_action_done))
    )
     (:action no_action
        :parameters ()
        :precondition (not (or (and (< (light) 10) (not (light_on))) (and (not (light_on)) (force_light)) (and (light_on) (force_light)) (and (or (> (humidity) 45) (> (inside_temp) 22)) (not (is_raining)) (> (inside_temp) (outside_temp)) (not (windows_open))) (and (< (humidity) 45) (< (inside_temp) 10) (windows_open)) (and (is_raining) (windows_open)) (and (not (windows_open)) (force_window)) (and (windows_open) (force_window)) (and (or (< (inside_temp) 22) (> (inside_temp) (outside_temp))) (not (air_cooler_on))) (and (or (> (inside_temp) 22) (< (inside_temp) (outside_temp))) (air_cooler_on)) (and (not (air_cooler_on)) (force_cooler)) (and (air_cooler_on) (force_cooler)) (and (= (water_level) 0) (not (water_spender_on))) (and (> (water_level) 10) (water_spender_on)) (and (not (water_spender_on)) (force_water))))
        :effect (no_action_possible)
    )
     (:action open_window
        :parameters ()
        :precondition (and (or (> (humidity) 45) (> (inside_temp) 22)) (not (is_raining)) (> (inside_temp) (outside_temp)) (not (windows_open)))
        :effect (and (windows_open) (window_action_done))
    )
     (:action stop_water
        :parameters ()
        :precondition (and (> (water_level) 10) (water_spender_on))
        :effect (and (not (water_spender_on)) (water_action_done))
    )
     (:action stop_water
        :parameters ()
        :precondition (and (not (water_spender_on)) (force_water))
        :effect (and (water_spender_on) (water_action_done))
    )
     (:action turn_off_cooler
        :parameters ()
        :precondition (and (or (> (inside_temp) 10) (< (inside_temp) (outside_temp))) (air_cooler_on))
        :effect (and (not (air_cooler_on)) (cooler_action_done))
    )
     (:action turn_on_cooler
        :parameters ()
        :precondition (and (or (< (inside_temp) 10) (> (inside_temp) (outside_temp))) (not (air_cooler_on)))
        :effect (and (air_cooler_on) (cooler_action_done))
    )
     (:action turn_on_light
        :parameters ()
        :precondition (and (< (light) 10) (not (light_on)))
        :effect (and (light_on) (light_action_done))
    )
    ;optimal humidity: <45 
    ;optimal temperature: 22
)