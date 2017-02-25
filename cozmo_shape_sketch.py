#!/usr/bin/env python3

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

shape_sides = 10

def cozmo_program(robot: cozmo.robot.Robot):

    robot.move_lift(-3)

    for _ in range(shape_sides):
        
        robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()

        robot.move_lift(3)

        robot.drive_straight(distance_mm(75), speed_mmps(50)).wait_for_completed()
        
        robot.turn_in_place(degrees(360/shape_sides)).wait_for_completed()
        
        robot.drive_straight(distance_mm(-75), speed_mmps(50)).wait_for_completed()

        robot.move_lift(-3)
        
cozmo.run_program(cozmo_program)
