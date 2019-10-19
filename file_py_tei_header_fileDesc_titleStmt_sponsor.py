import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_sponsor(text=""):
    sponsor = et.Element("sponsor");
    sponsor.text=text;
    return sponsor;

