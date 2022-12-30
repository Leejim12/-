fileName = 'tsp30.txt'
infile = open(fileName,'r')
line = infile.read()
temp = line.split("\n")
infile.close()
numCities = temp[0]
locations = temp[1:len(temp)-2]
print(numCities)
print(locations)
