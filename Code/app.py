import streamlit as st
from functions import homePage, displayWriting, sidebar, getQuote, message

st.set_page_config(page_title="Tat Tvam Asi", page_icon="🕉")
choose = sidebar()

##########################################################################################################################################################

if choose == "Why This?":
    #Arguments: title, messsage
    title, message = message()
    homePage(title, message)

##########################################################################################################################################################

elif choose == "Few Learnings":
    #Arguments: uniqueKey, coverImageUrl, heading, metaDescription, contentPath
    #writing 1: 
    displayWriting("FL1", 'https://raw.githubusercontent.com/imsanketsingh/Tat-Tvam-Asi/main/Images/krishna.jpg?token=GHSAT0AAAAAACTI3SZHDKV3JNJ2KMKALBD4ZTIMR4A', 'Rashmirathi : Part 1', 'The first article of the series that explores the great epic **Rashmirathi** by Ramdhari Singh Dinkar, delving into its Philiterary themes, offering insights into duty, morality, and the complexities of the Mahabharata character, Karna.', '../Writings/Few Learnings/krishna.html')
    
##########################################################################################################################################################

elif choose == "Great Learners": 
        pass

##########################################################################################################################################################

elif choose == "Miscellaneous": 
        pass

##########################################################################################################################################################

st.sidebar.markdown("<p style='font-style: italic;'>{}</p>".format(getQuote()[0]), unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-style: italic; text-align: right; margin-right: 2rem;'>{}</p>".format("- "+ getQuote()[1]), unsafe_allow_html=True)

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

##########################################################################################################################################################