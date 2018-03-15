import math

# Function to set up basic nXnXn grid to map on
def Make_Grid(n):
	Grid = [8888888] * n[0]								# Creating n rows
	for i in range(n[0]):
		Grid[i] = [8888888] * n[1] 						# Introducing n colums within n rows

	for i in range(n[0]):
		for j in range(n[1]):
			Grid[i][j] = [8888888] * n[2] 					# Adding n units within every row and column

	return Grid

#-------------------------------------------------------------------------------------------------------------------------------------------

# Function that introduces blocks within the grid
# n --> Size of total grid
# R --> Radius of intraversible regions
# Grid --> Empty grid to introduce blocks into
# Blocks --> Origin of every intraversible region with radius R
def Insert_Blocks(n, R, Grid, Blocks):
	
	R = math.ceil(R)

	for Loc in Blocks:
		for i in range(-R, R+1):
			for j in range(-R, R+1):
				for k in range(-R, R+1):
					if ((i*i)+(j*j)+(k*k)) <= (R*R):
						Grid[(Loc[0]+i)%n[0]][(Loc[1]+j)%n[1]][(Loc[2]+k)%n[2]] = 1111111

	return Grid

#-------------------------------------------------------------------------------------------------------------------------------------------

# Function defines the algorithm to map region with steps to the destination
def Map_Grid(n, Start, End, Grid):
	Grid[Start[0]][Start[1]][Start[2]] = 999999		# Defining the start position with 9999

	if Grid[End[0]][End[1]][End[2]] == 1111111:		# If the end is within an intraversible region, do not move.
		return Grid

	Grid[End[0]][End[1]][End[2]] = 0				# Define end as 0 to start step count

	# Algorithm explained on wikipedia as https://en.wikipedia.org/wiki/Pathfinding
	MainList = [End];							
	count = 0;

	while count < len(MainList):
		
		CurLoc = MainList[count];
		TestList = [];

		for i in range(-1,2):						# The following 3 for loops will iterate to check the 26 locations around a certain point.
			for j in range(-1,2):
				for k in range(-1,2):
					TestList.append([((CurLoc[0]+i)%n[0]),((CurLoc[1]+j)%n[1]),((CurLoc[2]+k)%n[2])])

		for TestLoc in TestList:					# A loop to identify which of the 26 positions need to be numbered as possible move points.
			if Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] == 999999:														# Test to identify start position and terminate program=
				return Grid

			elif Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] == 1111111:													# Test to identify intraversible locations
				pass

			elif Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] <= (Grid[CurLoc[0]][CurLoc[1]][CurLoc[2]] + 1):				# Test to check that the test location has minimum step count
				pass

			else:
				MainList = MainList + [TestLoc];
				Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] = (Grid[CurLoc[0]][CurLoc[1]][CurLoc[2]] + 1)					# Updating step count
		count = count + 1;

	return Grid


#-------------------------------------------------------------------------------------------------------------------------------------------

# The following functions appends the appropriate lines of code to an XYZ file
def Write_XYZ(FileName, Locations, Names):
	
	N_Atoms = len(Locations)

	with open(FileName,"a") as Path:
		Path.write(str(N_Atoms)+"\n")
		Path.write("Some Element\n")
		for i in range(0,N_Atoms):
			Path.write(Names[i]+"\t"+str(Locations[i][0]/10)+"\t"+str(Locations[i][1]/10)+"\t"+str(Locations[i][2]/10)+"\n")

		Path.close();

	return 0;

#-------------------------------------------------------------------------------------------------------------------------------------------

# This function is responsible for making a move in the correct cardinal direction

def Take_Step(n, CurrentPos, Grid):

	NewPosStep = 10000000;
	NewPos = [(CurrentPos[0]),(CurrentPos[1]),(CurrentPos[2])]

	for i in range(-1,2):						# The following 3 for loops will iterate to check the 26 locations around a certain point.
			for j in range(-1,2):
				for k in range(-1,2):
					x = (CurrentPos[0]+i)%n[0];
					y = (CurrentPos[1]+j)%n[1];
					z = (CurrentPos[2]+k)%n[2];
					if Grid[x][y][z] < NewPosStep:											# Confirming that the next step is less than our current step
						NewPosStep = Grid[x][y][z]
						NewPos = [x,y,z]
	
	return NewPos

#-------------------------------------------------------------------------------------------------------------------------------------------

def Read_XYZ(FileName):

	with open(FileName,"r") as Path:
		Positions = []
		Names = []

		N = int(Path.readline())

		Path.readline()
		for i in range(0,N):
			Atom = Path.readline().strip('\n').split('\t')
			Names.append(Atom[0])
			Positions.append( [ int(round(float(Atom[1])*10,0)), int(round(float(Atom[2])*10,0)), int(round(float(Atom[3])*10,0)) ] )

		Path.close();

	return [Names, Positions]

#-------------------------------------------------------------------------------------------------------------------------------------------

def No_Move(CurrentPos,n):

	NewPos = []

	for i in range(len(CurrentPos)):
		NewPos.append([ ((CurrentPos[i][0]+1)%n[0]), ((CurrentPos[i][1]+1)%n[1]), ((CurrentPos[i][2]+1)%n[2]) ])

	return NewPos

#-------------------------------------------------------------------------------------------------------------------------------------------

def Set_n(Start_Pos,Final_Pos):
	
	n = [0,0,0]

	Max_Start_X = max(CheckMax[0] for CheckMax in Start_Pos)
	Max_Start_Y = max(CheckMax[1] for CheckMax in Start_Pos)
	Max_Start_Z = max(CheckMax[2] for CheckMax in Start_Pos)

	Max_End_X = max(CheckMax[0] for CheckMax in Final_Pos)
	Max_End_Y = max(CheckMax[1] for CheckMax in Final_Pos)
	Max_End_Z = max(CheckMax[2] for CheckMax in Final_Pos)

	n[0] = (Max_Start_X * (Max_Start_X>=Max_End_X)) + (Max_End_X * (Max_Start_X<Max_End_X))
	n[1] = (Max_Start_Y * (Max_Start_Y>=Max_End_Y)) + (Max_End_Y * (Max_Start_Y<Max_End_Y))
	n[2] = (Max_Start_Z * (Max_Start_Z>=Max_End_Z)) + (Max_End_Z * (Max_Start_Z<Max_End_Z))

	return n