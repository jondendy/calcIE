
import streamlit as st

# Title of the app
st.title('Dynamic Calculator')

# Number of inputs
num_inputs = st.slider('Select number of inputs', 1, 6, 1)

# Create input fields
inputs = []
for i in range(num_inputs):
    value = st.number_input(f'Input {i+1}', value=0.0)
    inputs.append(value)

# Perform calculation
try:
    result = sum(inputs)  # Example calculation: sum of inputs
    st.success(f'Result: {result}')
except Exception as e:
    st.error(f'Error: {str(e)}')
