import streamlit as st

# Title of the app
st.title('Dynamic Calculator with Operators')

# Number of variables
num_vars = st.slider('Enter the number of variables needed', 2, 6, 2)

# Create input fields and operator selectors
inputs = []
operators = []
for i in range(num_vars):
    value = st.number_input(f'Variable {i+1}', value=0.0)
    inputs.append(value)
    if i < num_vars - 1:
        operator = st.selectbox(f'Operator {i+1}', ('+', '-', '*', '/'))
        operators.append(operator)
result = 0
# Perform calculation
for i in range(1, num_vars):
    try:
        if operators[i-1] == '+':
            result += inputs[i]
        elif operators[i-1] == '-':
            result -= inputs[i]
        elif operators[i-1] == '*':
            result *= inputs[i]
        elif operators[i-1] == '/':
            result /= inputs[i]
    except ZeroDivisionError:
        st.error("Error: Division by zero")
    except TypeError:
        st.error("Error: Invalid input type")

st.success(f'Result: {result}')


















































