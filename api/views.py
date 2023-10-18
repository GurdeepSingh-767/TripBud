from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework import permissions
import stripe
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def CustomUserCreate(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        
@api_view(['POST'])
def CustomUserLogin(request):
    if request.method == 'POST':
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None

        if not user:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user and user.password == password:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response({'access_token': access_token, 'refresh_token': refresh_token}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
        


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripPhotosViewSet(viewsets.ModelViewSet):
    queryset = TripPhotos.objects.all()
    serializer_class = TripPhotosSerializer





from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


stripe.api_key = 'sk_test_51O2ahASFoylgLrMye3TqRpXEjb3TWNbwG9ISupPRMM2dmibhc3Y7y01S1w702IgjkBTXaAkiLvckLGWm0KM4iSkA00h2iCbbqN'

@require_POST
@csrf_exempt
def create_checkout_session(request, trip_id):
    try:
        trip = Trip.objects.filter(trip_id=trip_id)
        data = serializers.serialize('json', trip)
        serialized_data = json.loads(data)
        fields = serialized_data[0]['fields']
        print("helloo:",fields)
        # You may fetch other details like price from the 'trip' object
        # Replace 'price' with the actual field name in your Trip model.
        price = float(fields['accommodation_per_trip'])  # Adjust this based on your Trip model structure
        print(price)
        
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': fields['trip_name'],  # Name of the trip
                        },
                        'unit_amount': int(price * 100),  # Convert price to cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:5173/home/',  # Define your success URL
            cancel_url='http://127.0.0.1:5173/home/',    # Define your cancel URL
        )
        print(checkout_session.id)
        return JsonResponse({'sessionId': checkout_session.id})
    except Trip.DoesNotExist:
        return JsonResponse({'error': 'Trip not found'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

