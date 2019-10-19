
import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_principal(text=""):
    principal = et.Element("principal");
    principal.text=text;
    return principal;

