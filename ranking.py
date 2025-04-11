import os

# Función para cargar el ranking desde un archivo
def load_ranking():
    if os.path.exists("ranking.txt"):
        with open("ranking.txt", "r") as file:
            ranking = [line.strip().split(" - ") for line in file.readlines()]
            return [(entry[0], entry[1], int(entry[2])) for entry in ranking]
    return []

# Función para mostrar el ranking en consola
def show_ranking():
    ranking = load_ranking()
    ranking.sort(key=lambda x: x[2], reverse=True)
    print("Ranking:")
    for idx, entry in enumerate(ranking, start=1):
        print(f"{idx}. {entry[0]} - {entry[1]} - {entry[2]} puntos")
