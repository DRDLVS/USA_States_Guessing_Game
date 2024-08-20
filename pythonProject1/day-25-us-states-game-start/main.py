import turtle
import pandas as pd

# Configurar la pantalla
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Cargar datos del archivo CSV
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


# Función para mostrar el nombre del estado en el mapa
def show_state_on_map(state_name, x, y):
    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x, y)
    state_turtle.write(state_name, align="center", font=("Arial", 7, "bold"))


# Bucle para permitir múltiples entradas del usuario
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state name?"
    ).title()


    if answer_state == "Exit":

        remaining_states = []
        for state in all_states:
            if state not in guessed_states:
                remaining_states.append(state)

        df = pd.DataFrame(remaining_states, columns=["State"])
        print(df)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv('states_to_learn.csv', index=True, index_label="Remaining States")
        break

    # Comprobar si el estado ingresado está en la lista y no ha sido adivinado antes
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Obtener las coordenadas del estado
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)

        # Mostrar el estado en el mapa
        show_state_on_map(answer_state, x, y)
    elif answer_state in guessed_states:
        print(f"Ya has adivinado {answer_state}. Intenta con otro estado.")






