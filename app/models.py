"""
Models Auto Loader

This file is used to load all models in the app.api submodules.

DO NOT EDIT THIS FILE.

"""

import pkgutil

from django.conf import settings
from django.db import models


def load_models():
    """
    Load all models in the app.api submodules.

    This method will iterate modules in the app.api package. Then iterate submodules and search for
    a file named PACKGE_NAME_models.py. If this file is found, import all the classes that are
    instances of models.Model in the global scope
    """
    base_path = settings.BASE_DIR / "app" / "api"
    for module in pkgutil.iter_modules([base_path]):
        for submodule in pkgutil.iter_modules([base_path / module.name]):
            if submodule.name.endswith("_models"):
                module = __import__(f"app.api.{module.name}.{submodule.name}", fromlist=["*"])
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, models.Model):
                        globals()[attr_name] = attr


load_models()
