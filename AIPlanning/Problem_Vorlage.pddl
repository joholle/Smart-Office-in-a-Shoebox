(define (problem pleasant_room) (:domain office_space)

(:init
    ;------ werden im template (durch verändern der Zahl) gesetzt ----
    (= (light) 5) 
    (= (humidity) 5)
    (= (inside_temp) 5)
    (= (water_level) 5)

    ; (wetter api)
    (= (outside_temp) 5)
    
    ;------ werden im template (durch auskommentieren/einkommentieren) gesetzt ----
    ; (wetter api)
    (is_raining)

    (force_light)
    (force_window)
    (force_cooler)
    (force_water)

    ;------ aktueller status, der vom letzten plan übernommen wird ----
    (light_on)
    (windows_open)
    (air_cooler_on)
    (water_spender_on)
)

(:goal (or
    (light_action_done)
    (window_action_done)
    (water_action_done)
    (cooler_action_done)
    (no_action_possible)
))


)
