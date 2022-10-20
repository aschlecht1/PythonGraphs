# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:34:51 2022

This is the main function, comments describing what we need to fill in

@author: aschl
"""
from typing import List, Any

import numpy as np

from generateGraphs import *
from station import *


slotDuration = 1 / np.power(10, 5)

rateOfArrivals = 200

simulationTime = 10

frameRate_Lambda = [100, 200, 300, 400, 700, 1000]
ThroughputA = []
ThroughputC = []

CollisionsA = []
CollisionsC = []

FairnessIndex = []

MaxTimeSec = 10
MaxTime = MaxTimeSec / slotDuration

stations: list[Station] = []




def setUpSingleCollisionDomain(FRLambda):
    stationA = Station("A")
    stationB = Station("B")
    stationC = Station("C")
    stationD = Station("D")

    stationA.setDestination("B")
    stationC.setDestination("D")

    stationA.addStationToDomain(stationB)
    stationA.addStationToDomain(stationC)
    stationA.addStationToDomain(stationD)

    stationB.addStationToDomain(stationA)
    stationB.addStationToDomain(stationC)
    stationB.addStationToDomain(stationD)

    stationC.addStationToDomain(stationA)
    stationC.addStationToDomain(stationB)
    stationC.addStationToDomain(stationD)

    stationD.addStationToDomain(stationA)
    stationD.addStationToDomain(stationB)
    stationD.addStationToDomain(stationC)

    stationA.generateTraffic(FRLambda, MaxTimeSec, slotDuration)
    stationC.generateTraffic(FRLambda, MaxTimeSec, slotDuration)

    stations.clear()
    print(stations)

    stations.append(stationA)
    stations.append(stationB)
    stations.append(stationC)
    stations.append(stationD)


def setUpHiddenTerminals(FRLambda):
    stationA = Station("A")
    stationB = Station("B")
    stationC = Station("C")

    stationA.setDestination("B")
    stationC.setDestination("B")

    stationA.addStationToDomain(stationB)

    stationB.addStationToDomain(stationA)
    stationB.addStationToDomain(stationC)

    stationC.addStationToDomain(stationB)

    stationA.generateTraffic(FRLambda, MaxTimeSec, slotDuration)
    stationC.generateTraffic(FRLambda, MaxTimeSec, slotDuration)

    stations.clear()
    print(stations)

    stations.append(stationA)
    stations.append(stationB)
    stations.append(stationC)


def setUpCSMAwCA():
    for s in stations:
        s.setVCS(False)


def setUpCSMAwVCS():
    for s in stations:
        s.setVCS(True)


# todo
def getNextTime():
    minTime = MaxTime
    for s in stations:
        t = s.getNextEventTime()
        if t != -1 and t < minTime:
            minTime = t
    return minTime


print("Program running")

for l in frameRate_Lambda:
    ThroughputA_lambda = []
    ThroughputC_lambda = []
    CollisionsA_lambda = []
    CollisionsC_lambda = []
    FairnessIndex_lambda = []
    for i in range(0, 4):
        print("Setup: Lambda " + str(l), end=" ")
        # set up Collision domain
        if i % 2 == 0:
            setUpSingleCollisionDomain(l)
            print("Single Collision Domain, ", end="")
        else:
            setUpHiddenTerminals(l)
            print("Hidden Terminals, ", end="")
        # set up CSMA
        if (i < 2):
            setUpCSMAwCA()
            print("CSMA /w Collision Avoidance \n\n")
        else:
            setUpCSMAwVCS()
            print("CSMA /w Virtual Carrier Sensing \n\n")

        # 0: Single Collision domain w/ collision Avoidance
        # 1: Hidden Terminals w/ collision Avoidance
        # 2: Single Collision domain w/ Virtual Carrier Sensing
        # 3: Hidden terminals w/ Virtual Carrier Sensing

        time = 0

        while time < MaxTime:
            # print("time: " + str(time))
            for s in stations:
                s.time_call(time)
            newTime = getNextTime()
            if (newTime < time):
                print("time Error: time=" + str(time) + "newtime=" + str(newTime))
            else:
                time = newTime

        throughputA = stations[0].T * 8000
        throughputA /= 10
        ThroughputA_lambda.append(throughputA)

        throughputC = stations[2].T * 8000
        throughputC /= 10
        ThroughputC_lambda.append(throughputC)

        CollisionsA_lambda.append(stations[0].N)
        CollisionsC_lambda.append(stations[2].N)

        FI = (stations[0].T + stations[0].N) / (stations[2].T + stations[2].N)
        FairnessIndex_lambda.append(FI)

        print("Number of Transmissions from " + stations[0].name + ": " + str(stations[0].T))
        print("Number of Transmissions from " + stations[1].name + ": " + str(stations[1].T))
        print("Number of Transmissions from " + stations[2].name + ": " + str(stations[2].T))
        # print("Number of Transmissions from " + stations[3].name + ": " + str(stations[3].T))
        print("Number of collisions from " + stations[0].name + ": " + str(stations[0].N))
        print("Number of collisions from " + stations[1].name + ": " + str(stations[1].N))
        print("Number of collisions from " + stations[2].name + ": " + str(stations[2].N))
        # print("Number of collisions from " + stations[3].name + ": " + str(stations[3].N))


    # todo use data to generate graphs

    # def generateTraffic(arg1, arg2):

    #    print(arg1 + arg2)
    ThroughputA.append(ThroughputA_lambda)
    ThroughputC.append(ThroughputC_lambda)
    CollisionsA.append(CollisionsA_lambda)
    CollisionsC.append(CollisionsC_lambda)
    FairnessIndex.append(FairnessIndex_lambda)



def column(matrix, i):
    return [row[i] for row in matrix]

#graphs for T for NodeA
generateGraphs(frameRate_Lambda, "Throughput", "A", column(ThroughputA, 0), column(ThroughputA, 1), column(ThroughputA, 2),
               column(ThroughputA, 3), 0, 0, 0, 0)
#graphs for T for NodeC
generateGraphs(frameRate_Lambda, "Throughput", "C", column(ThroughputC, 0),  column(ThroughputC, 1), column(ThroughputC, 2),
               column(ThroughputC, 3), 0, 0, 0, 0)
#graphs for N for NodeA
generateGraphs(frameRate_Lambda, "Collisions", "A", column(CollisionsA, 0),  column(CollisionsA, 1), column(CollisionsA, 2),
               column(CollisionsA, 3), 0, 0, 0, 0)
#graphs for T for NodeC
generateGraphs(frameRate_Lambda, "Collisions", "C", column(CollisionsC, 0),  column(CollisionsC, 1), column(CollisionsC, 2),
               column(CollisionsC, 3), 0, 0, 0, 0)
#graphs for T for NodeC
generateGraphs(frameRate_Lambda, "Fairness Index", "C", 0, 0, 0, 0, column(FairnessIndex, 0),  column(FairnessIndex, 1), column(FairnessIndex, 2),
               column(FairnessIndex, 3))


