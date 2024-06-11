import streamlit as st
from  PIL import Image
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import random
import requests
from io import BytesIO


def homePage(title, message):
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown(f'<p style="color: #767196; font-size: 27px; font-style:helvetica;">{title}</p>', unsafe_allow_html=True)    
    st.markdown(f"""{message}""", unsafe_allow_html=True)


def showthecontent(filepath):
    with open(filepath, "r") as f:
        html_string = f.read()
    components.html(html_string, scrolling = True, height = 700)


def displayWriting(uniqueKey, coverImageUrl, heading, metaDescription, contentPath):
    response = requests.get(coverImageUrl)
    image_data = BytesIO(response.content)
    learningCoverImage1 = Image.open(image_data)
    learningCoverImage1 = learningCoverImage1.resize((320, 240))
    with st.container():
        image_col, text_col = st.columns((2, 3))
        with image_col:
            st.image(learningCoverImage1)
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;}
            </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">{heading}</p>', unsafe_allow_html=True)
            st.markdown(metaDescription, unsafe_allow_html=True)
        if st.button("Get into it", key=uniqueKey):
            showthecontent(contentPath)
            st.button("Wrap it up!", help="Close it")
    st.write('---')

def sidebar():
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .sidebar .sidebar-content:hover {
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    .option-menu li {
        border-radius: 8px;
        margin: 5px 0;
        transition: background-color 0.3s ease;
    }
    .option-menu li:hover {
        background-color: #e0e0e0;
    }
    .icon {
        color: #ff7f50 !important;
        font-size: 28px !important;
    }
    .nav-link {
        font-size: 16px !important;
        color: #333 !important;
        font-weight: bold !important;
    }
    .nav-link-selected {
        background-color: #28a745 !important;
        color: #fff !important;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)
    
    with st.sidebar:
        choose = option_menu("🕉 Hare Krishna 🕉", ["Why This?", "Few Learnings", "Great Learners", "Miscellaneous"],
                         icons=['sunrise', '1-square-fill', '2-square-fill', '3-square-fill'],
                         menu_icon="🕉", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#fafafa"},
                             "icon": {"color": "#0err50", "font-size": "28px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#df5f00", "color": "#fff", "border-radius": "8px"},
                         }
    )
    return choose


def readSpecificLine(filePath, lineNumber):
    try:
        with open(filePath, 'r') as file:
            lines = file.readlines()
            if lineNumber <= 0 or lineNumber > len(lines):
                return f"Error: Line number {lineNumber} is out of range. The file has {len(lines)} lines."
            line = lines[lineNumber - 1].strip()
            if " - " not in line:
                return f"Error: Line does not contain the expected format 'quote - book name'."
            quote, bookName = map(str.strip, line.rsplit(" - ", 1))
            return quote, bookName
    except FileNotFoundError:
        return f"Error: The file {filePath} does not exist."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

def getQuote():
    filePath = './Writings/Quotes/quotes.txt'
    lineNumber = random.randint(1, 95) 
    result = readSpecificLine(filePath, lineNumber)
    return result

def message():
    return 'From ignorance towards light: A meaningful start', """<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In a metus dictum, fringilla nibh quis, maximus sapien. Suspendisse sit amet metus ornare, commodo erat sit amet, elementum est. Pellentesque sit amet odio accumsan, viverra urna eu, euismod ex. In a lacus sed nisi ullamcorper convallis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce facilisis metus nibh, vel facilisis justo sagittis vitae. Nulla sed ornare tortor. Sed ut molestie ipsum, eu consectetur ante. Fusce semper sit amet libero sed pellentesque.

Sed nec risus sem. Ut ac eros non lectus vulputate mollis ut sit amet orci. Curabitur ornare tellus ultrices ultricies finibus. Sed quis elementum orci. Etiam tempor a mauris a venenatis. Etiam volutpat nibh dictum facilisis porttitor. Quisque tristique purus pretium lacus gravida, id rutrum felis tincidunt. Mauris vitae leo arcu. Nunc consequat tempor vestibulum. Vivamus cursus lorem odio, sit amet mollis turpis sagittis sit amet. Nam vel turpis dolor. Nam ultrices, augue eu pulvinar feugiat, ante dolor ultrices erat, vitae accumsan ante ligula sit amet sapien. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum bibendum justo id posuere fringilla.

Quisque imperdiet at mauris pellentesque posuere. Aenean aliquet faucibus laoreet. Cras consectetur odio sit amet mauris commodo, non ullamcorper mauris rhoncus. Donec leo massa, dapibus ac turpis sed, convallis pellentesque magna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In hac habitasse platea dictumst.</p>"""