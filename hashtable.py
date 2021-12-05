dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


hashmap = {}
i = 0 
for i in range(5):
    hashmap[i] = i 
print (hashmap) 

s_hashmap = {1:1}

for i in range(len(hashmap)):
    if s_hashmap[1] == hashmap[i]:
        print ("True")

    else:
         print("false")

print("------------------------------\n")

# Updating dictionary
dict['college'] = "HCC";
print(dict)
print("------------------------------\n")
# Delete dictinory
del dict['Name'];
print(dict)
print("------------------------------\n")
dict.clear();
print(dict)


