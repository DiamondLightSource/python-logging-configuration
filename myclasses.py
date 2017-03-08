import logging
import logconfig

# Optional but useful in a library or non-main module:
logging.getLogger(__name__).addHandler(logging.NullHandler())

class MyClass(object):
    def __init__(self):
        log = logging.getLogger(".".join([__name__, self.__class__.__name__]))
        log.addFilter(logconfig.ThreadContextFilter())
        log.debug("This Class has been created")
        log.info("get on with work")
        log.error("we have a problem...")

