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
#from scipy.stats import skew, kurtosis

import IMP
import IMP.atom
import IMP.algebra
import IMP.core
import IMP.saxs
import os



numberStructures = raw_input("enter the number of structures: ")
Nstructs = int(numberStructures)

#Natomsinligand = raw_input("enter the number of atoms in ligands: ")
#Natoms = int(Natomsinligand)
#Nspheres=raw_input("enter the number of spheres: ")
#Nsph=int(Nspheres)list
listNames = []
list0 =[]
list1 =[]
list2 =[]
list3 =[]
list4 =[]
list5 =[]
list6 =[]
list7 =[]
list8 =[]
list9 =[]
list10 =[]
list11 =[]
list12 =[]
list13 =[]
list14 =[]
list15 =[]
list16 =[]
list17 =[]
list18 =[]
list19 =[]
list20 =[]
list21 =[]
list22 =[]
list23 =[]
list24 =[]
list25 =[]
list26 =[]
list27 =[]
list28 =[]
list29 =[]
list30 =[]
list31 =[]
list32 =[]
list33 =[]
list34 =[]
list35 =[]
list36 =[]
list37 =[]
list38 =[]
list39 =[]

list40 =[]
list41 =[]
listTot =[]


list = [1, 3, 5, 7] 
#for i in range(0,Nstr):
for i in range(0, Nstructs):
#       InFileName="OutPdb-rpn2-13."+str(i)+".pdb"
       m = IMP.Model()

       #! read PDB
       datadir = '/u/cvr/apolitis/docs-imp/CovalentLabelling/benchAlphaBeta/runCL/'
       file = str('OutbAB.'+str(i)+'.pdb')
       InputFileName="OutbAB."+str(i)+".pdb"
       mp= IMP.atom.read_pdb(datadir + file, m,
       IMP.atom.NonWaterNonHydrogenPDBSelector(), True, True)
       #file = str(4merTTR_HM.pdb)

       #! select particles from the model
       particles = IMP.atom.get_by_type(mp, IMP.atom.ATOM_TYPE)

       #! add radius for water layer computation
       ft = IMP.saxs.default_form_factor_table()
       #for j in list:
       for j in range(0, len(particles)):
           radius = ft.get_radius(particles[j])
           IMP.core.XYZR.setup_particle(particles[j], radius)
       # compute surface accessibility
       s = IMP.saxs.SolventAccessibleSurface()
       surface_area = s.get_solvent_accessibility(IMP.core.XYZRs(particles))
        
       #for k in list:
       #    SA = surface_area[k-1]
       #    print SA


       def getSASA(surface_area):
           outSA = []
           for k in list:
               SA =surface_area[k-1]
               outSA.append(SA)
           return outSA
       SA=getSASA(surface_area)
       print SA       

       sa1 = surface_area[0]
       sa2 = surface_area[2]
       sa3 = surface_area[4]
       sa4 = surface_area[6]
       print sa1, sa2, sa3, sa4
#       sa42 = surface_area[949]
       #for k in list:
       #    sa
       #    print surface_area[k]
       #    list0.append(surface_area[k])
       #print 'Surface area: ' +str(surface_area)
#*****************************************
#       def getScoreCL(CL):
#              if CL>0.3:
#                     score1 = 1.0
#              else:
#                     score1 = 0.0
#              scoreCL = score1
#              return scoreCL
      
#       sr1 = getScoreCL(float(sa1)) 
#       sr2 = getScoreCL(float(sa2))
#       sr3 = getScoreCL(float(sa3))
#       sr4 = getScoreCL(float(sa4))
#       sr42 = getScoreCL(float(sa42))


#       Stot = sr1+sr2+sr3+sr4
#       print Stot

#       def getScoreCL2(CL):
#              outScore = []
#              for k in list:
#                  if CL>0.3:
#                         score1 = 1.0
#                  else:
#                         score1 = 0.0
#                  scoreCL = score1
#                  print scoreCL
#              return scoreCL
#       print getScoreCL2(SA)
       #for k in list:
       #    Stot2 = getScoreCL2(SA[k])
       #print Stot2
#*********************************

       listNames.append(InputFileName)
       #eSASA = str(surface_area)
       list1.append(sa1)
       list2.append(sa2)
       list3.append(sa3)
       list4.append(sa4)

#       listTot.append(Stot)

       #list0.append(eSASA)
       
       SummaryFileName ='test-Dev.csv'
       SummaryFile = open(SummaryFileName, 'w')
       SummaryFile.write(str(listNames) +'\n')
       #SummaryFile.write(str(list0) +'\n')
       SummaryFile.write(str(list1) +'\n')
       SummaryFile.write(str(list2) +'\n')
       SummaryFile.write(str(list3) +'\n')
       SummaryFile.write(str(list4) +'\n')
       
#       SummaryFile.write(str(listTot) +'\n')

SummaryFile.flush()
SummaryFile.close()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
#       for k in list:
 
#           listNames.append(file)
                                                                   
#           eSASA = str(surface_area)
           #eSA = str(SA)
   
#           list0.append(eSASA)
           #list1.append(eSA)

           # print list0
           # print list3
#           SummaryFileName = 'excel-testSASA.'+str(k)+'.csv'
#           SummaryFile = open(SummaryFileName, 'w')
           #SummaryFile.write(str(listNames) +'\n')
           #SummaryFile.write(str(list0) +'\n')
           #SummaryFile.write(str(list1) +'\n')
           #SummaryFile.write(str(list2) +'\n')
#           SummaryFile.write(str(list0) +'\n')

#       SummaryFile.flush()
#       SummaryFile.close()



        
        
        
