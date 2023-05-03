# materialsymbols-python
![GitHub repo size](https://img.shields.io/github/repo-size/T-Dynamos/materialsymbols-python)
![img](https://img.shields.io/static/v1?label=fonts&message=504&color=yellow)

Get all the possible combination of Material Symbols!

This repo provides fonts in `fonts/` path. You can also use `generator.py` to generate latest fonts yourself. These will be saved in `fonts/` dir.

Format of fonts: `Material_Symbols_<FONT_TYPE>-<OPTICAL_SIZE>-<WEIGHT>-<FILL>_<GRAD>.ttf`

> Example : https://github.com/T-Dynamos/materialsymbols-python/raw/main/fonts/Material_Symbols_Outlined-20-100-0_-25.ttf

Possible values:
```python
# Possible values
FONT_TYPE = ["Outlined", "Rounded", "Sharp"]
OPTICAL_SIZE = ["20", "24", "40", "48"]  # in px
GRAD = ["-25", "0", "200"]
WEIGHT = ['100', '200', '300', '400', '500', '600', '700']
FILL = [1,0]
```
What does this means:

![ii](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fl1dshu8o-adjustable_attributes_1.gif?alt=media&token=3e4384c6-b15a-4654-8250-ae61f38f8533)

See More : https://m3.material.io/styles/icons/overview

## Why this?
This project exists because not all libraries support [variable fonts](https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts), such as SDL. It aims to provide a solution for using variable fonts in libraries that do not support them. By converting the variable font to a set of static fonts, this project allows for the use of variable fonts in any library that supports static fonts.

## Usage
To use this repository, follow these steps:

1. Choose your favorite font file and download it. You can use it anywhere.
2. Type the Unicode character, for example: `\ue769`

You can find the Unicode character for each icon at https://fonts.google.com/icons.

Here's an example of how the icon would look like with its Unicode character:
> ![Screenshot_20230501_223656](https://user-images.githubusercontent.com/68729523/235493842-0de29262-b05d-4b8d-b2b4-e80b929d361d.png)

That's it! You can now use any Material Symbol for your projects.

[Kivy](https://github.com/kivy/kivy) Example:

```python
from kivy.app import App
from kivy.lang import Builder

UI = Builder.load_string(
"""
Label:
    text:"\ue769"
    font_name:"fonts/Material_Symbols_Rounded-20-100-0_-25.ttf"
    font_size:"300sp"
    halign:"center"
"""
)


class Testapp(App):

    def build(self):
        return UI

Testapp().run()
```
