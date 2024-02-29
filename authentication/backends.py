from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
    """
    Custom authentication backend for authenticating users using their email address.

    This backend extends the ModelBackend provided by Django and allows users to log in using their email
    instead of their username. It overrides the `authenticate` method to handle authentication based on email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Method for authenticating users based on their email address.

        Args:
            request: The HTTP request.
            username: The username or email provided by the user for authentication.
            password: The password provided by the user.
            **kwargs: Additional keyword arguments.

        Returns:
            The authenticated user object if successful, or None if authentication fails.
        """
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None