#Hello I am Abeer Choubey and I will be making a rock paper scissors game which is very easy to play and is graphical
#I have uploaded this code on my YT
#This was made using replit and streamlit library
import random
import streamlit as st

st.title("ROCK PAPER SCISSORS")
st.header("This was made by Abeer Choubey")
choice = random.choice(['rock', 'paper', 'scissors'])
st.write("Select your choice below")
x = st.button("Rock")
y = st.button("Paper")
z = st.button("Scissors")
if x:
  if choice == 'rock':
    st.write("Tie!")
    pass
  elif choice == 'paper':
    st.write("You lose!")
    pass
  elif choice == 'scissors':
    st.write("You win!")
    pass
  pass
elif y:
  if choice == 'rock':
    st.write("You win!")
    pass
  elif choice == 'paper':
    st.write("Tie!")
    pass
  elif choice == 'scissors':
    st.write("You lose!")
    pass
  pass
elif z:
  if choice == 'rock':
    st.write("You lose!")
    pass
  elif choice == 'scissors':
    st.write("Tie!")
    pass
  elif choice == 'paper':
    st.write("You win!")
    pass
  pass
