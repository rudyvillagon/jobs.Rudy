from datetime import date


class User:
        
        date_of_birth: date

        def __init__(self, date_of_birth):
            self.date_of_birth = date_of_birth


        @property
        def age(self):
            today = date.today()
            return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )



def verifi(func):
    def wrapper(user: User,*args, **kwargs):
        
        if user.age < 18:
            raise ValueError (f" {user.age} Years, You do not have access because of your age ❌")
        return func( user,*args, **kwargs)
    return wrapper

@verifi
def starter(user : User):
    return f"\n{user.age} Years, Access Granted. ✅\n"



my_user = User(date(2010, 1, 1))
my_user2 = User(date_of_birth=date(2000, 1, 1))

try:
    
    print(starter(my_user2))
    print(starter(my_user))
    
except ValueError as e:
    print(f"\nError:{e}\n")