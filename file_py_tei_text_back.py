import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_note(text, id=""):
    note = et.Element("p");
    note.attrib["id"]=id;
    note.text=text;
    return note;


def demo_back(list_of_notes):
    back = et.Element("back");
    for n in list_of_notes:
        back.append(n);
    return back;

