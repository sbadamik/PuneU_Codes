# The following is a Python 3 code that will be used to test functions written in Funcs.py
# The main function is the function to run for appropriate outputs.

import Funcs

#-------------------------------------------------------------------------------------------------------------------------------------------

# # Testing the writing of XYZ
# Locations = [[1,1,0],[2,2,0],[3,3,0],[4,4,0]]

# Clearance = open("FirstText.xyz","w")
# Clearance.close();

# Funcs.WriteXYZ("FirstText.xyz",Locations)
# Locations[3][2] = 1
# Locations[3][1] = 5
# Locations[0][0] = 3
# Locations[0][1] = 3
# Locations[1][2] = 1
# Locations[1][0] = 4
# Locations[2][1] = 4
# Locations[2][0] = 4
# Funcs.WriteXYZ("FirstText.xyz",Locations)

#-------------------------------------------------------------------------------------------------------------------------------------------

# # Testing the reading of data from a file using Read_XYZ()
# Pos = Funcs.Read_XYZ("TestXYZ_3Val.xyz")

# print(Pos)

#-------------------------------------------------------------------------------------------------------------------------------------------

# # Testing the function in the scenario that the configuration doesnt't change between steps

# TestCase = [ [1,1,1], [2,2,2], [3,3,3], [5,5,5], [6,6,6], [9,9,9] ]
# n = 10

# print("original:\n")
# print(TestCase)

# EndCase = Funcs.No_Move(TestCase, n)

# print("\nfinal:\n")
# print(EndCase)

A = 8

B = 6

print((A*(A<B)))