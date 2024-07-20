(define (domain office_room)
    (:requirements :conditional-effects :disjunctive-preconditions :equality :fluents :negative-preconditions :strips :typing)
    (:predicates (air_cooler_on) (cooler_action_done) (is_raining) (light_action_done) (light_on) (no_action_possible) (window_action_done) (windows_open) (z_end_predicate))
    (:functions (force_cooler) (force_light) (force_window) (humidity) (inside_temp) (light) (outside_temp) (water_level))
    (:action close_window
        :parameters ()
        :precondition (and (or (and (< (humidity) 40) (< (inside_temp) 22)) (and (is_raining) (> (water_level) 200)) (< (inside_temp) (outside_temp))) (windows_open) (= (force_window) 1))
        :effect (and (not (windows_open)) (window_action_done))
    )
     (:action force_close_window
        :parameters ()
        :precondition (and (windows_open) (= (force_window) 0))
        :effect (and (not (windows_open)) (window_action_done))
    )
     (:action force_off_light
        :parameters ()
        :precondition (and (light_on) (= (force_light) 0))
        :effect (and (not (light_on)) (light_action_done))
    )
     (:action force_on_light
        :parameters ()
        :precondition (and (not (light_on)) (= (force_light) 2))
        :effect (and (light_on) (light_action_done))
    )
     (:action force_open_window
        :parameters ()
        :precondition (and (not (windows_open)) (= (force_window) 2))
        :effect (and (windows_open) (window_action_done))
    )
     (:action force_turn_off_cooler
        :parameters ()
        :precondition (and (air_cooler_on) (= (force_cooler) 0))
        :effect (and (not (air_cooler_on)) (cooler_action_done))
    )
     (:action force_turn_on_cooler
        :parameters ()
        :precondition (and (not (air_cooler_on)) (= (force_cooler) 2))
        :effect (and (air_cooler_on) (cooler_action_done))
    )
     (:action no_action
        :parameters ()
        :precondition (not (or (and (< (light) 70) (not (light_on)) (= (force_light) 1)) (and (not (light_on)) (= (force_light) 2)) (and (light_on) (= (force_light) 0)) (and (or (> (humidity) 40) (> (inside_temp) 22)) (or (not (is_raining)) (< (water_level) 200)) (> (inside_temp) (outside_temp)) (not (windows_open)) (= (force_window) 1)) (and (or (and (< (humidity) 40) (< (inside_temp) 22)) (> (water_level) 200) (< (inside_temp) (outside_temp))) (windows_open) (= (force_window) 1)) (and (windows_open) (= (force_window) 0)) (and (not (windows_open)) (= (force_window) 2)) (and (> (inside_temp) 22) (< (inside_temp) (outside_temp)) (not (air_cooler_on)) (= (force_cooler) 1)) (and (or (< (inside_temp) 22) (> (inside_temp) (outside_temp))) (air_cooler_on) (= (force_cooler) 1)) (and (not (air_cooler_on)) (= (force_cooler) 2)) (and (air_cooler_on) (= (force_cooler) 0))))
        :effect (no_action_possible)
    )
     (:action open_window
        :parameters ()
        :precondition (and (or (> (humidity) 40) (> (inside_temp) 22)) (or (not (is_raining)) (< (water_level) 200)) (> (inside_temp) (outside_temp)) (not (windows_open)) (= (force_window) 1))
        :effect (and (windows_open) (window_action_done))
    )
     (:action turn_off_cooler
        :parameters ()
        :precondition (and (or (< (inside_temp) 22) (> (inside_temp) (outside_temp))) (air_cooler_on) (= (force_cooler) 1))
        :effect (and (not (air_cooler_on)) (cooler_action_done))
    )
     (:action turn_on_cooler
        :parameters ()
        :precondition (and (> (inside_temp) 22) (< (inside_temp) (outside_temp)) (not (air_cooler_on)) (= (force_cooler) 1))
        :effect (and (air_cooler_on) (cooler_action_done))
    )
     (:action turn_on_light
        :parameters ()
        :precondition (and (< (light) 70) (not (light_on)) (= (force_light) 1))
        :effect (and (light_on) (light_action_done))
    )
)