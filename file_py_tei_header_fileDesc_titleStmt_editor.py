import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_editor(text=""):
    editor = et.Element("editor");
    editor.text=text;
    return editor;
