import gzip
import json
import codecs
from collections import OrderedDict
from typing import Any


def load_json_gz(filename: str) -> Any:
    reader = codecs.getreader('utf-8')
    with gzip.open(filename) as f:
        return json.load(reader(f), object_pairs_hook=OrderedDict)


def save_json_gz(data: Any, filename: str) -> None:
    writer = codecs.getwriter('utf-8')
    with gzip.GzipFile(filename, 'wb') as outfile:
        json.dump(data, writer(outfile))