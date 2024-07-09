(define (problem simple_robot_problem)
  (:domain simple_robot)
  
  (:objects
    light1 - light
    light_sensor - sensor
  )

  (:init
    (off light1)
    (value-low light_sensor)
  )

  (:goal 
    (value-high light_sensor)
  )
)