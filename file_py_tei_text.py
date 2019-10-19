import numpy as np
import lxml
from lxml import etree as et
import os

import file_py_tei_text_front as front

import file_py_tei_text_body as body

import file_py_tei_text_group as group

import file_py_tei_text_back as back

def read_files(path):
    list_of_filenames = os.listdir(os.path.expanduser(path));
    list_of_docs=[];
    for name in list_of_filenames:
        f = open(path+"\\"+ name, "r", encoding="utf-8");
        list_of_docs.append(f);
    return list_of_docs;

def create_a_text(doc, id ="", order=""):
    Front = front.demo_front();
    Body = body.create_an_element_for_a_body(doc, id=id, order=order);
    Group = group.demo_group();
    Back = back.demo_back([]);
    text = et.Element("text");
    text.append(Front);
    text.append(Body);
    text.append(Group);
    text.append(Back);
    return text;


def write_text(list_of_docs, path, init_number):
    count = 0;
    for doc in list_of_docs:
        count+=1;
        text = create_a_text(doc, id=str(count), order=str(count));
        name = str(init_number + count)+".xml";
        f=open(path + "\\" + name, 'w', encoding="utf-8");
        f.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n');
        f.write(et.tostring(text, encoding="unicode"));
    return 0;
#path_in="F:\Khóa Luận\XML\code\_01\docs_txt";
#path_out="F:\\Khóa Luận\\XML\code\\_01\\docs_demo";

#write_text(read_files(path_in), path_out, 1);
