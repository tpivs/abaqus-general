#
# Script to read data from odb file and save it to a csv file
#
from odbAccess import *
import sys
odb = openOdb('Impact-Simulation.odb')
step1 = odb.steps['Impact']
# Edit the line below to enter the correct node number
region = step1.historyRegions['Node SPHERE-1.nn']
displacementData = region.historyOutputs['U2'].data
nn = len(displacementData)
dispFile = open('disp.csv','w')
for i in range(0, nn):
 dispFile.write('%10.4E,%10.4E \n’%(displacementData[i][0], displacementData[i][1]))
dispFile.close()
