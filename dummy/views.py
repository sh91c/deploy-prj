import asyncio
import time

from asgiref.sync import sync_to_async
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@sync_to_async(thread_sensitive=False)
@api_view(['GET'])
def sync_to_async_view(request):
    time.sleep(1)
    return Response(
        data={
            "TEST sync_to_async TEST"
        }, status=status.HTTP_200_OK
    )


@api_view(['GET'])
def sync_view(request):
    time.sleep(1)
    return Response(
        data={
            "TEST sync TEST"
        }, status=status.HTTP_200_OK
    )

@api_view(['GET'])
async def non_deco_async_view(request):
    await asyncio.sleep(1)

    return Response(
        data={
            "TEST non_deco_async TEST"
        }, status=status.HTTP_200_OK
    )