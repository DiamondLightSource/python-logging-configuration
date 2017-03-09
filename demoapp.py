import logging
import logconfig
import myclasses

# DLS specific configuration: the pygelf module is required in the environment
# although our code does not directly import it!
# For a full-size project you should specify this dependency in setup.py
from pkg_resources import require
require('pygelf==0.2.11')

log = logging.getLogger(name="demoapp")
logconfig.setup_logging()

def main():
    c = myclasses.MyClass()
    log.info(c)

    try:
        1/0
    except ZeroDivisionError as e:
        log.exception(e)
        
    raise RuntimeError("Horrible things have happened!!")


if __name__ == "__main__":
    import os.path
    import sys
    try:
        log.info("application: demoapp.py, arguments: %s", sys.argv)
        main()
    except Exception as e:
        log.exception(e)
        raise

