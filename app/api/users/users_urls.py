"""
users urls
"""

from django import urls

from app.api.users import users_endpoints


app_name = "users"  # pylint: disable=invalid-name


urlpatterns = [
    urls.path(
        "class-view/",
        users_endpoints.TestAPIView.as_view(),
        name="'test_class_based_api_view'"
    ),
    urls.path(
        "api-view/",
        users_endpoints.test_api_view,
        name="test_api_view"
    ),
]

