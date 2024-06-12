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
    return 'From ignorance towards light: A meaningful start', """<p style="text-align: justify;"><span style="text-shadow: rgba(136, 136, 136, 0) 0px 0px 0px; color: rgb(40, 50, 78);">It all starts with the realization that something needs to be corrected in my life. Anyone would need this realization to explore this path of knowledge. It could be anything from anxiety to adventure, and from fear to regret that pushes us to know the reality of self. This simple realization is the first breakthrough in the broader and most important of all knowledge, self-realization.</span></p>
<p style="text-align: justify;"><span style="text-shadow: rgba(136, 136, 136, 0) 0px 0px 0px; color: rgb(40, 50, 78);">Overcoming the burdens of the mind is very tough. You seek help from the ultimate, you pray, you explore possibilities of knowing. Amid all this, you constantly fight with yourself, your fears, your insecurities, and you are so confused with your life and what&apos;s happening to it. You sometimes get the feeling that you should renounce everything, but you stay there, believing in.</span></p>
<p style="text-align: justify;"><span style="text-shadow: rgba(136, 136, 136, 0) 0px 0px 0px; color: rgb(40, 50, 78);">You hope that one day you will get connected with that one unifying consciousness that is the ultimate, and that will be the liberation. Liberation from the difficulties of the mind. </span><span style="text-shadow: rgba(136, 136, 136, 0) 0px 0px 0px; color: rgb(40, 50, 78);">You try to follow the words of sages and you find that you are already connected and you just don&apos;t have the realization, and hence all this pain and suffering. From that day, you begin something.</span></p>"""