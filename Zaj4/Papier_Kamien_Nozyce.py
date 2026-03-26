import random
computer_points = 0
user_points = 0

def computer_move():
    n = random.randint(1, 3)
    if n == 1:
        return "Papier"
    elif n == 2:
        return "Kamien"
    elif n == 3:
        return "Nozyce"

def user_move():
    user_answer = input("Podaj odpowiednią cyfrę: \n1 - Papier, \n2 - Kamien, \n3 - Nozyce, \n4 - stop\n")
    if user_answer == "1":
        return "Papier"
    elif user_answer == "2":
        return "Kamien"
    elif user_answer == "3":
        return "Nozyce"
    elif user_answer == "4":
        stop = True

def result_move(computer_points, user_points):
    if computer_move() == user_move():
        computer_points += 0.5
        user_points += 0.5
        print("Wynik tej rundy to remis")
        return computer_points, user_points
    elif computer_move() == "Papier" and user_move() == "Kamien":
        computer_points += 1
        print("Wynik tej rundy to wygrana komputera")
        return computer_points, user_points
    elif computer_move() == "Nozyce" and user_move() == "Papier":
        computer_points += 1
        print("Wynik tej rundy to wygrana komputera")
        return computer_points, user_points
    elif computer_move() == "Kamien" and user_move() == "Nozyce":
        computer_points += 1
        print("Wynik tej rundy to wygrana komputera")
        return computer_points, user_points
    elif computer_move() == "Papier" and user_move() == "Nozyce":
        user_points += 1
        print("Wynik tej rundy to wygrana gracza")
        return computer_points, user_points
    elif computer_move() == "Kamien" and user_move() == "Papier":
        user_points += 1
        print("Wynik tej rundy to wygrana gracza")
        return computer_points, user_points
    elif computer_move() == "Nozyce" and user_move() == "Kamien":
        user_points += 1
        print("Wynik tej rundy to wygrana gracza")
        return computer_points, user_points

while True:
    user_move()
    computer_move()
    print(f"Zagrałeś {user_move()}, a komputer zagrał {computer_move()}")
    result_move(computer_points, user_points)
    print(computer_points, user_points)
