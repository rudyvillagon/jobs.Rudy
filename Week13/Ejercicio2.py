class Parameters:

    def __init__(self, list_Parameters):
        self.list_Parameters = list_Parameters
    
    

def Int_Review(func):
    def wrapper(*args, **kwargs ):
        
        for i, arg in enumerate(args):
            if not isinstance(arg, (int)):
                raise TypeError(f"The caracter {i+1} = ({arg}) its not a number")
        return func(*args, **kwargs)
    return wrapper

@Int_Review
def list_par(a, b):
    return a , b 

print(list_par(4, 3))
print(list_par("Q", 2 ))




