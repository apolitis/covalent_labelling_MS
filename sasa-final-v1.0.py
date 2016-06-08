
# Code for calculating the solvent accessibility of many different structures
# Written by AP for interpreting covalent labelling followed by MS data

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

import sys

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
listSA = []


#Enter the list here
list = [4, 77, 92, 94, 146, 169, 173, 174, 175, 178, 195, 203, 204, 247, 271, 344, 359, 361, 413, 436, 440, 441, 442, 445, 462, 470, 471, 514, 585, 590, 593, 607, 619, 637, 648, 652, 656, 666, 711, 714, 719, 720, 723, 732, 745, 871, 890, 919, 921, 975, 980, 983, 997, 1009, 1027, 1038, 1042, 1046, 1056, 1101, 1104, 1109, 1110, 1113, 1122, 1135, 1261, 1280, 1309, 1311]

#for i in range(0,Nstr):
for i in range(0, Nstructs):
#       InFileName="OutPdb-rpn2-13."+str(i)+".pdb"
       m = IMP.Model()

       #! read PDB
       datadir = '/u/cvr/apolitis/docs-imp/CovalentLabelling/tryptophanSynth18Sept/run-sample4/pdbs/'
       file = str('TS-5k.'+str(i)+'.pdb')
       InputFileName="TS-5k."+str(i)+".pdb"
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
        

       def getSASA(surface_area):
           outSA = []
           for k in list:
               SA =surface_area[k-1]
               outSA.append(SA)
           return outSA
       #SA=getSASA(surface_area)
       #sSA = str(SA)
       Sw = getSASA(surface_area)

       Tscore = sum(Sw)
       print Sw, Tscore 

       listSv = []


       def getViolationsCL(surface_area, cutoff):
              if surface_area>cutoff:
                     vScore = 0.0
              else:
                     vScore = 1.0
              v_score = vScore
              return v_score



#calculate the sum of violations
       def getVScores(surface_area):
               for i in range(len(list)):
                       Sv = getViolationsCL(Sw[i], 0.3) # threshold defining that a residue is exposed or buried
                       listSv.append(Sv)
               return listSv
# print overall violation score
       Sviol = getVScores(Sw)
       print Sviol
       TotalVScore = sum(Sviol)
       print TotalVScore


       listNames.append(InputFileName)
       #eSASA = str(surface_area)
       eSF=str(Tscore)
       list3.append(eSF) 
  
       eSF2 = str(TotalVScore)
       list4.append(eSF2)

       SummaryFileName ='results-TS5k-cor-20Sept.csv'
       SummaryFile = open(SummaryFileName, 'w')
       SummaryFile.write(str(listNames) +'\n')
       SummaryFile.write(str(list3) +'\n')
       SummaryFile.write(str(list4) +'\n')

SummaryFile.flush()
SummaryFile.close()





        
        
        
