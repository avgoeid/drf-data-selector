import importlib

from django.conf import settings


def load(path):
    path_list = path.split(".")
    cls_name = path_list[-1]
    sub_path = ".".join(path_list[:-1])
    m = importlib.import_module(sub_path)

    return getattr(m, cls_name)


selectors = (load(i) for i in settings.DATA_SELECTORS)
