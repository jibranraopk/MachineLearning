import streamlit as st

# Title and instructions
st.title("Multi-Screen Video Player by JRAO")
st.write("Enter the YouTube video URL below. The video will be displayed in a 5x5 grid and will autoplay and loop.")

# Get YouTube URL from user
video_url = st.text_input("Enter YouTube Video URL:")

# Extract video ID from the URL
video_id = video_url.split("v=")[-1] if "youtube.com" in video_url else video_url

# Create HTML table with placeholders for 100 screens (5 rows x 5 columns)
if video_id:
    embed_code = f'''
    <iframe width="300" height="150" src="https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}" frameborder="0" allow="autoplay; encrypted-media;" allowfullscreen></iframe>
    '''
    
    table_code = "<table>"
    for i in range(5):
        table_code += "<tr>"
        for j in range(5):
            table_code += f"<td>{embed_code}</td>"
        table_code += "</tr>"
    table_code += "</table>"
    
    st.write(table_code, unsafe_allow_html=True)
