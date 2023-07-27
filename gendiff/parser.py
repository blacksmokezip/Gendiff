import json
import yaml
from pathlib import Path


def read_file(path):
    data = open(path, 'r')
    return data


def get_format(path):
    format = Path(path).suffix
    return format[1:]


def parse(data, format):
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(data)
    return json.load(data)
