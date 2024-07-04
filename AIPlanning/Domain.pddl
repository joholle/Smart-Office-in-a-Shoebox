;Header and description

(define (domain office_space)

;remove requirements that are not needed
(:requirements :strips :fluents :durative-actions :timed-initial-literals :typing :conditional-effects :negative-preconditions :duration-inequalities :equality)



; un-comment following line if constants are needed
;(:constants )

(:predicates ;todo: define predicates here
    (light_on)
    (windows_open)
    (air_cooler_on)
    (water_spender_on)
)


(:functions ;todo: define numeric functions here
    (light)
    (humidity)
    (temperature)
    (water_level)
)

;define actions here
(:action turn_on_light
    :parameters ()
    :precondition (< (light) 10)
    :effect (and (light_on)) 
)

(:action open_window
    :parameters ()
    :precondition (or
        (> (humidity) 10)
        (> (temperature) 10)
    )
    :effect (and 
        (windows_open)
        (air_cooler_on)    
    ) 
)

(:action fill_up_water
    :parameters ()
    :precondition (= (water_level) 0)
    :effect (and (water_spender_on))
)
)