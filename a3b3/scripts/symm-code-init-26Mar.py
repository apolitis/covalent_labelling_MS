#import wx
import re
#import os, numarray
import operator
from operator import itemgetter
#from numpy  import *
#from Numeric import *
from math import *
#from Numeric import * # imports numerical python
import csv


Nstart = raw_input("Enter the starting model number:  ")
NA = int(Nstart)
Nend = raw_input("Enter the end+1 model number:  ")
NB = int(Nend)


ReferenceAtom = raw_input("Enter the reference atom number:  ")
refAtom = int(ReferenceAtom)

ReferenceA = raw_input("Enter the ref atom number of the first subunit:  ")
refA = int(ReferenceA)

ReferenceB = raw_input("Enter the ref atom number of the second subunit:  ")
refB = int(ReferenceB)

ReferenceC = raw_input("Enter the ref atom number of the third subunit:  ")
refC = int(ReferenceC)

NumberAtoms = raw_input("Enter the number of atoms of the building block:  ")
Natoms = int(NumberAtoms)


listSym0 = []
listSym1 = []
listSym2 = []
listSym3 = []
listSym4 = []
listSym5 = []
listSym6 = []
listSym7 = []

listNames=[]

##Read input file
for i in range(NA,NB):
       InputFileName="models_9mer1."+str(i)+".mfj"
       def ReadFile(InputFile):
              InputFile = open(InputFileName,'r') # Open file to read
              InputFileLines = InputFile.read().splitlines() # string of lines from pdb file
              InputFile.close()
              return InputFileLines


       def coordinates(lines):
              outX=[]
              outY=[]
              outZ=[]
              outR=[]
              for i in lines[6:]:
                     l = re.findall ("(\S+)", i) 
                     X0 = float(l[0])
                     Y0 = float(l[1])
                     Z0 = float(l[2])
                     R0 = float(l[3])
                     outX.append(X0)
                     outY.append(Y0)
                     outZ.append(Z0)
                     outR.append(R0)
                     #print Scr2
              return outX, outY, outZ, outR
       b= coordinates(ReadFile(InputFileName))
       #print b[0][0]
       #coordinates(ReadFile(InputFileName))
       def getRefCoords(lines):
              Xref = (b[0][refAtom-1]+b[0][refAtom+Natoms-1]+b[0][refAtom+Natoms*2-1])/3
              Yref = (b[1][refAtom-1]+b[1][refAtom+Natoms-1]+b[1][refAtom+Natoms*2-1])/3
              Zref = (b[2][refAtom-1]+b[2][refAtom+Natoms-1]+b[2][refAtom+Natoms*2-1])/3
              return Xref, Yref, Zref

       ref = getRefCoords(ReadFile(InputFileName))

       def getDistancesAA(lines):
              DA1ref = sqrt(pow(b[0][refA-1]-ref[0], 2) + pow(b[1][refA-1]-ref[1], 2) + pow(b[2][refA-1]-ref[2], 2))
              DB1ref = sqrt(pow(b[0][refB-1]-ref[0], 2) + pow(b[1][refB-1]-ref[1], 2) + pow(b[2][refB-1]-ref[2], 2)) 
              DC1ref = sqrt(pow(b[0][refC-1]-ref[0], 2) + pow(b[1][refC-1]-ref[1], 2) + pow(b[2][refC-1]-ref[2], 2))
              
              DA2ref = sqrt(pow(b[0][refA+Natoms-1]-ref[0], 2) + pow(b[1][refA+Natoms-1]-ref[1], 2) + pow(b[2][refA+Natoms-1]-ref[2], 2))
              DB2ref = sqrt(pow(b[0][refB+Natoms-1]-ref[0], 2) + pow(b[1][refB+Natoms-1]-ref[1], 2) + pow(b[2][refB+Natoms-1]-ref[2], 2))
              DC2ref = sqrt(pow(b[0][refC+Natoms-1]-ref[0], 2) + pow(b[1][refC+Natoms-1]-ref[1], 2) + pow(b[2][refC+Natoms-1]-ref[2], 2))

              DA3ref = sqrt(pow(b[0][refA+Natoms*2-1]-ref[0], 2) + pow(b[1][refA+Natoms*2-1]-ref[1], 2) + pow(b[2][refA+Natoms*2-1]-ref[2], 2))
              DB3ref = sqrt(pow(b[0][refB+Natoms*2-1]-ref[0], 2) + pow(b[1][refB+Natoms*2-1]-ref[1], 2) + pow(b[2][refB+Natoms*2-1]-ref[2], 2))
              DC3ref = sqrt(pow(b[0][refC+Natoms*2-1]-ref[0], 2) + pow(b[1][refC+Natoms*2-1]-ref[1], 2) + pow(b[2][refC+Natoms*2-1]-ref[2], 2)) 
            
              return DA1ref, DB1ref, DC1ref, DA2ref, DB2ref, DC2ref, DA3ref, DB3ref, DC3ref,

       
       listNames.append(InputFileName)
       c = getDistancesAA(ReadFile(InputFileName))
          
       da1 = str(c[0])
       db1 = str(c[1])
       dc1 = str(c[2])

       da2 = str(c[3])
       db2 = str(c[4])
       dc2 = str(c[5])

       da3 = str(c[6])
       db3 = str(c[7])
       dc3 = str(c[8])

       scoreA = sqrt(pow((c[0]-c[3])+(c[0]-c[6]+(c[3]-c[6])), 2))
       scoreB = sqrt(pow((c[1]-c[4])+(c[1]-c[7]+(c[4]-c[7])), 2))
       scoreC = sqrt(pow((c[2]-c[5])+(c[2]-c[8]+(c[5]-c[8])), 2))
    
       TotalScore = scoreA+scoreB+scoreC

#       CenterDist_Score = sqrt(pow(c[3]-c[4], 2) + pow(c[4]-c[5], 2)+ pow(c[3]-c[5], 2))
#       AlphaDist_Score = sqrt(pow(c[0]-c[1], 2) + pow(c[1]-c[2], 2)+ pow(c[0]-c[2], 2)) # the error was here in the last  pow thing

       d6 = str(TotalScore)
#       d7 = str(AlphaDist_Score)

       print "Symmetry_Score" + d6
#       print "AlphaDist_Score" + d7
     
#       listSym0.append(d0)
#       listSym1.append(d1)
#       listSym2.append(d2)
#       listSym3.append(d3)
#       listSym4.append(d4)
#       listSym5.append(d5)
       listSym6.append(d6)
#       listSym7.append(d7)
   
       
       SummaryFileName = '9mer_symmetry_score-test.csv'
       SummaryFile = open(SummaryFileName, 'w')
       SummaryFile.write(str(listNames) +'\n')
#       SummaryFile.write(str(listSym0) +'\n')
#       SummaryFile.write(str(listSym1) +'\n')
#       SummaryFile.write(str(listSym2) +'\n')
#       SummaryFile.write(str(listSym3) +'\n')
#       SummaryFile.write(str(listSym4) +'\n')
#       SummaryFile.write(str(listSym5) +'\n')
       SummaryFile.write(str(listSym6) +'\n')
#       SummaryFile.write(str(listSym7) +'\n')
       


SummaryFile.flush()
SummaryFile.close()



        
        
        
