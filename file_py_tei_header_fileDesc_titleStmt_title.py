import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_title(doc=None):
    title = et.Element("title");
    title.text=doc.find("title").text;
    return title;


