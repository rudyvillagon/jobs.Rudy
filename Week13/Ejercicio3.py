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
    def wrapper(user: User,*args):
        
        if user.age < 18:
            raise ValueError (f" The User is {user.age} years old, not an Adult ❌")
        return func( user,*args)
    return wrapper

@verifi
def starter(user : User):
    return f"\nThe age of the user is {user.age} years old and is an adult. ✅\n"



my_user = User(date(2010, 1, 1))

try:
    print(starter(my_user))
except ValueError as e:
    print(f"\nErros:{e}\n")