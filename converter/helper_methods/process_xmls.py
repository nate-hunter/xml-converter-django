from converter.helper_methods import create_dictionarys
import lxml.etree as etree
import csv
import os

def process_directory(directory, studio):
    """ TAKES A DIRECTORY OF XML METADATA AND OUTPUTS A LIST WHICH IS USED BY `write_to_csv()`."""
    
    # file_list = []
    list_data = []
    studio_error = ''

    for filename in os.scandir(directory):
        if filename.is_file() and filename.name.endswith('.xml'):
            file = os.path.join(directory, filename)
            # print('++++FILE:', file)
            # file_list.append(file)
            if studio.lower() == "a&e":
                ae_dict = create_dictionarys.create_ae_data_dict(file)
                list_data.append(ae_dict)
                studio_name = studio.upper()
            elif studio.lower() == "disney":
                disney_dict = create_dictionarys.create_disney_data_dict(file)
                list_data.append(disney_dict)
                studio_name = studio.upper()
            elif studio.lower() == 'discovery':
                discovery_dict = create_dictionarys.create_discovery_data_dict(file)
                list_data.append(discovery_dict)
                studio_name = studio.upper()
            else:
                studio_error = "'" + studio + "' is not set up to convert XMLs to CSV at this time."
                break    

    # for filename in os.scandir(directory):
    #     if filename.is_file() and filename.name.endswith('.xml'):
    #         file = os.path.join(directory, filename)
    #         file_list.append(file)
    #         if studio.lower() == "a&e":
    #             ae_dict = create_ae_data_dict(file)
    #             list_data.append(ae_dict)
    #         elif studio.lower() == "disney":
    #             disney_dict = create_disney_data_dict(file)
    #             list_data.append(disney_dict)
    #         elif studio.lower() == 'discovery':
    #             discovery_dict = create_discovery_data_dict(file)
    #             list_data.append(discovery_dict)
    #         else:
    #             studio_error = "'" + studio + "' is not set up to convert XMLs to CSV at this time."
    #             break


    return list_data