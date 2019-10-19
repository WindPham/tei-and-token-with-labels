
import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_encodingDesc():
    encodingDesc = et.Element("encodingDesc");
    return encodingDesc;