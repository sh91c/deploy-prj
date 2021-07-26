from asgiref.sync import sync_to_async
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@sync_to_async
@api_view(['GET'])
def test_view(request):
    for i in range(0, 100):
        print(i)

    return Response(
        data={
            "success"
        }, status=status.HTTP_200_OK
    )