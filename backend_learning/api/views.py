from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  
from rest_framework import status

# ✅ User Registration API (No authentication required)
@api_view(['POST'])
@permission_classes([AllowAny])  # ✅ Allow access without authentication
def register_user(request):
    """Registers a new user and generates a token."""
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if user already exists
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    # Create the user
    user = User.objects.create_user(username=username, password=password)

    # Generate a token for the new user
    token, _ = Token.objects.get_or_create(user=user)

    return Response({"message": "User registered successfully", "token": token.key}, status=status.HTTP_201_CREATED)

# ✅ User Login API (No authentication required)
@api_view(['POST'])
@permission_classes([AllowAny])  # ✅ Allow access without authentication
def login_user(request):
    """Logs in a user and returns a token."""
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.filter(username=username).first()

    if user and user.check_password(password):
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"message": "Login successful", "token": token.key})
    
    return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ User Logout API (Requires authentication)
@api_view(['POST'])
def logout_user(request):
    """Logs out the user by deleting their token."""
    if request.user.is_authenticated:
        request.user.auth_token.delete()
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    
    return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
