import xml.etree.ElementTree as ET
import os
import shutil


def parser_xml(path):
    # Change the Path of the xml folder and lines to make it run on your project
    # Creation of the Path that we are gonna use the .gt.txt files and the corrisponding image lines
    print("The current working directory is %s" % path)

    new_path = path + r"\GroundTruth"
    print(path)

    try:
        os.mkdir(new_path)  # create the directory used to store the xml files
    except OSError:
        print("Creation of the directory %s failed because already existed" % path)
    else:
        print("Successfully created the directory %s " % path)

    # Loop to open each files in the xml Directory to read each xml
    # To save the trascription inside each one into .txt file
    directory = path + r"\xml"
    for filename in os.listdir(directory):
        mytree = ET.parse(directory + '\\' + filename)
        myroot = mytree.getroot()
        i = 0  # counter of the trascription
        save_path = new_path  # path to save the new .gt.txt files
        for child in myroot[1]:
            sentence = child.attrib['text']
            # reformat the name of the file to be the same of the png
            name = filename.replace(".xml", "")
            name = name + "-" + str(i).zfill(2)
            # create the file .gt.txt requested by calamari_ocr to do the training phase
            xml_name = os.path.join(save_path, name + ".gt.txt")
            xml_tmp = open(xml_name, "w")
            xml_tmp.write(sentence)
            xml_tmp.close()
            i = i + 1

    # Copy all the png in the Directory of the Ground Truth to generate the files required by The Calamari_OCR
    source = r'C:\Users\Lorenzo Gianassi\PycharmProjects\DDMproject\lines'
    destination = path
    for root, subdirectories, files in os.walk(source):  # lists all the paths of each file
        for file in files:
            shutil.copy2(os.path.join(root, file), destination)