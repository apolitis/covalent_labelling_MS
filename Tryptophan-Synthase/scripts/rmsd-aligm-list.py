#  ultrafast code to compare molecular shapes
# get rmsds

import re
#import os, numarray
#import operator
#from operator import itemgetter
#from numpy  import 
from Numeric import *
from math import *
#from Numeric import * # imports numerical python
#from scipy import *
import csv
from scipy.stats import skew, kurtosis

import IMP
import IMP.atom
import IMP.algebra



Nstructures=raw_input("enter the number of structures : ")
Nstr=int(Nstructures)

Natomsinligand = raw_input("enter the number of atoms in ligands: ")
Natoms = int(Natomsinligand)
#Nspheres=raw_input("enter the number of spheres: ")
#Nsph=int(Nspheres)list

list = [39, 89, 132, 154, 252, 297, 299, 465, 491, 528, 555, 588, 605, 656, 752, 761, 794, 824, 920, 990, 1156, 1163, 1185, 1287, 1334, 1471, 1475, 1506, 1524, 1539, 1553, 1738, 1746, 1748, 1836, 1847, 1852, 1892, 1905, 2050, 2162, 2175, 2190, 2240, 2273, 2294, 2305, 2470, 2544, 2587, 2614, 2619, 2687, 2694, 2782, 2817, 2887, 3077, 3127, 3155, 3191, 3248, 3249, 3259, 3306, 3308, 3312, 3317, 3434, 3440, 3511, 3531, 3577, 3633, 3638, 3640, 3661, 3668, 3692, 3788, 3847, 3887, 4015, 4092, 4102, 4107, 4140, 4213, 4246, 4307, 4331, 4334, 4364, 4380, 4386, 4389, 4396, 4408, 4465, 4485, 4556, 4591, 4624, 4669, 4897, 4904, 4935, 4989]

