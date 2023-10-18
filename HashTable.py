class HashTable:
    def __init__(self,size=7):
        self.data_map=[None] * size

    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash= (my_hash + ord(letter)*23) % len(self.data_map)
            return my_hash
        
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(f'{i} : {val}')
            # print(i, ": ", val)

    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hastTable=HashTable()
# my_hastTable.print_table()

# Setting some values in the hash table using hash and set_item function
print('After setting items')
my_hastTable.set_item('bolts',1400)
my_hastTable.set_item('washers',50)
my_hastTable.set_item('lumber',70)
my_hastTable.set_item('asutosh',70)
my_hastTable.set_item('ASUTOSH',70)
my_hastTable.set_item('ASUTOSH',70)
my_hastTable.set_item('ASUTOSH',70)
my_hastTable.print_table()

# Get method starts ---------
print('\n-----GET Method results below-----\n')
print(f"Getting value for the key 'bolts'   : {my_hastTable.get_item('bolts')}")
print(f"Getting value for the key 'washers' : {my_hastTable.get_item('washers')}")
print(f"Getting value for the key 'asutosh' : {my_hastTable.get_item('asutosh')}")
print(f"Getting value for the key 'ASUTOSH' : {my_hastTable.get_item('ASUTOSH')}")
print(f"Getting value for the key 'fhfhdk' : {my_hastTable.get_item('fhfhdk')}")

# Returning all keys of the Hash Table
print('\n-----Printing All the keys-----\n')
print(my_hastTable.keys())
