from asgiref.sync import sync_to_async
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@sync_to_async
@api_view(['GET'])
def sync_to_async_view(request):
    for i in range(0, 100000):
        print(i)

    return Response(
        data={
            "TEST sync_to_async TEST"
        }, status=status.HTTP_200_OK
    )


@api_view(['GET'])
def sync_view(request):
    for i in range(0, 100000):
        print(i)

    return Response(
        data={
            "TEST sync TEST"
        }, status=status.HTTP_200_OK
    )
