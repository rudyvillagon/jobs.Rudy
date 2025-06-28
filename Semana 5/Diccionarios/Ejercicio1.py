Hotel = {
    "Hotel name" : "California Resort",
    "Number of stars" : 5,
    "Rooms" : [
    {
            "number" : 1,
            "floor" : 2,
            "Price_for_night" : 150,
    },      
    {       "number" : 2,
            "Floor" : 2,
            "price_for_night" : 150,
    },           
    {
            "number" : 3,
            "floor" : 2,
            "Price_for_night" : 150,
    },        
    {
            "number" : 4,
            "floor" : 2,
            "Price_for_night" : 150,
     },      
    ],
   }  

Rooms = Hotel.items["Rooms"]
for key, value in Hotel.items():

    print(key)
    print(value)
    print(Rooms)