import logging
logger = logging.getLogger('poj')
logger.setLevel(logging.DEBUG)
pojHandler = logging.StreamHandler()
pojHandler.setLevel(logging.DEBUG)
pojHandler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S'))
logger.addHandler(pojHandler)