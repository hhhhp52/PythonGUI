import logging

import constants


def get_host_by_env(env):
    env_host = None
    if env == constants.LOCAL:
        env_host = constants.LOCAL_HOST
    elif env == constants.DEV:
        env_host = constants.DEV_HOST
    elif env == constants.STAGING:
        env_host = constants.STAGING_HOST
    else:
        logging.log(level=0, msg="Not permit env")
    return env_host
