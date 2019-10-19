import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_respStmt(text=""):
    respStmt = et.Element("respStmt");
    respStmt.text=text;
    return respStmt;


