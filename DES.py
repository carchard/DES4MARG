__author__ = "Connor Archard"

# Diagram of the street that we are going to model
#
#=================================|  B |=============||       ||=============
#                                 |  i |                Stop 
#--Lake Street--------South Side--|  k |---Middle-----  Signal  ---North Side
#                                 |  e |                Light
#=================================|  s |=============||       ||=============
#     W
#     ^
#     |
#  S<-O->N
#     |
#     v
#     E
#

# imports
import numpy
import time
import Queue as qu

# enable flags
print_en = True

# data structures to track state of the simulation
global numNorthCars
global numNorthMiddleCars
global numSouthMiddleCars
global numSouthCars
numNorthCars = 0
numNorthMiddleCars = 0
numSouthMiddleCars = 0
numSouthCars = 0

global eventQueue
global currTime
eventQueue = qu.PriorityQueue() # insert tuples of (priorityNum, data)
                                # in this model, (startTime, event)
stopLightState = True # True = red/stop, False = green/go
currTime       = 0

# model parameters
muNCars     = 10
muSCars     = 20
sigNCars    = 10
sigSCars    = 15
muBike      = 30
sigBike     = 30
P_carSlows  = 0.5
P_bikeSlows = 0.5
greenDur    = 75
redDur      = 25
bikePassDur = 7

# parameters to track statistics and control simulaiton
endTime       = 4 * 60 * 60 # all units of time are in seconds
totalNumCars  = 0
totalWaitTime = 0

# class to handle event driven simulation
# Event types to care about:
# 0 - Start Event =============> 'START'
# 1 - North Car arrival =======> 'NA'
# 2 - North Car departure =====> 'ND'
# 3 - South Car arrival =======> 'SA'
# 4 - South Car departure =====> 'SD'
# 5 - Bike Path arrival =======> 'BA'
# 6 - Bike Path departure =====> 'BD'
# 7 - Middle North arrival ====> 'MNA'
# 8 - Middle North departurn ==> 'MND'
# 9 - Middle South arrival ====> 'MSA'
# 10 - Middle South departure => 'MSD'
# 11 = End event ==============> 'END'
class event():
	def __init__(self,eventType,startTime,duration):
		self.eventType = eventType
    self.startTime = startTime
    self.duration  = duration

  def printCurrentStatistics(self):
    # TO DO: print out the current time, event, relevant statistics for debugging
    pass

	def scheduleNextEvent(self):
    # Switch/case based on the current event type. Schedule the departure event and the
    # next arrival event of the current type
		pass

	def updateStatistics(self):
    # check the state variables as they stand, and update them based on the event type
		pass

def main():
  # create the end event
  endEvent = event(eventType='END',startTime=endTime,duration=0)
  eventQueue.put((endEvent.startTime,endEvent))

  # create the start event
  startEvent = event(eventType='START',startTime=currTime,duration=0)
  eventQueue.put((startEvent.startTime,startEvent))
	
  currEvent = eventQueue.get()
	while currEvent.eventType is not 'END':
    if print_en:
      currEvent.printCurrentStatistics()
		currEvent.scheduleNextEvent()
		currEvent.updateStatistics()
		currEvent = eventQueue.get()[-1]


if __name__ == "__main__":
  print 'Running Discrete Event Simulation'
  main()
