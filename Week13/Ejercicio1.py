class Inf_User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __repr__(self):
        return f"Inf_User(name={self.name}, age={self.age})"


def print_parameters(func):
    def wrapper(*args, **kwargs):
        print(f"\nLlamando a '{func.__name__}' con:")
        print(f"  Posicionales: {args}")
        print(f"  Nombrados: {kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' retornó: {result}\n")
        return result
    return wrapper    


@print_parameters
def new_user(name, age):
    return Inf_User(name, age)


new_user(name = "Pedro", age = 23)

