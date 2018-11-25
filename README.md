repositorium name: hidmetRadarImageGetter

For Python versions 3.6 and above.
Service handles requests and return radar images from hidmet.gov.rs

Two part service:

1. Handler
    Waits for requests on specific port for radar images and responses with set of images;
    <TO-DO>

2. Image getter name: hidmet_image_getter.py
    Image getter has parameters:
        --radar-type (kosutnjak, lawr, DEFAULT: composite)
        --save-folder (DEFAULT: /composite)
        --log-level (off, low, DEFAULT: verbose)
    
    It scans http://hidmet.gov.rs/ciril/osmotreni/radarska.php for specific pictures of radar-type and saves them in save-folder;



DEFAULT_SAVE_FOLDER = "/composite"
DEFAULT_RADAR_TYPE = "composite"
DEFAULT_LOG_LEVEL = "verbose"
