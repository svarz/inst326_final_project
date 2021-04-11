# Pseudocode:

Module 1 or Class Data_Read:
	"""Read in csv/dataset. Subset dataset. Return desired subset.
	"""

	def read_data():
		"""Read in dataset
		"""

	def subset_data():
		"""Subset the dataset into clean dataset
		"""

	def user_desired_data():
		"""Use GUI to obtain desired data from the user. Calculate and return the 
        requested data.
		"""



Module 2 or Class Calculations_Analysis:
	"""Perform the calculations and analysis with the subset that was passed in
	"""
import pandas as pd

Incorporate describe() or info() to find relevant information about the datasets(csv).

#Potential analysis:
#	Penalty minutes vs team loss
#		-use for loop to iterate through penalty minutes by players and record them
#   of team penalties vs team loss
#   Goals scored by certain players vs team win
#   Best players by age
#   Height vs individual success 
#   Fights by team vs wins (per season)
#   Fights vs # Penalties in a game
