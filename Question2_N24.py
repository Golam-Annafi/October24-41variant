#2.a.i 
class Horse:
    def __init__(self, aname, amaxfenceheight, apercentage):
        self.__Name = aname   #string
        self.__MaxFenceHeight = amaxfenceheight   #integer
        self.__PercentageSuccess = apercentage   #integer
    
#2.a.ii 
    def GetName(self):
        return self.__Name 
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight 

#2..d 
    def Success(self, height, risk):
        if height > self.__MaxFenceHeight:
            success = self.__PercentageSuccess * 0.20
        else:
            if risk == 5:
                success =  self.__PercentageSuccess * 0.6
            elif risk == 4:
                success = self.__PercentageSuccess * 0.7
            elif risk == 3:
                success = self.__PercentageSuccess * 0.8
            elif risk == 2:
                success = self.__PercentageSuccess * 0.9
            elif risk == 1:
                success =  self.__PercentageSuccess * 1
        return success
            
#2.b.i
Horses = [] 

Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))

print(Horses[0].GetName())
print(Horses[1].GetName())

#2.c.i 
class Fence:
    def __init__(self, aheight, arisk):
        self.__Height = aheight    #integer
        self.__Risk = arisk     #integer
        
    def GetHeight(self):
        return self.__Height 
    def GetRisk(self):
        return self.__Risk 
    
#2.c.ii 
Course = []
for x in range(0, 4):
    valid = False
    while not valid:
        value1 = int(input("Enter height between 70 and 180: "))
        if value1 >= 70 and value1 <= 180:
            valid = True
    valid = False
    while not valid:
        value2 = int(input("Enter risk between 1 and 5: "))
        if value2 >= 1 and value2 <= 5:
            valid = True
    Course.append(Fence(value1, value2)) 
    
#2.e.i 
for y in range(0,2):
    for x in range(0, 4):
      chance = Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
      print(f"The horse {Horses[y].GetName()} at fence {x} has a {chance}% chance of success")

#2.e.ii
Averagesuccess = []
for y in range(0,2):
    total = 0
    for x in range(0,4):
        chance =  Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
        total += chance 
    average = total / 4
    Averagesuccess.append(average)
    print(f"{Horses[y].GetName()} has a average success chance of {average}%")
Highest = Averagesuccess[0]
winner = -1
for i in range(1,2):
    if Highest < Averagesuccess[i]:
        winner = i 
        Highest = Averagesuccess[i] 
print(f"{Horses[winner].GetName()} has the highest average chance of success with {Highest}%")