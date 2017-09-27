import random
class Resistor:
    def __init__(self,x,y,resist,group):
        self.position_x = x
        self.position_y = y
        self.resist = resist
        self.group = str(group)

    def get_position(self):
        return([self.position_x,self.position_y])

    def get_resist(self):
        return(int(self.resist))

    def get_connect(self):
        return(self.group_in,self.group_out)
    def get_group(self):
        return(self.group)
class Battery:
    def __init__(self,x,y,voltage,group):
        self.position_x = x
        self.position_y = y
        self.voltage = voltage
        self.group = group
    def get_position(self):
        print(self.position_x,self.position_y)
    def get_group(self):
        return(self.group)

    
def read_object(path):
    object = open(path, 'r')
    ObjectArray = object.read().splitlines()

    for index in range(len(ObjectArray)):
        ObjectArray[index] = ObjectArray[index].split()
    #print(ObjectArray[1])
    ObjectClassArray = []
    for index in range(len(ObjectArray)):
        if ObjectArray[index][0] == 'Res' :
            ObjectClassArray.append(Resistor(ObjectArray[index][1],ObjectArray[index][2],ObjectArray[index][3],ObjectArray[index][4]))

        if ObjectArray[index][0] == 'Bat' :
            ObjectClassArray.append(Battery(ObjectArray[index][1],ObjectArray[index][2],ObjectArray[index][3],ObjectArray[index][4]))

    return(ObjectClassArray)


def Generate_resistor(range_pos,renge_resist):
    Type = "Resi"
    x = random.randrange(0,range_pos,1)
    y = random.randrange(0,range_pos,1)
    group_in = random.randrange(0,5,1)
    group_out= random.randrange(0,5,1)
    resist = random.randrange(0,renge_resist,10)
    return([Type,x,y,resist,group_in,group_out])

def Generate_file(path):
    File = open(path,'w')
    FileText=[]

    for index in range(10):
        FileText.append(Generate_resistor(10,100))

    File.write(str(FileText))

def find_res_map(Objects):
    Resistor_map = []
    Resistor_paralel_map = []
    resist_posl_par = 0
    index_b = 0
    index = 0
    resist_paralel=0
    while index < len(Objects)-1:

        #print(Objects[index].get_group())
        #print(Objects[index].get_resist())
        group = Objects[index].get_group()[0]
        if group == 'Z' or group == 'U' and not group == "B":
            Resistor_map.append(Objects[index].get_resist())
            index +=1
        print(group,index)
        group = Objects[index].get_group()[0]

        if Objects[index].get_group()[0] == Objects[index+1].get_group()[0] and not group == 'Z' and not group == 'U' and not group == "B":
            index_b = index
            Resistor_paralel_map.clear()
            resist_posl_par = 0
            resist_paralel=0
            print(resist_posl_par)
            print(index,'Paralel')
            while Objects[index_b].get_group()[0] == group and not group == 'Z':
                resist_posl_par = 0
                #print(index,'REDC')
                index = index_b
                group_2 = Objects[index].get_group()[1]
                if Objects[index_b].get_group()[1] == group_2 and not group_2 == '0':
                    while Objects[index_b].get_group()[1] == group_2 and not group_2 == '0':
                        resist_posl_par += Objects[index_b].get_resist()
                        #print(resist_posl_par,index_b,'WHILE')
                        index_b+=1
                if Objects[index_b].get_group()[1] == group_2 and group_2 == '0':
                    Resistor_paralel_map.append(Objects[index_b].get_resist())
                    index_b +=1
                if resist_posl_par>0:
                    Resistor_paralel_map.append(resist_posl_par)
                #print(Resistor_paralel_map,'LIST')
                index = index_b
                #print(Resistor_paralel_map,index)
            count = 0
            while count < (len(Resistor_paralel_map)):
                resist_paralel += 1 / Resistor_paralel_map[count]
                count +=1
                #print(resist_paralel,"MOR")
            if resist_paralel > 0:
                resist_paralel = 1 / resist_paralel
            Resistor_map.append(resist_paralel)
            index = index_b
            #print(Resistor_paralel_map,'LIST')
        elif group == 'Z' or group == 'U' and not group == "B":
            Resistor_map.append(Objects[index].get_resist())
            index +=1
        group = Objects[index].get_group()[0]
        print(index)
        index_b = index
    index_c = 0
    while index_c < len(Resistor_map):
        if Resistor_map[index_c] == 0:
            #print(Resistor_map,index_c)
            Resistor_map.pop(index_c)
        index_c+=1
    index_c = 0
    while index_c < len(Resistor_map):
        if Resistor_map[index_c] == 0:
            #print(Resistor_map,index_c)
            Resistor_map.pop(index_c)
        index_c+=1

    return(Resistor_map,"DER")

def check_connect(resistor_a,resistor_b):
    if resistor_a.get_group() == resistor_b.get_group() and not resistor_a == 'Z0' and not resistor_b == "Z0":
        return(True)
    else:
        return(False)
