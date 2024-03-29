"""
URL Auto Loader.

This file is used to automatically load all urls from app.api submodules.

DO NOT EDIT THIS FILE.

"""
import pkgutil

from django import urls
from django.conf import settings


def load_urls() -> list[urls.URLPattern]:
    """
    Iterate app.api submodules, look for a module called PACKAGE_NAME_urls.py and load the urls,
        appending them to the urls
    :return: list of urls
    """
    patterns = []
    base_path = settings.BASE_DIR / "app" / "api"
    # Iterate app.api submodules
    for module in pkgutil.iter_modules([base_path]):
        # Look for a submodule (file) called PACKAGE_NAME_urls.py
        for submodule in pkgutil.iter_modules([base_path / module.name]):
            if submodule.name.endswith("_urls"):
                # Load the urls, appending them to the urls list
                urls_module = __import__(f"app.api.{module.name}.{submodule.name}", fromlist=["*"])
                patterns.append(
                    urls.path(
                        f"{module.name}/",
                        urls.include(urls_module, namespace=module.name),
                    )
                )
    return patterns


urlpatterns = load_urls()
