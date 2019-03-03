import configparser

# Create config parser
config = configparser.ConfigParser()
config.read('../CONFIG.ini')


def get_params(section):
    """
    Takes as parameter a section from the CONFIG.ini file and return a list containing the values
    of that section, also the keys for the value can be extracted as item[0]
    """
    values = []
    items = config.items(section)
    for item in items:
        values.append(item[1])
    return values
