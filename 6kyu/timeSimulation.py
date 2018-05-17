#!/bin/python3

#When developing a game, it's often useful to be able to control time. We could slow it down when a character dies, or speed it up to make things look flashy, or stop time altogether when the player pauses the game.
#
#Let's write an object we can use to simulate time and mess with it as we wish!
#
#new SimTime()
#Creates a new SimTime instance. Nothing special here. Once an instance has been created, we can use its methods to play with time, and get the current "simulated" time.
#
#sim = SimTime()
#instance.get()
#Returns the current time withing the simulation. This value will start at 0.
#
#sim.get() == 0
#instance.set_speed(new_speed)
#At the current realtime and simtime, the simulation speed is set to new_speed.
#
#From the current realtime until the speed is changed again, simulated time should reflect this new speed.
#
#Note: speed can go negative and may lead simulated time "into the past".
#
#sim.set_speed(2)  # now each change in real time will be doubled for simulate time
#
#sim.set_speed(1)  # now changes in simulated time will be the same as in real time
#instance.update(current_realtime)
#Used to tell the simulation what the current time is outside, in the real world. This will be used to calculate the change in realtime, and therefore the change in simulated time.
#
#Real time only moves in one direction. So if current_realtime doesn't make sense (moves backwards), throw an error.
#
## assuming current speed is 1
#
#sim.update(10)
#sim.get() == 10
#Example:
## sim time = 0, real time = 0, sim speed = 1
#sim.update(12)
#sim.get() == 12
#sim.set_speed(3)
#
## from now onwards, change in realtime
## will be multiplied by the speed of 3
#
#sim.update(15)
## realtime changed by 3
## simtime should change by 3 * 3 = 9
## 12 + (3 * 3) = 21
#sim.get() == 21
#
#sim.update(17)    # adding 2 * 3 instead of 2 again
#sim.get() == 27
#sim.set_speed(1)
#
## from now on change in sim time
## will be multiplied by the speed of 1
#
#sim.update(18)    # adding 1 to sim time
#sim.get() == 28


class SimTime:

    def __init__( self ) :
        self.realtime = 0
        self.time = 0
        self.speed = 1
        
    def get( self ) :
        return self.time
        
    def set_speed( self, new_speed ) :
        self.speed = new_speed
        
    def update( self, current_realtime ) :
        if current_realtime < self.realtime :
            raise TimeGoBackError 
        self.time += ( current_realtime - self.realtime ) * self.speed
        self.realtime = current_realtime


if __name__ == "__main__" :
    sim = SimTime()
    sim.update( 12 )
    print( sim.get() )

    sim.set_speed( 3 )
    sim.update( 15 )
    print( sim.get() )
    
    sim.update( 17 )
    print( sim.get() )

    sim.set_speed( 1 )
    sim.update( 18 )
    print( sim.get() )
