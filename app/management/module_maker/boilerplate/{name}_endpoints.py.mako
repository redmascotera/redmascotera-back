"""
${name} endpoints
"""

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test_api_view(request):
    return Response({'message': 'Hello, World!'})


class TestAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})
