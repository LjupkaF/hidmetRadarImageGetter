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

def downloading (url):
    """
    Downloading images from URL and collect their path in a list
    """
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, features='lxml')
    if url == URL_FOR_KOSUTNJAK or url == URL_FOR_COMPOSITE:
        links = soup.findAll('div', id = 'slider1', src = False)
        images = [i for i in links]
    else:
        links = soup.findAll('div', style='padding: 0 20px 0 20px;')
        images = [i for i in links]
    return print(images)

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
    downloading(radar_type['kosutnjak'])
