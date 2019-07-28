names = [ "PKM", "ALN", "GLN", "PKM", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
count1 = count2 = dict()
c_names = {}

#easy way
for ex in names:
    if ex not in count1:
        count1[ex]=1
    else:
        count1[ex]=count1[ex]+1
print(f'using \'in\' operator: {count1}')

#alternate way which is not working

for name in names:
    if c_names.get(name)==None:
        count2[name]=1
    else:
        count2[name]=count2[name]+1
print(f'using get method : {count2}')
