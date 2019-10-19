
import numpy as np
import lxml
from lxml import etree as et
import os

import file_py_tei_header_fileDesc_titleStmt_title as title
import file_py_tei_header_fileDesc_titleStmt_author as author
import file_py_tei_header_fileDesc_titleStmt_editor as editor
import file_py_tei_header_fileDesc_titleStmt_funder as funder
import file_py_tei_header_fileDesc_titleStmt_principal as principal
import file_py_tei_header_fileDesc_titleStmt_respStmt as respStmt
import file_py_tei_header_fileDesc_titleStmt_sponsor as sponsor

def create_an_element_for_a_titleStmt(doc=None):

    titleStmt = et.Element("titleStmt");
    titleStmt.append(title.create_an_element_for_a_title(doc=doc));
    titleStmt.append(author.create_an_element_for_an_author(doc = doc));
    titleStmt.append(editor.create_an_element_for_a_editor());
    titleStmt.append(funder.create_an_element_for_a_funder());
    titleStmt.append(principal.create_an_element_for_a_principal());
    titleStmt.append(respStmt.create_an_element_for_a_respStmt());
    titleStmt.append(sponsor.create_an_element_for_a_sponsor());

    return titleStmt;