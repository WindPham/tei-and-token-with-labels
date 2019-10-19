import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_pubPlace(text=""):
    pubPlace=et.Element("pubPlace");
    pubPlace.text=text;
    return pubPlace;

def create_an_element_for_a_publicationStmt(list_of_elements = []):
    publicationStmt = et.Element("publicationStmt");
    for p in list_of_elements:
        publicationStmt.append(p);
    return publicationStmt;

