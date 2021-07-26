import asyncio
import time

from asgiref.sync import sync_to_async
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.decorators import sync_and_async_middleware


@sync_and_async_middleware
def simple_middleware(get_response):
    # One-time configuration and initialization goes here.
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            # Do something here!
            response = await get_response(request)
            return response

    else:
        def middleware(request):
            # Do something here!
            response = get_response(request)
            return response

    return middleware


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


async def async_view(request):
    await asyncio.sleep(1)
    return HttpResponse("Made a pretty page asynchronously.")
