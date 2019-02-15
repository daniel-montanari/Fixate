import fixate.config
import importlib


def find(alias):
    """
    Finds an implemented driver from the loaded fixate-local.yml and from the fixate-local.yml files provided in the
    test script folder that is launched
    :param alias: Alias of the resource you are trying to find. Set in config as
    <alias>:
       cls: <import path>:<class>
       params:
          <params to pass to the class on instantiation>
    :return: Instantiated class by that alias
    """
    try:
        conf = fixate.config.local[alias]
    except KeyError as e:
        raise ValueError("No known alias {}\nPlease check fixate-local.yml is set up correctly".format(alias)) from e
    imp_str, cls_str = conf["cls"].split(":")
    imp = importlib.import_module(imp_str)
    cls = getattr(imp, cls_str)
    return cls(**conf["params"])
