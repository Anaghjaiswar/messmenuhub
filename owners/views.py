from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer,LoginSerializer
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate


# Dashboard view
def dashboard(request):
    return render(request, 'owners/MessOwners_dashboard.html')


# Manage menu view
def manage_menu(request):
    return render(request, 'owners/manage-menu.html')

# Signup page view
def signup(request):
    return render(request, 'owners/signuppage.html')

# Login page view
def login(request):
    return render(request, 'owners/loginpage.html')

# Menu posting view
def menu_posting(request):
    return render(request, 'owners/menu_posting.html')

# Resources view
def resources(request):
    return render(request, 'owners/resources.html')


def special_offers_promotions(request):
    return render(request, 'owners/special_offers_promotions.html')

def help_guidelines(request):
    return render(request, 'owners/help_guidelines.html')


def contact_support(request):
    return render(request, 'owners/contact_support.html')

def announcements(request):
    return render(request, 'owners/announcements.html')


# Signup View
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Return token and user data (we will return JWT token)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        # print("Validation Errors:", serializer.errors)
        # print("Request Data:", request.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Use username for authentication
        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Generate the JWT token for the user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response(
            {"access": access_token},
            status=status.HTTP_200_OK,
        )