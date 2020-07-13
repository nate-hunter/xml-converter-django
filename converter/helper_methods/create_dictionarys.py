import lxml.etree as etree
import csv 
import os


def create_ae_data_dict(xml_to_parse):
    # METADATA PROVIDED BY A&E

    with open(xml_to_parse, 'rb') as f:
        open_xml = f.read()

    root = etree.fromstring(open_xml)

    data_dict = {
        'Series': '',
        'Season': '',
        'Title': '',
        'EpisodeNumber': '',
        'Description': '',
        'SeasonDescription': '',
        'Actor1': '',
        'Actor2': '',
        'Rating': '',
        'Genre': '',
        'Duration': '',
        'ReleaseYear': ''
    }

    for child in root.getchildren():
        if not child.text == 'N/A':
            if child.tag in data_dict:
                data_dict[child.tag] = child.text

    return data_dict


def create_disney_data_dict(xml_to_parse):
    # METADATA PROVIDED BY DISNEY

    with open(xml_to_parse, 'rb') as f:
        open_xml = f.read()

    root = etree.fromstring(open_xml)

    # print('----ROOT:', root)

    data_dict = {
        'series': '',
        'series_short_synopsis': '',
        'series_start_year': '',
        'season': '',
        'season_short_synopsis': '',
        'title': '',
        'episode_number': '',
        'runtime': '',
        'short_synopsis': '',
        'genre': '',
        'rating': '',
        'cast': '',
        'physical_release_date': ''
    }

    for key in data_dict:
        for element in root.iter(key):
            if element.tag == 'cast':
                list_actor = []
                for actor in element.getchildren():
                    actor_name = actor.get("name")
                    list_actor.append(actor_name)

                data_dict[element.tag] = '; '.join(list_actor)
            else:
                data_dict[element.tag] = element.text

    

    return data_dict


def create_discovery_data_dict(xml_to_parse):
    # METADATA PROVIDED BY DISCOVERY
    with open(xml_to_parse, 'rb') as f:
        open_xml = f.read()

    root = etree.fromstring(open_xml)

    data_dict = {
        'series_name': '',
        'season_title': '',
        'container_position': '',
        'title': '',
        'release_date': '',
        'season_description': '',
        'description': '',
        'genre': '',
        'rating': '',
        'duration': ''
    }

    for key in data_dict:
        for child in root.getchildren():
            k = "{http://apple.com/itunes/importer}" + key
            for ch in child.iter(k):
                tag = ch.tag.split("}")[1]
                if data_dict[tag] == 'container_position':
                    data_dict[tag] = int(ch.text)
                else:
                    data_dict[tag] = ch.text

    # print (data_dict)
    # newlist = sorted(data_dict, key=lambda i: i['container_position']) 
    # print (sorted(data_dict, key = lambda i: i['container_position'])) 
    # print sorted(data_dict, key = lambda i: (i['container_position'], i['name'])) 

    # return newlist
    return data_dict