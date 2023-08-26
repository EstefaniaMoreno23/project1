import random
import streamlit as st

st.title("My first streamlit")  #para poner el titulo cuando se corra (es como la salida de RStudio )

options = ["Piedra","Papel","Tijera"] #se hizo una lista []
user = st.selectbox("Select one option: ",options) #.selectbox sirve para q la salida sea una cajita con opciones


RandomOption = random.randint(0,2) #se pone randint porq rand de random e int de integer y aleatorios de 0 a 2
computer = options[RandomOption]

st.write("User selection: ", user) #el st.write es el mismo print pero se pone asi porq estamos en la libreria streamlit
st.write("Computer selection: ", computer) #print("Computer = ",computer)


if user == computer:
    st.header("Empate 😑")
elif user == "Piedra" and computer == "Tijera":
    st.header("Gana User😊")
elif user == "Tijera" and computer == "Piedra":
    st.header("Gana Computer😒")  

##Otra forma de hacerlo del profe
elif user =="Papel":
    if computer =="Tijera":
        st.header("Gana Computer😒")
    else:
        if computer == "Piedra":
            st.header("Gana User😊")

## Mi forma
elif user == "Tijera" and computer == "Papel":
    st.header("Gana User😊")
elif user == "Piedra" and computer == "Papel":
    st.header("Gana Computer😒")


# para atualizar pip -->   python -m pip install --upgrade pip   copiar y pegarlo en Cmder

