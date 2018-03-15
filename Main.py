# This file holds the core main function used to run the pathing algorithm for atoms

import Funcs

# Deciding Grid Sizing
n = [83,74,1];

# Random radius since minimum distance in our code is 0.25nm = 2.5 Angstrom = 25 to scale
R = 7;

# Reading initial and final positions of all atoms
[Names,Start_Pos] = Funcs.Read_XYZ("Graphene_Init.xyz")
Final_Pos = Funcs.Read_XYZ("Graphene_Final.xyz")[1]

# n = Funcs.Set_n(Start_Pos,Final_Pos)
# print(n)

# Setting up required calculation variables that must be initialized for looping
Current_Pos = Start_Pos[:]
LastPos =  []

AtomN = len(Start_Pos)
CompCounter = 0;



# Identifying atoms that are already at destination
for i in range(AtomN):
	if Start_Pos[i]==Final_Pos[i]:
		CompCounter = CompCounter + 1

# Setting up output file
ClearFile = open("AllData.xyz","w")
ClearFile.close()

Funcs.Write_XYZ("AllData.xyz",Start_Pos, Names)

# Iterating the motion
# Each iteration of the while loop is one step for all atoms
while Current_Pos != Final_Pos:

	CompCounter = 0

	LastPos = [Temp[:] for Temp in Current_Pos]

	# Each iteration of the for considers one step for a different atom
	for i in range(AtomN):
		Blocks = []

		if Current_Pos[i]!=Final_Pos[i]:
			
			# Define intraversible locations
			for j in range(AtomN):
				if i!=j:
					Blocks.append(Current_Pos[j])

			Base_Grid = Funcs.Make_Grid(n)
			User_Grid = Funcs.Insert_Blocks(n, R, Base_Grid, Blocks)
			Mapd_Grid = Funcs.Map_Grid(n, Current_Pos[i], Final_Pos[i], User_Grid)
			Move_Step = Funcs.Take_Step(n, Current_Pos[i], Mapd_Grid)

			Current_Pos[i][0] = Move_Step[0]
			Current_Pos[i][1] = Move_Step[1]
			Current_Pos[i][2] = Move_Step[2]

		# if Current_Pos[i] == Final_Pos[i]:
		# 	CompCounter = CompCounter + 1

	if Current_Pos == LastPos:
		Current_Pos = Funcs.No_Move(Current_Pos,n)
		print("A")

	Funcs.Write_XYZ("AllData.xyz", Current_Pos, Names)
	print("B")
