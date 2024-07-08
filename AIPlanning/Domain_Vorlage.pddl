(define (domain office_space)

(:requirements :strips :typing :conditional-effects :negative-preconditions :equality :disjunctive-preconditions :numeric-fluents)


(:predicates 
    (light_on)
    (windows_open)
    (air_cooler_on)
    (water_spender_on)

    (force_light)
    (force_window)
    (force_cooler)
    (force_water)

    (is_raining)

    (light_action_done)
    (window_action_done)
    (water_action_done)
    (cooler_action_done)

    (no_action_possible)
)

;============================== sensor values ==============================

(:functions 
    (light)
    (humidity)
    (inside_temp)
    (water_level)

    
    (outside_temp)
)

;---------------------------------------------------------------------------
;============================== light actions ==============================
;---------------------------------------------------------------------------

(:action turn_on_light
    :parameters ()
    :precondition (and
        (< (light) 10)
        (not (light_on))
    )
    :effect (and 
        (light_on)
        (light_action_done)
    ) 
)

;============================== force light actions ==============================

(:action force_on_light
    :parameters ()
    :precondition (and
        (not (light_on))
        (force_light)
    )
    :effect (and 
        (light_on)
        (light_action_done)
    ) 
)

(:action force_off_light
    :parameters ()
    :precondition (and
        (light_on)
        (force_light)
    )
    :effect (and 
        (not (light_on))
        (light_action_done))
     
)

;----------------------------------------------------------------------------
;============================== window actions ==============================
;----------------------------------------------------------------------------
(:action open_window
    :parameters ()
    :precondition (and
        (or
            (> (humidity) 10)
            (> (inside_temp) 10)
        )
        (not (is_raining))
        (> (inside_temp) (outside_temp))
        (not (windows_open))
    )
    :effect (and 
        (windows_open)
        (window_action_done)
    ) 
)


(:action close_window
    :parameters ()
    :precondition (or 
        (and
            (< (humidity) 10)
            (< (inside_temp) 10)
            (windows_open)
        )
        (and
            (is_raining)
            (windows_open)
        )
    )
    :effect (and 
        (not (windows_open))
        (window_action_done)
    ) 
)
;--------------------------- force window actions ---------------------------
(:action force_close_window
    :parameters ()
    :precondition (and 
        (force_window)
        (windows_open)
    )
    :effect (and 
        (not (windows_open))
        (window_action_done)
    ) 
)

(:action force_open_window
    :parameters ()
    :precondition (and 
        (force_window)
        (not (windows_open))
    )
    :effect (and 
        (windows_open)
        (window_action_done)
    ) 
)
;----------------------------------------------------------------------------
;============================== cooler actions ==============================
;----------------------------------------------------------------------------
(:action turn_on_cooler
    :parameters ()
    :precondition (and
        (or
            (< (inside_temp) 10)
            (> (inside_temp) (outside_temp))
        )
        (not (air_cooler_on))
    )
    :effect (and
        (air_cooler_on)
        (cooler_action_done)          
    ) 
)

(:action turn_off_cooler
    :parameters ()
    :precondition (and
        (> (inside_temp) 10)
        (< (inside_temp) (outside_temp))
        (air_cooler_on)
    )
    :effect (and 
        (not (air_cooler_on))    
        (cooler_action_done)
    ) 
)
;--------------------------- force cooler actions ---------------------------

(:action force_turn_on_cooler
    :parameters ()
    :precondition (and
        (not (air_cooler_on))
        (force_cooler)
    )
    :effect (and 
        (air_cooler_on)    
        (cooler_action_done)
    ) 
)

(:action force_turn_off_cooler
    :parameters ()
    :precondition (and
        (air_cooler_on)
        (force_cooler)
    )
    :effect (and
        (not (air_cooler_on))    
        (cooler_action_done)
    ) 
)
;----------------------------------------------------------------------------
;=============================== water actions ==============================
;----------------------------------------------------------------------------
(:action fill_up_water
    :parameters ()
    :precondition (and
        (= (water_level) 0)
        (not (water_spender_on))
    )
    :effect (and 
        (water_spender_on)
        (water_action_done)    
    )
)

(:action stop_water
    :parameters ()
    :precondition (and
        (> (water_level) 10)
        (water_spender_on)
    )
    :effect (and 
        (not (water_spender_on))
        (water_action_done)    
    )
)

;============================== force water action ==============================

(:action force_fill_up_water
    :parameters ()
    :precondition (and
        (not (water_spender_on))
        (force_water)
    )
    :effect (and 
        (water_spender_on)
        (water_action_done)    
    )
)

;============================== no action possible ==============================

(:action no_action
    :parameters ()
    :precondition (not
        (or
                (< (light) 10)
                (and
                    (or
                        (> (humidity) 10)
                        (> (inside_temp) 10)
                    )
                    (not (windows_open))
                )
                (and
                    (> (inside_temp) 10)
                    (not (windows_open))
                )
                (= (water_level) 0)
        )
    )
    :effect (and (no_action_possible))
)

)