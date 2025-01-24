import streamlit as st
from PIL import Image, ImageDraw
# Function to create a stick family image
def create_stick_family():
    img = Image.new('RGB', (200, 200), color='white')
    d = ImageDraw.Draw(img)
#     Draw stick figures
    d.line((50, 100, 50, 150), fill='black', width=3)  # Body
    d.ellipse((45, 80, 55, 90), fill='black')  # Head
    d.line((50, 120, 30, 140), fill='black', width=3)  # Left arm
    d.line((50, 120, 70, 140), fill='black', width=3)  # Right arm
    d.line((50, 150, 40, 180), fill='black', width=3)  # Left leg
    d.line((50, 150, 60, 180), fill='black', width=3)  # Right leg
    return img
 
Function to create home type images
def create_home_type(home_type):
    img = Image.new('RGB', (200, 200), color='white')
    d = ImageDraw.Draw(img)
    if home_type == 'Detached':
        d.rectangle((50, 100, 150, 150), outline='black', width=3)
        d.polygon([(50, 100), (100, 50), (150, 100)], outline='black', fill='grey')
    elif home_type == 'Bungalow':
        d.rectangle((50, 120, 150, 150), outline='black', width=3)
        d.polygon([(50, 120), (100, 90), (150, 120)], outline='black', fill='grey')
    elif home_type == 'Semi-detached':
        d.rectangle((50, 100, 100, 150), outline='black', width=3)
        d.rectangle((100, 100, 150, 150), outline='black', width=3)
        d.polygon([(50, 100), (75, 50), (100, 100)], outline='black', fill='grey')
        d.polygon([(100, 100), (125, 50), (150, 100)], outline='black', fill='grey')
    elif home_type == 'Flat':
        d.rectangle((50, 100, 150, 150), outline='black', width=3)
        d.line((50, 120, 150, 120), fill='black', width=3)
        d.line((50, 140, 150, 140), fill='black', width=3)
    return img
    
# Streamlit app
def main():
    st.title('Dynamic Calculator with Graphics')
    st.header('Stick Family')
    stick_family_img = create_stick_family()
    st.image(stick_family_img, caption='Stick Family')
    
    st.header('Home Types')
    home_types = ['Detached', 'Bungalow', 'Semi-detached', 'Flat']
    for home_type in home_types:
        st.subheader(home_type)
        home_img = create_home_type(home_type)
        st.image(home_img, caption=home_type)
                
        if __name__ == "__main__":
            main()
