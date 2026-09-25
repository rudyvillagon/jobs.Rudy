class Person:


    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
        


class Bus:


    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []



    def board_passenger(self, Person):   
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(Person) 
            print(f"\n{Person} is getting ON ✅ the Bus")
            if self.passengers == self.max_passengers:
                print("\n---the Bus is Completely Full---")
                

    def exit_one_passen(self, Person):
        if Person in self.passengers:
            self.passengers.remove(Person)
            print(f"\n{Person} is getting OFF ❌ the Bus")
            if self.passengers == 0:
                print("\nThe Bus is Empty...")   

P1 = Person("Mario")
P2 = Person("Sara")
P3 = Person("Carlos")
P4 = Person("Sofia")

bus_ten = Bus(10)

bus_ten.board_passenger(P1)
bus_ten.board_passenger(P2)
bus_ten.exit_one_passen(P1)
bus_ten.board_passenger(P3)
bus_ten.exit_one_passen(P2)
bus_ten.board_passenger(P1)
bus_ten.board_passenger(P2)
bus_ten.board_passenger(P4)