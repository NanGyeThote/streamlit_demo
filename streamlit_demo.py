import streamlit as st

st.title('This is an Authentic Loan Agency')
st.title('Business is :blue[cool] :sunglasses:')

number = st.number_input('Enter the amount you want to lend : ')
st.write('The initail amount is', number)

st.write('Total loan : ', 0.2*number+number)

option = st.selectbox(
   "How would you like to be received?",
   ("Cash", "Debit Card", "Visa"),
   index=None,
   placeholder="Select receive method...",
)

st.write("You selected:", option)
st.title('Do you agree the deal?')
agree = st.checkbox("I agree")

if agree:
    st.write("Yeah!We scam you haha")

