#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 06:57:47 2021

@author: markmathis
"""

#       AA         55555555555
#      AAAA        55555555555
#     AAAAAA       55     
#    AAAAAAAA      55    
#    AA    AA      55
#    AA    AA      55
#    AAAAAAAA      555555555555         
#    AAAAAAAA                55
#    AA    AA               555
#    AA    AA              555
#    AA    AA            555
#    AA    AA     555555555
#=================================================

#------------------------------------------#
# Title: CDInventory.py
# Desc: Script that askes a user to enter Album data and then
#       stores that data in a text file.
# MMathis, 2021-Feb-11, Started File
#          2021-Feb-14, Finished 
#------------------------------------------#
# 1. Display menu allowing the user to choose: 'Add CD', 'Display Current Inventory', 'Save Inventory to file' and 'exit'

CD_data={}  #data dictionary
strChoice = '' # User input
lstTbl = [] # list of lists to hold data
strFileName = 'CDInventory.csv'  # data storage file
objFile = None  # file object

# Get user Input
print('Write or Read file data.')
while True:   # established true argument
    print('\n[a] add data to list\n[w] to write data to file\n[r] to read data from file')
    print('[v] view all data\n[d] to delete a file\n[exit] to quit')
    strChoice = input('a, w, r, d, or exit: ').lower()  # all user input will be lower case
    print('\n\n')   # newlines to stack menu
    if strChoice == 'exit':  #exits program
        break
    
    if strChoice == 'a':   
     n = int(input("How many CD do you want to enter?: ")) #variable to loop input
     for i in range(n):  # number of times to loop
       keys = input("ID: ") #input key
       Artist = (input("Artist: "))  
       Album = (input("Album: "))
       CD_data[keys] = Artist, Album #Establish sictionary structure
       print("DATA ENTERED")
   
    elif strChoice == 'r':
         f = open(strFileName) # open test file
         with open(strFileName, 'r') as fileobj: # read textfile
          for row in fileobj:   #for statement to read data by row
           print( row.rstrip('\n') ) # strip newline character by row
           
    elif strChoice == 'w':
     import csv   #csv module
     f = open('CDInventory.csv','r')  #read text file
     reader = csv.reader(f) 
     for row in reader:   #for statement to read data by row
         CD_data[row][0]:{row[1],row[2]}  #import data and structure into dictionary
 
    elif strChoice == 'd':
         bgone = input("enter an ID# to delete: ")  #user input for row to delete
         for key in CD_data.keys():  #for statement
          if key == bgone:   #true condition for delete
           del CD_data[key]  #execute delete of row by key
         break
         print(CD_data)
         
    elif strChoice =='v': 
        print(CD_data)   # View data in dictionary
        
    else:     #if conditions are false execute next line
     print("\n Not Valid Choice Try again")
     
       