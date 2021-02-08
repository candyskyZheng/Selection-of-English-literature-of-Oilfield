#### Selection-of-English-literature-of-Oilfield
#### 油田英文文献筛选， 返回一个txt文档  false_pdf_name_0. txt, 油田名称只出现在参考文献里的文件名称；
#### 1.  遍历文件夹下的子文件夹；
#### 2.  遍历子文件夹下的pdf文档(text_path), 获取油田名称（Field_name)；
#### 3.  读取pdf文档，将整片文章存成string；
#### 4.  检索 string 中 Field_name 和 “References" or "Reference" or "REFERENCE" or "REFERENCES"的位置；
#### 5.  比较二者的位置，如果 Field 只出现在reference 之后，而且文章中存在reference，则返回text_path，并将text_path写入false_field_name_0.txt；
#### 6.  读取false_field_name_0.txt 获得不符合的文件的路径，将不符合的文件移出原文件夹放到 “D:\文件更新\Refer_Update0203\1” 文件夹中。
