from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string(""" 
BoxLayout:
    Label:
        font_name:"./Material_Symbols_Sharp-20-100-0_0.ttf"
        icon:"home"
"""))
