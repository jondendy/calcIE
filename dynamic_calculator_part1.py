
import streamlit as st

# Title of the app
st.title('Dynamic Calculator')

# Slider for selecting the number of variables
num_vars = st.slider('Select number of variables', 2, 6, 2)

# Input fields for each variable
dynamic_inputs = []
for i in range(num_vars):
    dynamic_inputs.append(st.number_input(f'Variable {i+1}', value=0.0))

# Selectbox for choosing operators
operators = ['+', '-', '*', '/']
selected_operators = []
for i in range(num_vars - 1):
    selected_operators.append(st.selectbox(f'Operator {i+1}', operators))

# Display the inputs and operators
st.write('Variables:', dynamic_inputs)
st.write('Operators:', selected_operators)
