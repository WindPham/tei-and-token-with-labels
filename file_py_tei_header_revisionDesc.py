
import numpy as np
import lxml
from lxml import etree as et
import os


def create_an_element_for_a_revisionDesc(list_of_elements=[]):
    revisionDesc = et.Element("revisionDesc");
    for e in list_of_elements:
        revisionDesc.append(e);
    return revisionDesc;