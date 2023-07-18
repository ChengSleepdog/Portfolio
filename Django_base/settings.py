# -*- coding: utf-8 -*-
import os
import yaml
import logging.config

# change this environment variable for the deployment
ENVIRONMENT = os.getenv("API_ENVIRONMENT", "dev")

logger_config_file = os.getenv("LOGGER_CONFIG_FILE", 'utils/logger_unit/init_logger.yaml')

# 讀取並配置日誌
with open(logger_config_file, "r") as config_file:
    config = yaml.safe_load(config_file.read())
    logging.config.dictConfig(config)

# test in localhost(including postgres/redis running as docker container)
# ENVIRONMENT = os.getenv("API_ENVIRONMENT", "test_in_localhost")

# apply config!!!
DJANGO_CONF_MODULE = "config.{env}".format(env=ENVIRONMENT)

try:
    _module = __import__(DJANGO_CONF_MODULE, globals(), locals(), ["*"])
except ImportError as e:
    raise ImportError("Could not import config '{}' (Is it on sys.path?): {}".format(
        DJANGO_CONF_MODULE, e))

for _setting in dir(_module):
    if _setting == _setting.upper():
        locals()[_setting] = getattr(_module, _setting)
