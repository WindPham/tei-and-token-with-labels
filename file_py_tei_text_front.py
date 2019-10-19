
import numpy as np
import lxml
from lxml import etree as et
import os


def create_an_element_for_a_p(name, text):
    p = et.Element(name);
    p.text=text;
    return p;

def create_an_element_for_a_list(name, list_of_ps):
    ele_list=et.Element(name);
    for p in list_of_ps:
        ele_list.append(p);
    return ele_list;

def create_an_element_for_a_div1(list_of_LIST, type=""):
    div1=et.Element("div1");
    div1.attrib["type"]=type;
    for l in list_of_LIST:
        div1.append(l);
    return div1;

def create_an_element_for_a_front(list_of_div1s):
    front = et.Element("front");
    for d in list_of_div1s:
        front.append(d);
    return front;

def demo_front():
    label=create_an_element_for_a_p("label","");
    item =create_an_element_for_a_p("item", "");
    head =create_an_element_for_a_p("head", "");
    trailer=create_an_element_for_a_p("trailer", "");
    List=create_an_element_for_a_list("list",[label, item]);
    div1=create_an_element_for_a_div1([head, List, trailer]);
    return create_an_element_for_a_front([div1]);




