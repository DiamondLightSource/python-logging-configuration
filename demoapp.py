import logging
import logconfig
import myclasses

log = logging.getLogger(name="demoapp")

def main():
    logconfig.setup_logging()

    c = myclasses.MyClass()
    log.info(c)

    try:
        1/0
    except ZeroDivisionError as e:
        log.exception(e)
        
    raise RuntimeError("Horrible things have happened!!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log.exception(e)
        raise

