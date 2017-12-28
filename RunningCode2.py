## Defination of all the functions required to generate environment


# Function to print square grid of any choice
def PrintGrid(a = []):
	for i in range(len(a)):
		for j in range(len(a[i])):
			print "%s\t" % (a[i][j]),
		print "\n"

	print "______________________________________________________________________________________________________________________________________________________________" 


# Create a n x n grid to map surface on along with approprite intraversible regions
# n is the size of the grid
# Blocks defines a n x 2 array where every row represents coordinates of the midpoint of an intraversible node. Each node is 3 units along the edge
def GridMaker(n, Blocks = []):
	Grid = ['.'] * n;
	for i in range(n):
		Grid[i] = ['.'] * n;

	for Point in Blocks:
		for i in xrange(-1,2):
			for j in xrange(-1,2):
				if (Point[0]+i)>=0 and (Point[0]+i)<n and (Point[1]+j)>=0 and (Point[1]+j)<n:
					Grid[Point[0]+i][Point[1]+j] = 111111;
	return Grid


# The function is designed to load a map on the terrain provided and implement the A* algorithm for shortest path
# n defines the size of the map
# Start is a 2 value list with coordinates for the starting point of the motion
# End is a  2 value list with coordinates for the destination of the object
# Grid provides a n x n  map of the terrain to be traversed
def MapGenerator(n, Start = [], End = [], Grid = []):
	Grid[Start[0]][Start[1]] = 808;
	Grid[End[0]][End[1]] = 0;

	MainList = [End];
	count = 0

	while count < len(MainList):

		StepC = MainList[count]
		TestList = [];

		for i in xrange(-1,2):
			for j in xrange(-1,2):
				if (StepC[0]+i)>=0 and (StepC[0]+i)<n and (StepC[1]+j)>=0 and (StepC[1]+j)<n:
					TestList.append([StepC[0]+i,StepC[1]+j])

		for TestLoc in TestList:

			if Grid[TestLoc[0]][TestLoc[1]] == 111111:										# Test for intraversable regions
				pass

			elif Grid[TestLoc[0]][TestLoc[1]] == 808:										# Test for concerned object
				pass

			elif Grid[TestLoc[0]][TestLoc[1]] <= (Grid[StepC[0]][StepC[1]]+1):				# Test for confirming minimized step count
				pass
			
			else:
				MainList = MainList + [TestLoc];
				Grid[TestLoc[0]][TestLoc[1]] = (Grid[StepC[0]][StepC[1]]+1)					# Updating step count

		count = count + 1

	Grid[Start[0]][Start[1]] = 'X';
	
	return Grid

# The function takes in the current position of a point on the mapped grid and determines the best next step to move towards on the Grid
# It then returns the new position that the element then has.
def MakeAMove (CurrentPos = [], MappedGrid = []):

	NewPosStep = 100
	for i in xrange(-1,2):
			for j in xrange(-1,2):
				if (CurrentPos[0]+i)>=0 and (CurrentPos[0]+i)<n and (CurrentPos[1]+j)>=0 and (CurrentPos[1]+j)<n:
					if MappedGrid[CurrentPos[0]+i][CurrentPos[1]+j] < NewPosStep:											# Confirming that the next step is less than our current step
						NewPosStep = MappedGrid[CurrentPos[0]+i][CurrentPos[1]+j]	
						NewPos = [(CurrentPos[0]+i),(CurrentPos[1]+j)]
	
	return NewPos


# The funtion converts unsorted user input into sorted lists
def SortPos(Pos = []):
	SinglePos = [0,0]
	NewPos = []
	for i in range(len(Pos)):
			SinglePos[i%2] = Pos[i]
			if (i%2) == 1:
				NewPos.append([SinglePos[0],SinglePos[1]]);

	return NewPos

																															## The following code is run by the interpreter first

n = 20 #input('Enter the size of the grid \n')

StartPos = []
FinalPos = [0]

# Take inputs repetitively until an equal number of coordinates are given
while len(StartPos) != len(FinalPos):
	StartPos = SortPos(map(int,raw_input('Would you please enter start coordinates of all atoms seperated by spaces (x1 y1 x2 y2....)\n').strip().split()))
	FinalPos = SortPos(map(int,raw_input('Would you please enter final coordinates of all atoms seperated by spaces (x1 y1 x2 y2....)\n').strip().split()))

	AtomN = len(StartPos)

	if AtomN!= len(FinalPos):
		print "\nSire! Number of starting coordinates must equal final coordinates. Find the missing coordinates por favor."
		print "Thou entered %d start values but %d end values.\n" % (len(StartPos),len(FinalPos))
	else:
		print "\nThank you my liege. \n"

BasicBlocks = [[19,19],[0,19]] #,[10,10],[4,11],[14,3],[12,7]];
CurrentPos = StartPos[:]
CompCounter = 0;

OutputGrid = GridMaker(n, BasicBlocks)
for i in range(AtomN):
	OutputGrid[CurrentPos[i][0]][CurrentPos[i][1]] = "P" + str(i+1);
	OutputGrid[FinalPos[i][0]][FinalPos[i][1]] = "D" + str(i+1);

PrintGrid(OutputGrid)
raw_input("\nHit enter to continue. \n")


while CompCounter < AtomN:

	for i in range(AtomN):

		if CurrentPos[i]!=FinalPos[i]:
			Blocks = BasicBlocks[:];
			for j in range(AtomN):
				if i!=j:
					Blocks.append(CurrentPos[j])

	 		WorkGrid = GridMaker(n,Blocks)
	 		MappedGrid = MapGenerator(n, CurrentPos[i], FinalPos[i], WorkGrid)

	 		MoveTo = MakeAMove(CurrentPos[i], MappedGrid)

	 		OutputGrid[CurrentPos[i][0]][CurrentPos[i][1]] = ".";
			CurrentPos[i] = MoveTo;
			OutputGrid[CurrentPos[i][0]][CurrentPos[i][1]] = "P" + str(i+1);

			if CurrentPos[i] == FinalPos[i]:
				CompCounter = CompCounter + 1
				print "\nYour Highness. Point %d has reached its destination\n" % (i+1)

			PrintGrid(OutputGrid)

			raw_input("\nHit enter to continue. \n")
			

print "\nCongratulations Your Majesty. The aim has been achieved. All atoms are in place.\n"