

import numpy as np
import lxml
from lxml import etree as et
import os

#-----------------------------------------------------------------------
def raw_name(text=""):
    persnameText=et.Element("rawName");
    persnameText.text=text;
    return persnameText;

def create_an_element_for_a_persname(doc = None, id=""):
    persname=et.Element("persName");
    persname.attrib["id"]=id;
    persname.append(raw_name(doc.find("author").text));
    return persname;
#------------faith-------------------------------------
def create_an_element_for_a_faith(text="", id=""):
    faith=et.Element("faith");
    faith.attrib["id"]=id;
    faith.text=text;
    return faith;
#------------language knowledge------------------------
def create_an_element_for_a_language(text="", id=""):
    lang = et.Element("language");
    lang.attrib["id"]=id;
    lang.text=text;
    return text;

def create_an_element_for_a_langKnowledge(list_of_languages=[], id=""):
    langKnowledge=et.Element("langKnowledge");
    langKnowledge.attrib["id"]=id;
    for l in list_of_languages:
        langKnowledge.append(l);
    return langKnowledge;

#------------------------------------------------------------------------
def create_an_element_for_a_nationality(text="", id=""):
    nationality = et.Element("nationality");
    nationality.attrib["id"]=id;
    nationality.text=text;
    return nationality;

def create_an_element_for_a_gender(value=""):
    sex = et.Element("sex");
    sex.attrib["value"]=value;
    if(value=="F"):
        sex.text="female";
    else:
        sex.text="male";
    return sex;
    
def create_an_element_for_age(Age="0"):
    age = et.Element("age");
    age.text=Age;
    return age;

def create_an_element_for_a_region(value="", text=""):
    region = et.Element("region");
    region.attrib["value"]=value;
    region.text=text;
    return region;

def create_an_element_for_an_event(list_of_events=[]):
    event=et.Element("event");
    for e in list_of_events:
        event.append(e);
    return event;

def create_an_element_for_address(text=""):
    address=et.Element("address");
    address.text=text;
    return address;

def create_an_element_for_a_socecStatus(doc = None):
    return et.Element("socecStatus");

def create_an_element_for_occupation(doc = None):
    return et.Element("occupation");

def create_an_element_residence(doc = None):
    return et.Element("residence");

def create_an_element_affiliation(doc = None):
    return et.Element("affiliation");

def create_an_element_education(doc = None):
    return et.Element("education");

def create_an_element_floruit(doc = None):
    return et.Element("floruit");

def create_an_element_persona(doc = None):
    return et.Element("persona");

def create_an_element_state(doc = None):
    return et.Element("state");

def create_an_element_trait(doc = None):
    return et.Element("trait");

#=====================================================================

def create_an_element_for_an_author(doc = None):
    author = et.Element("author");
    author.append(create_an_element_for_a_faith());
    author.append(create_an_element_for_a_langKnowledge());
    author.append(create_an_element_for_a_nationality(u"Việt Nam", id = "nationality-VN"));
    author.append(create_an_element_for_a_gender("M"));
    author.append(create_an_element_for_age());
    author.append(create_an_element_for_a_region());
    author.append(create_an_element_for_an_event());
    author.append(create_an_element_for_address());
    author.append(create_an_element_for_a_persname(doc = doc));
    author.append(create_an_element_for_a_socecStatus());
    author.append(create_an_element_for_occupation());
    author.append(create_an_element_residence());
    author.append(create_an_element_affiliation());
    author.append(create_an_element_education());
    author.append(create_an_element_floruit());
    author.append(create_an_element_persona());
    author.append(create_an_element_state());
    author.append(create_an_element_trait());
    return author;

