"""
This module contains the functions for creating new modules in the app/api directory.
"""

from django.conf import settings
from mako.template import Template


def make_api_module(name: str):
    """
    Creates a new module in app/api with the given name using the boilerplate templates.
    """
    module_path = settings.BASE_DIR / "app" / "api" / name
    if module_path.exists():
        raise FileExistsError(f"API module {name} already exists.")
    module_path.mkdir()
    # Create boilerplate files
    boilerplate_path = settings.BASE_DIR / "app" / "management" / "module_maker" / "boilerplate"
    for file in boilerplate_path.iterdir():
        if file.suffix != ".mako":
            continue
        with open(file, "r", encoding="utf8") as f:
            template = Template(f.read())
        with open(
            module_path / file.name.format(name=name).replace(".mako", ""),
            "w",
            encoding="utf8"
        ) as f:
            f.write(template.render(name=name))
