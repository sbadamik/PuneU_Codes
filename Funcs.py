# Function to set up basic nXnXn grid to map on
def Make_Grid(n):
	Grid = [8888888] * n								# Creating n rows
	for i in range(n):
		Grid[i] = [8888888] * n 						# Introducing n colums within n rows

	for i in range(n):
		for j in range(n):
			Grid[i][j] = [8888888] * n 					# Adding n units within every row and column

	return Grid

#-------------------------------------------------------------------------------------------------------------------------------------------

# Function that introduces blocks within the grid
# n --> Size of total grid
# R --> Radius of intraversible regions
# Grid --> Empty grid to introduce blocks into
# Blocks --> Origin of every intraversible region with radius R
def Insert_Blocks(n, R, Grid, Blocks):
	
	while Loc in Blocks:
		for i in range(-R, R+1):
			for j in range(-R, R+1):
				for k in range(-R, R+1):
					if ((i*i)+(j*j)+(k*k)) <= (R*R):
						Grid[(Loc[0]+i)%n][(Loc[1]+j)%n][(Loc[2]+k)%n] = 1111111

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
					TestList.append([((CurLoc[0]+i)%n),((CurLoc[1]+j)%n),((CurLoc[2]+k)%n)])

		while TestLoc in TestList:					# A loop to identify which of the 26 positions need to be numbered as possible move points.

			if Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] == 999999:														# Test to identify start position and terminate program
				return Grid

			elif Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] == 1111111:													# Test to identify intraversible locations
				pass

			elif Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] <= (Grid[CurLoc[0]][CurLoc[1]][CurLoc[2]] + 1):				# Test to check that the test location has minimum step count
				pass

			else:
				MainList = MainList + [TestLoc];
				Grid[TestLoc[0]][TestLoc[1]][TestLoc[2]] = (Grid[CurLoc[0]][CurLoc[1]][CurLoc[2]] + 1)					# Updating step count

	return Grid


#-------------------------------------------------------------------------------------------------------------------------------------------

# The following functions appends the appropriate lines of code to an XYZ file
def Write_XYZ(FileName, Locations):
	
	N_Atoms = len(Locations)

	with open(FileName,"a") as Path:
		Path.write(str(N_Atoms)+"\n")
		Path.write("Some Element\n")
		for i in range(0,N_Atoms):
			Path.write("C\t"+str(Locations[i][0])+"\t"+str(Locations[i][1])+"\t"+str(Locations[i][2])+"\n")

		Path.close();

	return 0;

#-------------------------------------------------------------------------------------------------------------------------------------------

# This function is responsible for making a move in the correct cardinal direction

def Take_Step(n, CurrentPos, Grid):

	NewPosStep = 1000000;
	NewPos = [(CurrentPos[0]),(CurrentPos[1]),(CurrentPos[2])]

	for i in range(-1,2):						# The following 3 for loops will iterate to check the 26 locations around a certain point.
			for j in range(-1,2):
				for k in range(-1,2):
					x = (CurrentPos[0]+i)%n;
					y = (CurrentPos[1]+j)%n;
					z = (CurrentPos[2]+k)%n;
					if Grid[x][y][z] < NewPosStep:											# Confirming that the next step is less than our current step
						NewPosStep = Grid[x][y][z]
						NewPos = [x,y,z]
	
	return NewPos

#-------------------------------------------------------------------------------------------------------------------------------------------

def Read_XYZ(FileName):

	with open(FileName,"r") as Path:
		Positions = []
		N = int(Path.readline())
		print(N)
		print("\n")
		Path.readline()
		for i in range(1,N+1):
			Atom = Path.readline().strip('\n').split('\t')
			Positions.append([float(Atom[1]),float(Atom[2]),float(Atom[3])])

		Path.close();

	return Positions
