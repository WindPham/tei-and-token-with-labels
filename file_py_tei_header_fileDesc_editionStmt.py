
import numpy as np
import lxml
from lxml import etree as et
import os



def create_an_element_for_editionStmt(doc=None):
    editionStmt = et.Element("editionStmt");
    return editionStmt;