#for i in range(0,Nstr):
for i in list:
       InFileName="OutPdb-rpn2-13."+str(i)+".pdb"

       def getRefStruct(InFile):
              InFile = open(InFileName,'r') # Open file to read
              InFileLines = InFile.read().splitlines() # string of lines from pdb file
              InFile.close()
              return InFileLines
       lines = getRefStruct(InFileName)
       def getCoords(lines):
              #outrM=[]
              outrX=[]
              outrY=[]
              outrZ=[]
              #outrR=[]
              for i in lines[0:946]:
	 	     if i.find('ATOM')>=0:
	                     l = re.findall ("(\S+)", i) 
                     	     #rM0=float(l[1])
                    	     rX0 = float(l[6])
                     	     rY0 = float(l[7])
                     	     rZ0 = float(l[8])
                     	     #rR0 = float(l[8])
                     	     #outrM.append(rM0)
                     	     outrX.append(rX0)
                     	     outrY.append(rY0)
                             outrZ.append(rZ0)
                     	     #outrR.append(rR0)
                    	 #print Scr2
	      return outrX, outrY, outrZ
		      
       z1 = getCoords(getRefStruct(InFileName))
       print z1[0], len(z1[0])
       
       #for i in range(85): 
              #if i.find('ATOM')>=0:
       #       ptsV1 = [(z1[0][i], z1[1][i], z1[2][i])] 

       listPointsV1 = []
       def getListPointsV1(lines):
              for i in range(Natoms):
		     pointsV1 = [z1[0][i], z1[1][i], z1[2][i]]
		     listPointsV1.append(pointsV1)
	      return listPointsV1
                            
              
       ptsV1= getListPointsV1(getRefStruct(InFileName))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


       list0 = []
       list1 = []
       list2 = []
       list3 = []
       list4 = []
       list5 = []
       list6 = []
       MA = 50000
       MB = 23000
       avD = 55.6
       listNames=[]
       ##Read input file
       #for j in range(0,Nstr):
       for j in list:
              InputFileName="OutPdb-rpn2-13."+str(j)+".pdb"
              #InputFileName="rpn3_cgall.mfj"
              def ReadFile(InputFile):
                     InputFile = open(InputFileName,'r') # Open file to read
                     InputFileLines = InputFile.read().splitlines() # string of lines from pdb file
                     InputFile.close()
                     return InputFileLines
       
              def coordinates(lines):
                     outX=[]
                     outY=[]
                     outZ=[]
                     #outR=[]
                     for i in lines[0:946]:
			    if i.find('ATOM')>=0:
				   l = re.findall ("(\S+)", i) 
				   X0 = float(l[6])
				   Y0 = float(l[7])
				   Z0 = float(l[8])
				   #R0 = float(l[8])
				   outX.append(X0)
				   outY.append(Y0)
				   outZ.append(Z0)
				   #outR.append(R0)
				   #print Scr2
		     return outX, outY, outZ #, outR
              b= coordinates(ReadFile(InputFileName))
              listPoints = []
              def getListPoints(lines):
                     for i in range(Natoms):
			     points = (b[0][i], b[1][i], b[2][i])
		             listPoints.append(points)
		     return listPoints
                                        
              pts= getListPoints(ReadFile(InputFileName))
              print i,j, len(pts) 
              # %%%%%%%%%%%%%%%%%%%%%%%%%%%
              #VecModels = [IMP.algebra.Vector3D(r) for r in [c[0], c[1], c[2], c[3], c[4], c[5]]]
              VecModels = [IMP.algebra.Vector3D(r) for r in pts]
              #       return VecModels
              #print VecModels
              #listV1 = [(13.7, 30.0, 23.7), (0.0, 30.0, 0.0), (-13.7, 30.0, 23.7), (23.8, 0.0, 29.7), (0.0, 0.0, -11.6), (0.5, 23.8, 12.0)]
              #v1 = [IMP.algebra.Vector3D(r) for r in [(13.7, 30.0, 23.7), (0.0, 30.0, 0.0), (-13.7, 30.0, 23.7), (23.8, 0.0, 29.7), (0.0, 0.0, -11.6), (0.5, 23.8, 12.0)]]
              v1 = [IMP.algebra.Vector3D(r) for r in ptsV1]
              #v2 = [IMP.algebra.Vector3D(r) for r in [(-7.965, 0.0, 14.988), (16.626, 0.0, 0.0), (-7.965, 0.0, -14.988), (-50.175, 2.75, 14.397), (25.188, -47.908, 24.659)]]
              #d = getVectors(ReadFile(InputFileName))
              #print "natural rmsd between v1 and v-models is: ", IMP.atom.get_rmsd(v1, VecModels)
              #natRMSD = IMP.atom.get_rmsd(v1, VecModels)

              print "natural rmsd between v1 and v-models is: ", IMP.atom.get_rmsd(v1, VecModels)
              natRMSD = IMP.atom.get_rmsd(v1, VecModels)
              tran = IMP.algebra.get_transformation_aligning_first_to_second(v1,VecModels)
              v3 = [tran.get_transformed(v) for v in v1]
              print "new rmsd is: ", IMP.atom.get_rmsd(VecModels,v3)
              newRMSD = IMP.atom.get_rmsd(VecModels,v3)

              
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    

              listNames.append(InputFileName)
                                                                   
              eRMSD = str(newRMSD)
              #eSA = str(SA)
   
              list0.append(eRMSD)
              #list1.append(eSA)

              # print list0
              # print list3
              SummaryFileName = 'rmsd_rpn2-13.'+str(i)+'.csv'
              SummaryFile = open(SummaryFileName, 'w')
              #SummaryFile.write(str(listNames) +'\n')
              #SummaryFile.write(str(list0) +'\n')
              #SummaryFile.write(str(list1) +'\n')
              #SummaryFile.write(str(list2) +'\n')
              SummaryFile.write(str(list0) +'\n')

       SummaryFile.flush()
       SummaryFile.close()



        
        
        
