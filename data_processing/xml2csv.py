#Credit to https://alex-vaith.medium.com/save-precious-time-with-image-augmentation-in-object-detection-tasks-2f9111abb851

from curses.ascii import ETB
import os 
import pandas as pd
import xml.etree.ElementTree as ETB

class_of_interest = ['glass', 'melt', 'breccia'] # classes for the ALSCC dataset
#class_of_interest = ['glass'] # class for lunar regolith simulant dataset

label_path = "C://Users//hnadeem5//Documents//VSCode//auto-particle-classification//alscc_working//preprocess//annotations" # update


def xml_to_csv(files):
    xml_list = []
    for xml_file in files:
        tree = ETB.parse(xml_file)
        root = tree.getroot()

        bbox_available = False
        for member in root.findall('object'):
            if member[0].text in class_of_interest:
                bbox_available = True 
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                print('value', value) 
                xml_list.append(value)
        if not bbox_available:
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text))
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns = column_name)
    return xml_df

def get_xml_files(folder):
    xml_files = list()
    for file in os.listdir(folder):
        if file.endswith('.xml'):
            xml_files.append(os.path.join(folder, file))
    return xml_files

def main():
    folder_path = os.path.join(label_path)
    xml_files = get_xml_files(folder_path)
    xml_df = xml_to_csv(xml_files)
    xml_df.to_csv(os.path.join(label_path, 'labels.csv'), index=False)
    print('Successfully converted xml to csv.')

if __name__ == '__main__':
    main()
