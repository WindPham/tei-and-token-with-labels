import file_py_tei as tei



if __name__=="__main__":
    path_xml_in = "F:\\Khóa Luận\\XML\\code\\_01\\docs_xml";
    path_txt_in = "F:\Khóa Luận\XML\code\_01\docs_txt";
    path_xml_out = "F:\\Khóa Luận\\XML\code\\_01\\docs_demo";
    
    
    TEI = tei.tei(path_xml_in, path_txt_in, path_xml_out);
    
    TEI.create_tei();

