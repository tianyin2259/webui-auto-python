import os

from loguru import logger

from common.setting import Path


class Logger:
    if not os.path.exists(Path.logs_path):
        os.mkdir(Path.logs_path)

    __log_path = Path.logs_path

    @staticmethod
    def info(msg):
        """

        :param msg:
        :return:
        """
        logger.add(f"{Logger.__log_path}{os.sep}info.log", rotation="500MB",
                   encoding="utf-8", enqueue=True,
                   retention="10 days")
        return logger.info(msg)

    @staticmethod
    def debug(msg):
        """

        :param msg:
        :return:
        """
        logger.add(f"{Logger.__log_path}{os.sep}debug.log", rotation="500MB",
                   encoding="utf-8", enqueue=True,
                   retention="10 days")
        return logger.debug(msg)

    @staticmethod
    def warning(msg):
        """

        :param msg:
        :return:
        """
        logger.add(f"{Logger.__log_path}{os.sep}warning.log", rotation="500MB",
                   encoding="utf-8", enqueue=True,
                   retention="10 days")
        return logger.warning(msg)

    @staticmethod
    def error(msg):
        """

        :param msg:
        :return:
        """
        logger.add(f"{Logger.__log_path}{os.sep}error.log", rotation="500MB",
                   encoding="utf-8", enqueue=True,
                   retention="10 days")
        return logger.error(msg)


if __name__ == '__main__':
    Logger.info("info")
    Logger.debug("debug")
    Logger.warning("warning")
    Logger.error("error")
