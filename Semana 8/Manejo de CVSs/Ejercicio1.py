import csv


def all_games():
     
    num_of_games = input("How many games are you gonna register:  ")
    num_of_games = int(num_of_games) 
    counter = 0
    games_list =[]


    while counter < num_of_games:
        counter += 1
        Name = input("Enter the name of the Game: ")
        Genre = input("Enter the genre: ")
        Developer = input("Enter the developer: ")
        ESRB_clasification = input("And last the ESRB clasification: ")
        
        game_dic = {
            "Name" : Name,
            "Genre" : Genre,
            "Developer" : Developer,
            "ESRB Clasification" : ESRB_clasification


        }
        games_list.append(game_dic)
  

    return games_list    
  
def write_game_list(file_name,games_list):
    with open(file_name, "w" ,encoding="utf-8") as file:
        if games_list:
            writer = csv.DictWriter(file,fieldnames = games_list[0].keys())
            writer.writeheader()
            for game in games_list:

                writer.writerow(game)        



final_list = all_games()

write_game_list("game_list.csv",final_list)