
import numpy as np
import lxml
from lxml import etree as et
import os

# Each .py file will be created higher or equal to the 4th level in the tree.
def check_empty(s):
    if s=="":
        return "0";
    return "1";

def solve_a_token(token):
    res = {"text":"", "SV":"", "RD":"", "LF":"","OW":"","BW":"","POS":""};
    list_of_tokens=token.strip(u"\n").split(u"/");
    #print(list_of_tokens);
    res["POS"] = list_of_tokens[-1];
    res["BW"] = check_empty(list_of_tokens[-2]);
    res["OW"] = check_empty(list_of_tokens[-3]);
    res["LF"] = check_empty(list_of_tokens[-4]);
    res["RD"] = check_empty(list_of_tokens[-5]);
    res["SV"] = check_empty(list_of_tokens[-6]);
    if (list_of_tokens[0] == '\ufeff'):
        list_of_tokens[0]=list_of_tokens[0][1:];
    s=0;
    res["text"] += list_of_tokens[s];
    if(len(list_of_tokens)-6>=2):
        for s in range(1, len(list_of_tokens)-6):
            res["text"] += ('/'+list_of_tokens[s]);
    return res;

def create_an_element_for_a_token(token, type="token", id="", order=""):
    dict = solve_a_token(token);
    element_token = et.Element("token");
    element_token.text = dict["text"];
    element_token.attrib["type"]=type;
    element_token.attrib["id"]=id;
    element_token.attrib["order"]=order;
    for k,v in dict.items():
        if (k=="text"):
            continue;
        else:
            element_token.attrib[k]=v;
    return element_token;

def solve_a_sentence(sentence):
    list_of_tokens = sentence.strip("\n").split(" ");
    return list_of_tokens;

def create_an_element_for_a_sentence(sentence, type="sentence", id="id", order="order"):
    list_of_tokens=solve_a_sentence(sentence);
    element_sentence = et.Element("sentence");
    element_sentence.text="";
    element_sentence.attrib["type"]=type;
    element_sentence.attrib["id"]=id;
    element_sentence.attrib["order"]=order;
    element_sentence.attrib["number_of_tokens"]=str(len(list_of_tokens));
    for i in range(0, len(list_of_tokens)):
        t = create_an_element_for_a_token(list_of_tokens[i], order=str(i+1), id=str(i+1));
        element_sentence.append(t);
    return element_sentence;

def create_an_element_for_a_div1(doc, type="doc", id="", order=""):
    element_div1=et.Element("div1");
    element_div1.attrib["type"]=type;
    element_div1.attrib["id"]=id;
    element_div1.attrib["order"]=order;
    count = 0;
    for i in doc:
        count+=1;
        sentence = create_an_element_for_a_sentence(i, order=str(count), id=str(count));
        element_div1.append(sentence);
    element_div1.attrib["number_of_sentences"]=str(count);
    return element_div1;

def create_an_element_for_a_body(list_of_docs, type="essay", id="", order=""):
    #list_of_docs: nhieu file duoc truyen vao dang con tro file da doc roi
    #note: trong corpus nay thi ta se moi mot file chi co 1 doc thoi. nen len(list_of_docs)==1
    element_body=et.Element("body");
    element_body.attrib["type"]=type;
    element_body.attrib["id"]=id;
    element_body.attrib['order']=order;
    count = 0;
    for doc in list_of_docs:
        count+=1;
        div1=create_an_element_for_a_div1([doc], id=str(count), order=str(count));
        element_body.append(div1);
    element_body.attrib["numbers_of_div1s"]=str(count);
    return element_body;
