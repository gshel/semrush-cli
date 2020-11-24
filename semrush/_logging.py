import logging
from logging.config import dictConfig


def configure_console_logger(
    logging_level: int = 20,
    disable_level: int = 0,
    disable_external_lib_loggers: bool = True,
):
    """Configurationg for logging to the console."""
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "f": {"format": f"%(asctime)s %(levelname)s [%(module)s.%(funcName)s:%(lineno)s] - %(message)s"}
            },
            "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "f", "level": logging_level,}},
            "root": {"handlers": ["console"], "level": logging_level},
            "disable_existing_loggers": disable_external_lib_loggers,
        }
    )
    if disable_level:
        logging.disable(disable_level)


# order matters when setting the verbosity: if a module's logger is init-ed _before_ the verbosity is set, the new
## logger will be disabled. We try to reduce human error by returning the module's logger after setting verbosity here.
def set_verbosity(module_name: str, verbose: bool = False, very_verbose: bool = False) -> logging.Logger:
    """
    Used to set the verbosity of the logger.
    :param module_name: Name of the module, e.g. ``__name__``.
    :type module_name: str
    :param verbose: Enables DEBUG level.
    :type verbose: bool
    :param very_verbose: Enables DEBUG level and the loggers from imported libraries.
    :type very_verbose: bool
    :return: A configured logger, which can be used throughout the code via ``logging.{LEVEL}()``.
    :rtype: logging.Logger
    """
    if very_verbose:
        configure_console_logger(logging_level=logging.DEBUG, disable_external_lib_loggers=False)
    elif verbose:
        configure_console_logger(logging_level=logging.DEBUG)
    else:
        configure_console_logger(logging_level=logging.INFO)

    return logging.getLogger(module_name)