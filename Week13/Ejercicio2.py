class Parameters:

    def __init__(self, list_Parameters):
        self.list_Parameters = list_Parameters
    
    

def Int_Review(func):
    def wrapper(*args, **kwargs ):
        
        for i, arg in enumerate(args):
            if not isinstance(arg, (int, float)):
                raise TypeError(f"\nThe character {i+1} = ({arg}) its not a number ❌ \n")
            
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"\nThe keyword argument '{key}' = ({value}) is not a number ❌ \n")
            
        return func(*args, **kwargs)
    return wrapper

@Int_Review
def list_par(a, b):
    return a , b 


try:
    print(list_par(4, 3))
except TypeError as e:
    print("Error:", e)    

try:    
    print(list_par(a = "A", b = 98 ))
except TypeError as e:
    print("Error:", e)   

try:     
    print(list_par("Q", 2 ))
except TypeError as e:
    print("Error:", e)





