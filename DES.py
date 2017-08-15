__author__ = "Connor Archard"

import numpy
import time
import Queue as qu

# data structures to track state of the simulation
global nCarsQueue
global sCarsQueue
global bikeQueue
global eventQueue
global currTime
nCarsQueue = qu.Queue()
sCarsQueue = qu.Queue()
bikeQueue  = qu.Queue()
eventQueue = qu.Queue()
stopLightState = True # True = red/stop, False = green/go

# model parameters
muNCars  = 10
muSCars  = 20
sigNCars = 10
sigSCars = 15
muBike   = 30
sigBike  = 30
P_carSlows = 0.5
P_bikeSlows = 0.5

# parameters to track statistics and control simulaiton
endTime = 24 * 60 * 60 # all units of time are in seconds
totalNumCars = 0
totalWaitTime = 0

# class to handle event driven simulation
# Event types to care about:
# 0 - Start Event
# 1 - North Car arrival
# 2 - North Car departure
# 3 - South Car arrival
# 4 - South Car departure
# 5 - Bike Path arrival
# 6 - Bike Path departure
# 7 = End event
class event():
	def __init__(self,eventType,eventTime):
		pass

	def scheduleNextEvent(self):
		pass

	def updateStatistics(self):
		pass

def main():
	currEvent = eventQueue.get()
	while currEvent.eventType is not 'End':
		currEvent.scheduleNextEvent()
		currEvent.updateStatistics()
		currEvent = eventQueue.get()


if __name__ == "__main__":
  print 'Running Discrete Event Simulation'
  main()
