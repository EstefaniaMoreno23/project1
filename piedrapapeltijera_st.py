import random
import streamlit as st

st.title("My first streamlit Estefania´s App")  #para poner el titulo cuando se corra (es como la salida de RStudio )

options = ["Rock","Paper","Scissors"] #se hizo una lista []
user = st.selectbox("Select one option: ",options) #.selectbox sirve para q la salida sea una cajita con opciones


RandomOption = random.randint(0,2) #se pone randint porq rand de random e int de integer y aleatorios de 0 a 2
computer = options[RandomOption]

st.write("User selection: ", user) #el st.write es el mismo print pero se pone asi porq estamos en la libreria streamlit
st.write("Computer selection: ", computer) #print("Computer = ",computer)


if user == computer:
    st.header("Tie 😑")
elif user == "Rock" and computer == "Scissors":
    st.header("User win😊")
elif user == "Scissors" and computer == "Rock":
    st.header(" Computer win😒")  

##Otra forma de hacerlo del profe
elif user =="Paper":
    if computer =="Scissors":
        st.header("Computer win😒")
    else:
        if computer == "Rock":
            st.header(" User Win😊")

## Mi forma
elif user == "Scissors" and computer == "Paper":
    st.header(" User win😊")
elif user == "Rock" and computer == "Paper":
    st.header(" Computer win😒")


#st.markdown("[Link to my first web page] (http://www.myfirstwebpageEstefania.com)")

# para atualizar pip -->   python -m pip install --upgrade pip   copiar y pegarlo en Cmder

