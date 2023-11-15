# -----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# -----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def hello():
    return app.send_static_file("index.html")


# write 'hello world' to the console
print("hello world")


valid_choices = ["rock", "paper", "scissors"]
score = 0

while True:
    # Pedir al jugador que introduzca su elección
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validar la entrada del jugador
    if player_choice not in valid_choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Elegir una opción aleatoria para el oponente
    opponent_choice = random.choice(valid_choices)

    # Comparar la elección del jugador con la del oponente
    if player_choice == opponent_choice:
        print("Tie!")
    elif player_choice == "rock" and opponent_choice == "scissors":
        print("You win!")
        score += 1
    elif player_choice == "scissors" and opponent_choice == "paper":
        print("You win!")
        score += 1
    elif player_choice == "paper" and opponent_choice == "rock":
        print("You win!")
        score += 1
    else:
        print("You lose!")

    # Preguntar al jugador si quiere seguir jugando
    play_again = input("Play again? (y/n)").lower()
    if play_again != "y":
        break

# Mostrar la puntuación final del jugador
print(f"Your score: {score}")

