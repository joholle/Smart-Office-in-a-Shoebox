(define (domain simple_robot)
  (:requirements :strips :typing)
  
  (:types
    sensor actuator - objects
    light - actuator
  )

  (:predicates
    (on ?l - light)
    (off ?l - light)
    (on-overwrite ?l - light)
    (off-overwrite ?l - light)
    (value-low ?s - sensor)
    (value-high ?s - sensor)
  )

  (:action turn_on
    :parameters (?l - light ?s - sensor)
    :precondition (and (off ?l) (value-low ?s))
    :effect (and (on ?l) (value-high ?s) (not (off ?l)) (not (value-low ?s)))
  )

  (:action force_on
    :parameters (?l - light ?s - sensor)
    :precondition (on-overwrite ?l)
    :effect (and (on ?l) (value-high ?s) (not (on-overwrite ?l)) (not (value-low ?s)))
  )

  (:action turn_off
    :parameters (?l - light ?s - sensor)
    :precondition (off-overwrite ?l)
    :effect (and (off ?l) (value-low ?s) (not (on ?l)) (not (off-overwrite ?l)) (not (value-high ?s)))
  )
)