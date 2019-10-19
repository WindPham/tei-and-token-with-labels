import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_creation(doc = None):
    creation = et.Element("creation");
    creation.append(doc.find("time"));
    return creation;


def create_an_element_for_a_profileDesc(doc = None):
    profileDesc=et.Element("profileDesc");
    profileDesc.append(create_an_element_for_a_creation(doc));
    return profileDesc;


