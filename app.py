import streamlit as st
import importlib
from PIL import Image
from streamlit_option_menu import option_menu

files = ['titanic','iris','cars']
pages=[]
modules=[]

for file in files:    
    modules.append(importlib.import_module(f'pag.{file}'))
    pages.append(file.capitalize())

    

st.set_page_config(
                    page_title="Template Project",
                    page_icon=Image.open("icon_site.png"),
                    layout="wide",
                    )

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
                        "title": title,
                        "function": function
                        })

    def main():
        with st.sidebar:
            app = option_menu(
                                menu_title="Menu",
                                options=pages,
                                icons=None,
                                menu_icon="bi-list",
                                default_index=0,
                                styles={
                                        "container": {"padding": "5!important", "background-color": "black"},
                                        "icon": {"color": "white", "font-size": "23px"},
                                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                                        "nav-link-selected": {"color": "black", "background-color": "#9ac280"}
                                        }
                                        )        
        selected_index = pages.index(app)
        modules[selected_index].main()

if __name__=='__main__':
    MultiApp.main()