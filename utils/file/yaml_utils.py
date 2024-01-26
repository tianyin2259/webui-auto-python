import traceback

import yaml

from common.setting import Path
from utils.log.loguru_utils import Logger


class YamlUtils:
    def __init__(self):
        self.root_path = Path()
        self.common_path = self.root_path.common_path
        self.data_path = self.root_path.data_path

    def read_yaml(self, filename):
        try:
            with open(filename, "r", encoding="utf8") as f:
                result = yaml.load(f, Loader=yaml.SafeLoader)
                return result
        except Exception as e:
            Logger().error(traceback.format_exc())

    def write_data(self, filename, data):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                yaml.dump(data, f, Dumper=yaml.SafeDumper, allow_unicode=True, default_flow_style=False)

        except Exception as e:
            Logger().error(traceback.format_exc())




