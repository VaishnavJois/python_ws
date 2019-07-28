#count the number of character in every element of the list
names = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]

print(list(map(lambda x:len(x),names)))

#capitalize

data = "Will,jack,john,ryan"

newL = data.split(',')

print(list(filter(map(lambda x:x.capitalize(),data.split(',')),lambda x:x.startswith('A'))))



