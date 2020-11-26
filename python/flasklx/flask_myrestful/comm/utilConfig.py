import logging

applog = logging.getLogger('app')
applog.setLevel(logging.DEBUG)

appHandle = logging.StreamHandler()
appFormatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
appHandle.setLevel(logging.DEBUG)
appHandle.setFormatter(appFormatter)

applog.addHandler(appHandle)
