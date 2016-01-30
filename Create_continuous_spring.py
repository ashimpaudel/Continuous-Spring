#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
#opening file to read the data and calculating radius and stuff
#!/usr/bin/env python
import os
import numpy
from Tkinter import *
import tkFileDialog as filedialog
import FileDialog
root = Tk()
root.withdraw()
import csv


print "Select the file to read the data from:"
ask = filedialog.askopenfilename(title = 'Sample data')
f = open( ask, "r")
csv_f = csv.reader(f)
biglist = []
datalength = 0
for row in csv_f:
    biglist.append(row)
    datalength += 1

#print len(biglist)
print 'datalenth = ' + str(datalength)

#extracting radius from biglist
length = len(biglist)
#calculating Radius
for i in range(length):
    a = 'r' + str((i+1))
    vars()[a] = biglist[i][0]

#calculating Length, this will calculate y1, y2, y3...
for i in range(length):
    b = 'y' + str((i+1))
    vars()[b] = biglist[i][1]




new_list = []

for i in range(length-1): #this will calculate L1, L2, L3.....
    c = 'L' + str((i+1))    
    distance = ((float(biglist[i+1][0]) - float(biglist[i][0]))**2 + (float(biglist[i+1][1]) - float(biglist[i][1]))**2)**0.5
    new_list.append(distance)
    vars()[c] = new_list[i]



n=72 # number of points along one revolution
modelName='Model-1'
partName='spring1'
#nt1=int(n*L1/p)+1 #total number of points
nt1=int(n*L1)+1 #total number of points


helixPoints=[]


my_dict={}
def calc_sum(n):
    sum1 = 0
    if n==0:
        return 0
    else:
        
        for i in range(0,n):
            L_value = 'L' + str(i+1)
            sum1 += eval(L_value)
        return sum1
    

z_previous = 0
for j in range(1, datalength):
    
    
    first_radius = 'r' + str(j)
    second_radius = 'r' + str (j+1)
    #print first_radius
    #print second_radius
    
    my_dict['first_radius'] = first_radius
    my_dict['second_radius'] = second_radius
    a = my_dict['second_radius']
    
    #print my_dict
   
    for i in range (0, n):
        theta=float(i)*2*math.pi/n
        a2 = eval(my_dict['second_radius'])
        a1 = eval(my_dict['first_radius'])
        r=((float(a2)- float(a1))*(theta-(2*math.pi))/(2*math.pi))+ float(a2)
        
        x=r*(math.sin(theta))
        y=r*(math.cos(theta))
        L_value1 = 'L' + str(j-1)
        L_value2 = 'L' + str(j)

        #check if z should be up or down:
        
        #y_second = y2 and y_first = y1
        y_first = 'y' + str(j)
        y_second = 'y' + str(j+1)
        difference = float(eval(y_second)) - float(eval(y_first))
        z = z_previous+(((difference)/n) * i)
        #print (((difference)/n) * i)
##        if difference > 0:
##            z = calc_sum(j-1) + (eval(L_value2) / n) * i
##        elif difference == 0:
##            z = z
##        elif difference <0:
##            z= calc_sum(j-1) - (eval(L_value2) / n) * i

        

            
        helixPoints.append((x, y, z))
    z_previous = z
    
    

x1=[]
y1=[]
z1=[]
ik=0
for i in helixPoints:
    print i
    ik+=1
    if ik == 73 or ik == 73*2 or ik == 73*3 or ik ==73*4:
        print 'aaaaa'
        print '\n \n \n'
    x1.append(i[0])
    y1.append(i[1])
    z1.append(i[2])


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, z1)
plt.show()
