

def reader():
    with open(r"Semana8\Canciones.txt") as file:
        line = file.readlines()
        return line


def sort_song():
        
    all_song = reader()
    sorted_lines = sorted(all_song)
    for line in sorted_lines:
     print(line.strip())


sort_song()
