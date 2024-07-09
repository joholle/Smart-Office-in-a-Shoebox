(define (problem simple_robot_problem)
  (:domain simple_robot)
  
  (:objects
    light1 - light
    light2 - light2
    light_sensor - sensor
    light_sensor2 - sensor2
  )

  (:init
    (off light1)
    (value-low light_sensor)
    (off light2)
    (value-low light_sensor2)
  )

  (:goal 
    (and (value-high light_sensor) (value-high light_sensor2))
  )
)