
import numpy as np
import lxml
from lxml import etree as et
import os

def create_an_element_for_a_name_of_source(doc = None):
    sourceName=et.Element("sourceName");
    sourceName.text=doc.find("source").text;
    return sourceName;

def create_an_element_for_a_url(doc = None):
    url = et.Element("url");
    url.text = doc.find("url").text;
    return url;

def create_an_element_for_a_description(doc = None):
    descOfText = et.Element("descOfText");
    descOfText.text = doc.find("description").text;
    return descOfText;

def create_an_element_for_a_sourceDesc(doc = None):
    sourceDesc = et.Element("sourceDesc");
    sourceDesc.append(create_an_element_for_a_name_of_source(doc=doc));
    sourceDesc.append(create_an_element_for_a_url(doc = doc));
    sourceDesc.append(create_an_element_for_a_description(doc = doc));
    return sourceDesc;