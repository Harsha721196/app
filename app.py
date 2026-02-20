import streamlit as st

st.title("Simple Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.write("Result:", a + b)
    elif operation == "Subtract":
        st.write("Result:", a - b)
    elif operation == "Multiply":
        st.write("Result:", a * b)
    elif operation == "Divide":
        if b != 0:
            st.write("Result:", a / b)
        else:
            st.error("Cannot divide by zero")