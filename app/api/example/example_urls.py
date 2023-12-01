
from django import urls

from app.api.example import example_endpoints


app_name = 'example'


urlpatterns = [
    urls.path('class-view/', example_endpoints.TestAPIView.as_view(), name='test_class_based_api_view'),
    urls.path('api-view/', example_endpoints.test_api_view, name='test_api_view'),
]

