
import streamlit as st
from PIL import Image, ImageDraw

# Title of the app
st.title('Enhanced Dynamic Calculator with Graphics')

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

# Household scaling
num_adults = st.number_input('Number of adults in household', min_value=0, value=1)
num_children = st.number_input('Number of children in household', min_value=0, value=0)

# Home size factor
home_type = st.selectbox('Type of home', ('Detached', 'Bungalow', 'Semi-detached', 'Flat'))
num_bedrooms = st.number_input('Number of bedrooms', min_value=1, value=1)

# Draw stick family with bodies
family_image = Image.new('RGB', (200, 100), color = (255, 255, 255))
draw = ImageDraw.Draw(family_image)
for i in range(num_adults):
    draw.ellipse((10 + i*30, 10, 30 + i*30, 30), fill=(0, 0, 0))
    draw.line((20 + i*30, 30, 20 + i*30, 60), fill=(0, 0, 0), width=2)
for i in range(num_children):
    draw.ellipse((10 + (num_adults + i)*30, 40, 30 + (num_adults + i)*30, 60), fill=(0, 0, 0))
    draw.line((20 + (num_adults + i)*30, 60, 20 + (num_adults + i)*30, 80), fill=(0, 0, 0), width=2)
st.image(family_image, caption='Family Representation')

# Draw home with different types
home_image = Image.new('RGB', (200, 100), color = (255, 255, 255))
draw = ImageDraw.Draw(home_image)
if home_type == 'Detached':
    draw.rectangle((50, 50, 150, 100), outline=(0, 0, 0))
    draw.polygon([(50, 50), (100, 20), (150, 50)], outline=(0, 0, 0))
elif home_type == 'Bungalow':
    draw.rectangle((50, 60, 150, 100), outline=(0, 0, 0))
elif home_type == 'Semi-detached':
    draw.rectangle((50, 50, 100, 100), outline=(0, 0, 0))
    draw.rectangle((100, 50, 150, 100), outline=(0, 0, 0))
    draw.polygon([(50, 50), (75, 20), (100, 50)], outline=(0, 0, 0))
    draw.polygon([(100, 50), (125, 20), (150, 50)], outline=(0, 0, 0))
elif home_type == 'Flat':
    draw.rectangle((50, 70, 150, 100), outline=(0, 0, 0))
st.image(home_image, caption='Home Representation')

# Perform calculation with BODMAS and scaling
try:
    # Example calculation logic
    result = inputs[0]
    for i in range(1, num_vars):
        if operators[i-1] == '+':
            result += inputs[i]
        elif operators[i-1] == '-':
            result -= inputs[i]
        elif operators[i-1] == '*':
            result *= inputs[i]
        elif operators[i-1] == '/':
            result /= inputs[i]

    # Apply household scaling
    result *= (num_adults + 0.5 * num_children)

    # Apply home size factor (simplified example)
    home_factor = {'Detached': 1.5, 'Bungalow': 1.2, 'Semi-detached': 1.0, 'Flat': 0.8}
    result *= home_factor[home_type] * num_bedrooms

    st.success(f'Result: {result}')
except Exception as e:
    st.error(f'Error: {str(e)}')

# Information text box
st.text_area('Calculator Information', 'This calculator helps you estimate energy consumption...')

# Load and apply CSS for thought bubble
with open('thought_bubble.css', 'r') as f:
    thought_bubble_css = f.read()

st.markdown(thought_bubble_css, unsafe_allow_html=True)
st.markdown('<div class="thought-bubble">Calculation results and information will appear here.</div>', unsafe_allow_html=True)
