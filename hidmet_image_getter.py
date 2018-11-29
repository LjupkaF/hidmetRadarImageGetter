import logging
import argparse
import urllib.request
from bs4 import BeautifulSoup
import re

DEFAULT_SAVE_DIRECTORY = '/composite'
DEFAULT_RADAR_TYPE = 'composite'
DEFAULT_LOG_LEVEL = 'verbose'

URL_FOR_KOSUTNJAK = "http://www.hidmet.gov.rs/ciril/osmotreni/radarska3bg.php"
URL_FOR_LAWR = "http://www.hidmet.gov.rs/ciril/osmotreni/lawr2.php"
URL_FOR_COMPOSITE = "http://www.hidmet.gov.rs/ciril/osmotreni/radarska3.php"

# Setting radar types and their url
radar_type = {'kosutnjak': URL_FOR_KOSUTNJAK, 'lawr': URL_FOR_LAWR, 'composite': URL_FOR_COMPOSITE}

def downloading_image_path (url):
    """
    Downloading images from URL and collect their path in a list named images_name
    """
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, features='lxml')
    if url == URL_FOR_KOSUTNJAK or url == URL_FOR_COMPOSITE:
        links = soup.findAll('div', id = 'slider1', src = False)
        images = str([i for i in links])
    else:
        links = soup.findAll('div', style='padding: 0 20px 0 20px;')
        images = str([i for i in links])

    # parsing the string of HTML name of images to their clear name
    images_without_prefix = re.sub(r'<img src="', '', images)
    images_without_sufix = re.sub(r'"/>', '', images_without_prefix)
    i = re.sub(r'(\[)?<(/)?(.)*>(\])?', '', images_without_sufix)
    images_name = [p for p in i.split('\n') if p != '']
    return print(images_name)

def folder_collection(url):
    pass

if __name__ == "__main__":

    # introducing arguments with description and default values
    parser = argparse.ArgumentParser()
    parser.add_argument('--radar-type', help='says which radar is used in program', default=DEFAULT_RADAR_TYPE)
    parser.add_argument('--save-folder', help='place where the images are stored', default=DEFAULT_SAVE_DIRECTORY)
    parser.add_argument('--log-level', help='define log level', default=DEFAULT_LOG_LEVEL)

    args = parser.parse_args()

    # Setting logging level
    logger = logging.getLogger()
    if args.log_level == 'off':
        logger.setLevel(logging.ERROR)
    elif args.log_level == 'low':
        logger.setLevel(logging.WARNING)
    else:
        logger.setLevel(logging.NOTSET)

    # logging.debug("debug:")
    # logging.info("info")
    # logging.warning("warning")
    # logging.error("error")
    # logging.critical("critical")

    print("Log level: " + args.log_level)
    print("Radar type:" + args.radar_type)
    print("Save folder:" + args.save_folder)

    logging.info('Starting downloading images path from URL')
    downloading_image_path(radar_type['kosutnjak'])
