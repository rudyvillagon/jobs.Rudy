class Bus:


    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.Person = 0



    def board_passenger(self):   
        if self.Person < self.max_passengers:
            self.Person += 1
            print(f"\ntheres 1 passengers getting ✅ On the Bus, there {self.Person} in total")
            if self.Person == self.max_passengers:
                print("\n---the Bus is Completely Full---")
                

    def exit_one_passen(self):
        if self.Person > 0:
            self.Person -= 1
            print(f"\ntheres 1 passengers getting ❌ Off the Bus, there {self.Person} passengers now in the bus")
            if self.Person == 0:
                print("\nThe Bus is Empty...")   

bus_ten = Bus(10)

bus_ten.board_passenger()
bus_ten.board_passenger()
bus_ten.exit_one_passen()
bus_ten.board_passenger()
bus_ten.exit_one_passen()
bus_ten.board_passenger()
bus_ten.board_passenger()
bus_ten.board_passenger()