"""
${name} urls
"""

from django import urls

from app.api.${name} import ${name}_endpoints


app_name = "${name}"  # pylint: disable=invalid-name


urlpatterns = [
    urls.path(
        "class-view/",
        ${name}_endpoints.TestAPIView.as_view(),
        name='"test_class_based_api_view'"
    ),
    urls.path(
        "api-view/",
        ${name}_endpoints.test_api_view,
        name="test_api_view"
    ),
]

