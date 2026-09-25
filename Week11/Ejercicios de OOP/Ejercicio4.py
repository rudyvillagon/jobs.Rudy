class Torso:
    def __init__(self, head, right_arm, right_leg, left_arm, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.right_leg  = right_leg
        self.left_arm = left_arm
        self.left_leg = left_leg



class Head:
    def __str__(self):
        return "Head 👨"
        

class Hand:
    def __str__(self):
        return "Hand 🖐"


class Arm:
    def __init__(self, hand):
        self.hand = hand
    
    def __str__(self):
        return f"Arm 💪 with {self.hand}"


class Feet:
    def  __str__(self):
        return "feet 🦶"


class Leg:
    def __init__(self, feet):
        self.feet = feet
    
    def __str__(self):
        return f"Leg 🦵 with {self.feet}"        

head = Head()

left_hand = Hand()
left_arm = Arm(left_hand)
left_feet = Feet()
left_leg = Leg(left_feet)

right_hand = Hand()
right_arm = Arm(right_hand)
right_feet = Feet()
right_leg = Leg(right_feet)



class Human(Torso):
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        Torso.__init__(self, head, right_arm, left_arm, right_leg, left_leg)
    

    def viewer(self):
        print("\n===  You just created a human  ===")
        print("\nHead: ",self.head)
        print("Right arm: ", self.right_arm)
        print("Right leg: ", self.right_leg)
        print("Left arm: ", self.left_arm)
        print("left leg: ",self.left_leg)


person = Human(head, right_arm, right_leg, left_arm, left_leg)
person.viewer()