python-logging-configuration
============================

Best practice logging configuration example.

This is a simple package, demonstrating a good practice for doing logging in python.

The logconfig.py module offers a default configuration and convenience functions 
and can be dropped directly into any python application.

Demonstrated use:

 * logconfig.py - copy this into your project and call logconfig.setup_logging()
                  from the __main__ module or main() function.
 * myclasses.py - Logging in a library using loggers named by module.class.
 * demoapp.py   - Logging and log configuration in an application.

