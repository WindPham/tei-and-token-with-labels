import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_funder(text=""):
    funder = et.Element("funder");
    funder.text=text;
    return funder;


