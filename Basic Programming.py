
#automobile class that will be used by a dealership as a vehicle inventory program.  The following attributes should be present in your automobile class:
#private string make
#private string model
#private string color
#private int year
#private int mileage
#constructor
#add a new vehicle
#remove a vehicle
#update vehicle attributes


class Automobile:
    def __init__(self):
        self.year = 0
        self.make = " "
        self.model = " "
        self.color = " "
    self.mileage = 0
        
    def add_vehicle(self):
        try:
            self.year = int(input("Vehicle year: "))
        except ValueError:
            self.year = int(input("Must be numeric: "))
        self.make = input("Vehicle make: ")
        self.model = input("Vehicle model: ")
        self.color = input("Vehicle color: ")
        try:
            self.mileage = int(input("Vehicle mileage (no commas): "))
            return True
        except ValueError:
        self.mileage = int(input("Do not use comma when entering mileage:"))
            
    def __str__(self):
        return('%d %s %s Color: %s Mileage: %d' %
              (self.year, self.make, self.model, self.color,
        self.mileage))
       

Inventory = []

def edit(Inventory):
    pos = int(input('Which vehicle is needs to be edited?: '))
    new_vehicle = car.add_vehicle()
    new_vehicle = car.__str__()
    Inventory[pos-1] = new_vehicle
    print('Vehicle was updated')

user=True
while user:
    print ("""
    Options:
    1.Add a Vehicle
    2.Remove a Vehicle
    3.Update Inventory
    4.View Inventory
    5.Ouput all vehicle inventory to txt file
    """)
    response=input("Choose an option:") 
    if response=="1": 
        car = Automobile()
        car.add_vehicle()
        Inventory.append(car.__str__())
        print("Vehicle added")
    elif response=="2":
        for i in Inventory:
            Inventory.pop(int(input("Enter position of vehicle to be removed: ")))
            print("Vehicle has been successfully removed.")
    elif response=="3":
        if len(Inventory) < 1:
            print("There are no vehicles in inventory.")
            continue
        edit(Inventory)
    elif response=="4":
        if len(Inventory) < 1:
            print("There are no vehicles in inventory.")
        else:
            print(Inventory)
        
    elif response=='5':
        f = open ("vehicle.txt", "w")
        f.write(str(Inventory))
        f.write('/n')
        f.close
        f=open("vehicle.txt", "r")
    print(f.read())

