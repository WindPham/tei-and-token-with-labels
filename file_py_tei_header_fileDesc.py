

import numpy as np
import lxml
from lxml import etree as et
import os
import file_py_tei_header_fileDesc_editionStmt as editionStmt
import file_py_tei_header_fileDesc_publicationStmt as publicationStmt
import file_py_tei_header_fileDesc_titleStmt as titleStmt
import file_py_tei_header_fileDesc_sourceDesc as sourceDesc
import file_py_tei_header_fileDesc_category as category

def create_an_element_for_a_fileDesc(doc=None):
    fileDesc = et.Element("fileDesc");
    fileDesc.append(titleStmt.create_an_element_for_a_titleStmt(doc = doc));
    fileDesc.append(publicationStmt.create_an_element_for_a_publicationStmt());
    fileDesc.append(editionStmt.create_an_element_for_editionStmt());
    fileDesc.append(sourceDesc.create_an_element_for_a_sourceDesc(doc = doc));
    fileDesc.append(category.create_an_element_for_a_category(doc = doc));
    return fileDesc;



