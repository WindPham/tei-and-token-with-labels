
import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_cateDesc(cate):
    cateDesc = et.Element("cateDesc");
    cateDesc.text = cate.text;
    return cateDesc;

def create_an_element_for_a_category(doc =  None):
    category = et.Element("category");
    category_list = doc.find("category_name_list");
    for cate in category_list:
        category.append(create_an_element_for_a_cateDesc(cate));
    return category;

