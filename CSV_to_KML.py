#!/usr/bin/python
# There are some file handling changes etc.
import csv

#Input the file name.

fname = raw_input("Enter file name including extension: ")
data = csv.reader(open(fname), delimiter = ',')

#Skip the 1st header row.

data.next()

#Get the name of the file to write out
output_file = fname.strip('csv')
f = open(output_file +'kml', 'w')

#Writing the kml file.
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
f.write("<Document>\n")
f.write("   <name>" + fname + '.kml' +"</name>\n")
for row in data:
    f.write("   <Placemark>\n")
    f.write("       <name>" + str(row[1]) + "</name>\n")
    f.write("       <description>" + str(row[0]) + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + str(row[3]) + "," + str(row[2]) + "," + str(row[4]) + "</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")
f.write("</Document>\n")
f.write("</kml>\n")

print "Writing file......"
f.close()
print " "
print "File Created. "
print "Press ENTER to exit. "

raw_input()
exit()
