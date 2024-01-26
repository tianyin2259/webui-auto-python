from common.setting import Path
from utils.other.models import Config
from utils.file.yaml_utils import YamlUtils

_data = YamlUtils().read_yaml(Path.common_path + "config.yaml")
config = Config(**_data)


def allure_utils():
    return None