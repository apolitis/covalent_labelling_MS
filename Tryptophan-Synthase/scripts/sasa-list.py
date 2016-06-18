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
list = [..] 
#for i in range(0,Nstr):
for i in list:
#       InFileName="OutPdb-rpn2-13."+str(i)+".pdb"
       m = IMP.Model()

       #! read PDB
       datadir = '/u/cvr/apolitis/docs-imp/CovalentLabelling/testCode-Sasa-list/'
       file = str('OutPdbi_Cter-new.'+str(i)+'.pdb')

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

       print 'Surface area: ' +str(surface_area)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    

       listNames.append(file)
                                                                   
       eSASA = str(surface_area)
       #eSA = str(SA)
   
       list0.append(eSASA)
       #list1.append(eSA)

       # print list0
       # print list3
       SummaryFileName = 'out-testSASA.'+str(i)+'.csv'
       SummaryFile = open(SummaryFileName, 'w')
       #SummaryFile.write(str(listNames) +'\n')
       #SummaryFile.write(str(list0) +'\n')
       #SummaryFile.write(str(list1) +'\n')
       #SummaryFile.write(str(list2) +'\n')
       SummaryFile.write(str(list0) +'\n')

       SummaryFile.flush()
       SummaryFile.close()



        
        
        
