import logging
from datetime import date
from pathlib import Path



def initilize():
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))

    logging.basicConfig(filename="../novatron/logs/{}.log".format(today.strftime("%d %B %Y")),
                        format='%(asctime)s - (filename)s - %(name)s - %(levelname)s - %(message)s'
                        )


def for_settings():
    initilize()
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))

    logging.basicConfig(filename="../logs/{}.log".format(today.strftime("%d %B %Y")),
                        format='%(asctime)s - (filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging






def debug_debug(message):
    initilize()
    return for_settings().debug(message)




def debug_info(message):
    initilize()
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))

    logging.basicConfig(filename="../novatron/logs/{}.log".format(today.strftime("%d %B %Y")),
                        format='%(asctime)s - (filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.info(message)





def debug_warning(message):
    initilize()
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))

    logging.basicConfig(filename="../novatron/logs/{}.log".format(today.strftime("%d %B %Y")),
                        format='%(asctime)s - (filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.warning(message)


''' Converts the cross balance in the API to the base value equivalence for buy purposes'''


def debug_error(message):
    initilize()
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))

    logging.basicConfig(filename="../logs/{}.log".format(today.strftime("%d %B %Y")),
                        format='%(asctime)s - (filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.error(message)


''' Converts the cross balance in the API to the base value equivalence for buy purposes'''


def debug_critical(message):
    initilize()
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../novatron/logs/{}.log".format(today.strftime("%d %B %Y")))

    logging.basicConfig(filename="../novatron/logs/{}.log".format(today.strftime("%d %B %Y")),
                        format='%(asctime)s - (filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.critical(message)


# debug_debug('Ujanja pale chini')
# debug_info('Ujanja pale chini')
# debug_warning('Ujanja pale chini')
# debug_error('Ujanja pale chini')
# debug_critical(debug_error('Ujanja pale chini'))
