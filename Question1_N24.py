#1.a
def ReadData(): 
    data = [] 
    try:
        file = open('Data.txt', 'r')
        for line in file:
            value = line.strip()
            data.append(value)
        file.close()
        return data
    except:
        print("file not found")
        
#b.i 
def FormatArray(array):
    result = ""
    for i in range(len(array)):
        result += " " + array[i]
    return result 

#b.ii 
stored_array = ReadData()
result = FormatArray(stored_array)
print(result)

#1.c 
def CompareStrings(val1, val2):
    count = 0
    found = False
    while not found:
        if val1[count] == val2[count]:
            count += 1
        else:
            found = True
            if val1[count] > val2[count]:
                return 1
            else:
                return 2

#1.d.i 
def Bubble(array):
    for x in range(0, len(array)):
        for y in range(0, len(array)-1-x):
            result = CompareStrings(array[y], array[y+1])
            if  result == 1:
                array[y], array[y+1] = array[y+1], array[y]
    return array

sorted = Bubble(stored_array)
sorted_format = FormatArray(sorted)
print(sorted_format)