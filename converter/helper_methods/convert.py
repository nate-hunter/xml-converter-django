import lxml.etree as etree
import csv
import os


def test_funk(directory, studio):

    return f"DIRECTORY: {directory} || STUDIO: {studio}" 


# def create_ae_data_dict(xml_to_parse):
#     # DATA PROVIDED BY A&E

#     with open(xml_to_parse, 'rb') as f:
#         open_xml = f.read()

#     root = etree.fromstring(open_xml)

#     data_dict = {
#         'Series': '',
#         'Season': '',
#         'Title': '',
#         'EpisodeNumber': '',
#         'Description': '',
#         'SeasonDescription': '',
#         'Actor1': '',
#         'Actor2': '',
#         'Rating': '',
#         'Genre': '',
#         'Duration': '',
#         'ReleaseYear': ''
#     }

#     for child in root.getchildren():
#         if not child.text == 'N/A':
#             if child.tag in data_dict:
#                 data_dict[child.tag] = child.text

#     return data_dict


# def create_disney_data_dict(xml_to_parse):
#     # DATA PROVIDED BY DISNEY

#     with open(xml_to_parse, 'rb') as f:
#         open_xml = f.read()

#     root = etree.fromstring(open_xml)

#     data_dict = {
#         'series': '',
#         'series_short_synopsis': '',
#         'series_start_year': '',
#         'season': '',
#         'season_short_synopsis': '',
#         'title': '',
#         'episode_number': '',
#         'runtime': '',
#         'short_synopsis': '',
#         'genre': '',
#         'rating': '',
#         'cast': '',
#         'physical_release_date': ''
#     }

#     for key in data_dict:
#         for element in root.iter(key):
#             if element.tag == 'cast':
#                 list_actor = []
#                 for actor in element.getchildren():
#                     actor_name = actor.get("name")
#                     list_actor.append(actor_name)

#                 data_dict[element.tag] = '; '.join(list_actor)
#             else:
#                 data_dict[element.tag] = element.text

#     return data_dict


# def create_discovery_data_dict(xml_to_parse):
#     # NEXT STUDIO TO SETUP
#     with open(xml_to_parse, 'rb') as f:
#         open_xml = f.read()

#     root = etree.fromstring(open_xml)

#     data_dict = {
#         'series_name': '',
#         'season_title': '',
#         'container_position': '',
#         'title': '',
#         'release_date': '',
#         'season_description': '',
#         'description': '',
#         'genre': '',
#         'rating': '',
#         'duration': ''
#     }

#     for key in data_dict:
#         for child in root.getchildren():
#             k = "{http://apple.com/itunes/importer}" + key
#             for ch in child.iter(k):
#                 tag = ch.tag.split("}")[1]
#                 data_dict[tag] = ch.text

#     return data_dict


# def process_directory(directory, studio):
#     """ TAKES A DIRECTORY OF XML METADATA AND OUTPUTS A LIST WHICH IS USED BY `write_to_csv()`."""
#     list_data = []
#     for filename in os.listdir(directory):
#         if filename.endswith(".xml"):
#             file = os.path.join(directory, filename)
#             if studio.lower() == "a&e":
#                 ae_dict = create_ae_data_dict(file)
#                 list_data.append(ae_dict)
#             elif studio.lower() == "disney":
#                 disney_dict = create_disney_data_dict(file)
#                 list_data.append(disney_dict)
#             elif studio.lower() == 'discovery':
#                 discovery_dict = create_discovery_data_dict(file)
#                 list_data.append(discovery_dict)
#             else:
#                 print("- '" + studio +
#                       "' is not set up to convert XMLs to CSV at this time.")
#                 break
#     return list_data


def extract_columns(data):
    """ EXTRACTS COLUMNS TO USE IN `write_to_csv()`'s `DictWriter()` """
    columns = []

    column_headers = data[0]

    for key in column_headers:
        columns.append(key)

    return columns


def write_to_csv(filename, data):
    columns = extract_columns(data)

    with open(filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


