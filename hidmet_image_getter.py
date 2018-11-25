import logging
import argparse

DEFAULT_SAVE_DIRECTORY = '/composite'
DEFAULT_RADAR_TYPE = 'composite'
DEFAULT_LOG_LEVEL = 'verbose'

if __name__ == "__main__":

    # introducing arguments with description and default values
    parser = argparse.ArgumentParser()
    parser.add_argument('--radar-type', help='says which radar is used in program', default=DEFAULT_RADAR_TYPE)
    parser.add_argument('--save-folder', help='place where the images are stored', default=DEFAULT_SAVE_DIRECTORY)
    parser.add_argument('--log-level', help='increase output verbosity', default=DEFAULT_LOG_LEVEL)

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
