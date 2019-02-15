import os
import sys
import fixate.config
import logging
from fixate.sequencer import Sequencer

__version__ = '0.4.3'

logger = logging.getLogger(__file__)


def load_config(config: str = '', config_name: str = ""):
    """
    Load a list of config files into fixate.config.<optional config name>
    :param config:
    :param config_name:
    :return:
    """
    if os.path.exists(config):
        fixate.config.load_yaml_config(config, config_name)
        logger.debug("Loaded Config File {}".format(config))
    else:
        logger.info("Config file {} was not found".format(config))


fixate.config.RESOURCES["SEQUENCER"] = Sequencer()
logger.debug("Loaded sequencer")
# Load the fixate default configurations
load_config(os.path.join(sys.prefix, "fixate.yml"))
load_config(os.path.join(sys.prefix, "fixate-local.yml"), "local")
