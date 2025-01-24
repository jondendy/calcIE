import streamlit as st

# Define CSS for the thought bubble
thought_bubble_css = '''
<style>
.thought-bubble {
    position: relative;
    background: #f0f0f0;
    border-radius: .4em;
    padding: 10px;
    margin: 20px 0;
}
.thought-bubble:after {
    content: '';
    position: absolute;
    border-style: solid;
    border-width: 15px 15px 0;
    border-color: #f0f0f0 transparent;
    display: block;
    width: 0;
    z-index: 1;
    bottom: -15px;
    left: 20px;
}
</style>
'''

# Streamlit app
st.title('Dynamic Calculator')

# Add CSS to the app
st.markdown(thought_bubble_css, unsafe_allow_html=True)

# Example calculation result
result = 42  # This would be dynamically calculated in a real app

# Display the result in a thought bubble
st.markdown(f'<div class=thought-bubble>Result: {result}</div>', unsafe_allow_html=True)

