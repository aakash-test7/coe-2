import streamlit as st
from pages.footer_all import base_footer 
from backend import generate_signed_url
from pages.Meta_Data import meta_data_page
from pages.Citations import citations_page
from pages.Glossary import glossary_page
from pages.Tutorials import tutorials_page

@st.cache_data(show_spinner=False)
def get_image_url(image_path):
    return generate_signed_url(image_path)

def display_about_content():
    st.title("About Us")
    col1, col2 = st.columns(2)
    
    # Container 1
    st.markdown("""<style>.stVerticalBlock.st-key-au2, .stVerticalBlock.st-key-au1, .stVerticalBlock.st-key-au3, .stVerticalBlock.st-key-au4, .stVerticalBlock.st-key-au5, .stVerticalBlock.st-key-au6 {background-color: rgb(185, 214, 148); color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-au2:hover, .stVerticalBlock.st-key-au1:hover, .stVerticalBlock.st-key-au3:hover, .stVerticalBlock.st-key-au4:hover, .stVerticalBlock.st-key-au5:hover, .stVerticalBlock.st-key-au6:hover {background-color: rgba(242,240,239,0.5); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);}</style>""", unsafe_allow_html=True)
    con = col1.container(border=False, key="au1")
    with con:
        c1, c2 = st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"), use_container_width=True)
        c2.subheader("Person1")
        c2.write("Hello")
    
    # Container 2
    con = col2.container(border=False, key="au2")
    with con:
        c1, c2 = st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"), use_container_width=True)
        c2.subheader("Person2")
        c2.write("Hello")

    # Container 3
    con = col1.container(border=False, key="au3")
    with con:
        c1, c2 = st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"), use_container_width=True)
        c2.subheader("Person3")
        c2.write("Hello")
    
    # Container 4
    con = col2.container(border=False, key="au4")
    with con:
        c1, c2 = st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"), use_container_width=True)
        c2.subheader("Person4")
        c2.write("Hello")

    # Container 5
    con = col1.container(border=False, key="au5")
    with con:
        c1, c2 = st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"), use_container_width=True)
        c2.subheader("Person5")
        c2.write("Hello")
    
    # Container 6
    con = col2.container(border=False, key="au6")
    with con:
        c1, c2 = st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"), use_container_width=True)
        c2.subheader("Person6")
        c2.write("Hello")

def about_page():
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = 'ABOUT-US'
    
    def set_active_tab(tab_name):
        st.session_state.active_tab = tab_name
    
    # Create columns for buttons
    st.write(" ")
    col1, col2, col3, col4, col5 = st.columns(5)
    if col1.button("ABOUT-US", key="btn_about",use_container_width=True):
        set_active_tab('ABOUT-US')
        st.rerun()
    if col2.button("META-DATA", key="btn_meta",use_container_width=True):
        set_active_tab('META-DATA')
        st.rerun()
    if col3.button("CITATIONS", key="btn_citations",use_container_width=True):
        set_active_tab('CITATIONS')
        st.rerun()
    if col4.button("GLOSSARY", key="btn_glossary",use_container_width=True):
        set_active_tab('GLOSSARY')
        st.rerun()
    if col5.button("TUTORIALS", key="btn_tutorials",use_container_width=True):
        set_active_tab('TUTORIALS')
        st.rerun()
        
    # Display content based on active tab
    if st.session_state.active_tab == 'ABOUT-US':
        display_about_content()
    elif st.session_state.active_tab == 'META-DATA':
        meta_data_page()
    elif st.session_state.active_tab == 'CITATIONS':
        citations_page()
    elif st.session_state.active_tab == 'GLOSSARY':
        glossary_page()
    elif st.session_state.active_tab == 'TUTORIALS':
        tutorials_page()
    
    base_footer()

if __name__ == "__main__":
    about_page()
