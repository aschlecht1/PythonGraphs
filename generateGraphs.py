# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:48:08 2022
@author: aschl
"""

import numpy as np

import matplotlib.pyplot as plt

"""
This function takes in lamda and NodeA's Throughput values for 
scenarios (a) and (b) for CSMA and CSMA/VCS and generate a line
plot with Throughput as a function of lamda
"""


def generateGraphs(lamda, graphType, nodeLetter, SingleCSMA,
                   MultipleCSMA, SingleCSMAwVCS,
                   MultipleCSMAwVCS, FairnessIndex_SingleCSMA, FairnessIndex_MultipleCSMA,
                   FairnessIndex_SingleCSMAwVCS, FairnessIndex_MultipleCSMAwVCS):
    if graphType == "Throughput" or (graphType == "Collisions" and nodeLetter == "A"):

        # line 1 points
        y1 = SingleCSMA
        x1 = lamda
        # plotting the line 1 points
        plt.plot(x1, y1, marker="D", label="Node " + nodeLetter + " Scenario_A CSMA")

        # line 2 points
        y2 = MultipleCSMA
        x2 = lamda
        # plotting the line 2 points
        plt.plot(x2, y2, marker="x", label="Node " + nodeLetter + " Scenario_B CSMA")

        # line 3 points
        y3 = SingleCSMAwVCS
        x3 = lamda
        # plotting the line 3 points
        plt.plot(x3, y3, marker="s", label="Node " + nodeLetter + " Scenario_A CSMA/VCS")

        # line 4 points
        y4 = MultipleCSMAwVCS
        x4 = lamda
        # plotting the line 4 points
        plt.plot(x4, y4, marker="o", label="Node " + nodeLetter + " Scenario_B CSMA/VCS")

        if graphType == "Throughput":
            # naming the y axis
            plt.ylabel(graphType + " (Kbps)")
        else:
            # naming the y axis
            plt.ylabel(graphType)

        # naming the x axis
        plt.xlabel('λ (fames/sec)')
        # giving a title to my graph
        plt.title(graphType + ' vs. λ for Node ' + nodeLetter)

        # show a legend on the plot
        plt.legend(bbox_to_anchor=(0.5, -0.5), loc='lower center')

        # function to show the plot
        plt.show()

    elif graphType == "Collisions" and nodeLetter == "C":

        """
        # line 1 points
        y1 = SingleCSMA
        x1 = lamda
        # plotting the line 1 points 
        plt.plot(x1, y1, marker="D", label = "Node " + nodeLetter + " Scenario_A CSMA")
        """
        # line 2 points
        y2 = MultipleCSMA
        x2 = lamda
        # plotting the line 2 points
        plt.plot(x2, y2, marker="x", label="Node " + nodeLetter + " Scenario_B CSMA")
        """
        # line 3 points
        y3 = SingleCSMAwVCS
        x3 = lamda
        # plotting the line 3 points 
        plt.plot(x3, y3, marker="s", label = "Node " + nodeLetter + " Scenario_A CSMA/VCS")
        """
        # line 4 points
        y4 = MultipleCSMAwVCS
        x4 = lamda
        # plotting the line 4 points
        plt.plot(x4, y4, marker="o", label="Node " + nodeLetter + " Scenario_B CSMA/VCS")

        # naming the y axis
        plt.ylabel(graphType)
        # naming the x axis
        plt.xlabel('λ (fames/sec)')
        # giving a title to my graph
        plt.title(graphType + ' vs. λ for Node ' + nodeLetter)

        # show a legend on the plot
        plt.legend(bbox_to_anchor=(0.5, -0.35), loc='lower center')

        # function to show the plot
        plt.show()

    else:
        # function to show the plot
        print("ohhyeah noo")

        # Calc Fairness Index (FI)
        # line 1 points
        y1 = FairnessIndex_SingleCSMA
        x1 = lamda
        # plotting the line 1 points
        plt.plot(x1, y1, marker="D", label="Fairness Index Scenario_A CSMA")
        # line 2 points
        y2 = FairnessIndex_MultipleCSMA
        x2 = lamda
        # plotting the line 2 points
        plt.plot(x2, y2, marker="x", label="Fairness Index Scenario_B CSMA")
        # line 3 points
        y3 = FairnessIndex_SingleCSMAwVCS
        x3 = lamda
        # plotting the line 3 points
        plt.plot(x3, y3, marker="s", label="Fairness Index Scenario_A CSMA/VCS")
        # line 4 points
        y4 = FairnessIndex_MultipleCSMAwVCS
        x4 = lamda
        # plotting the line 4 points
        plt.plot(x4, y4, marker="o", label="Fairness Index Scenario_B CSMA/VCS")

        # naming the y axis
        plt.ylabel("Fairness Index (FI)")
        # naming the x axis
        plt.xlabel('λ (fames/sec)')
        # giving a title to my graph
        plt.title("Fairness Index (FI)" + ' vs. λ for Scenarios with NodeA/NodeB')

        # show a legend on the plot
        plt.legend(bbox_to_anchor=(0.5, -0.5), loc='lower center')

        # function to show the plot
        plt.show()