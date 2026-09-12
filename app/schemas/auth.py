# app/schemas/auth.py
# This file is a list of "boxes" that hold data for the authentication (login/signup) features.
# Each box tells the app exactly what information is allowed to go in and out.
# Every line below has a simple comment explaining what it does.

from typing import Optional  # A word that means "this box is allowed to be empty".
from pydantic import (  # A tool that checks and shapes data automatically.
    BaseModel,  # The parent class that turns a "box" into a real, usable Python object.
    EmailStr,  # A special type of text that must look like an email address (like name@site.com).
    Field,  # A tool that adds extra rules to a box (like "the password must be long enough").
)


# The box for creating a new account (signup).
class UserSignUp(BaseModel):
    email: EmailStr  # The new user's email address (must look like a real email).
    password: str = Field(min_length=8)  # The new user's password (must have at least 8 letters/numbers).
    full_name: Optional[str] = None  # The new user's full name (can be empty if they do not give one).
    role: str = "student"  # The type of user (defaults to "student", could be "tutor").


# The box for logging into an existing account.
class UserLogin(BaseModel):
    email: EmailStr  # The user's email address.
    password: str  # The user's password.


# The box for the answer we send back after a successful login.
class TokenResponse(BaseModel):
    access_token: str  # The secret login key the app must keep and use for other requests.
    token_type: str = "bearer"  # The kind of key it is (always "bearer" here).
    user_id: str  # The user's ID number.
    email: Optional[EmailStr] = None  # The user's email address (can be empty).
    expires_in: Optional[int] = None  # How many seconds until the login key stops working.


# The box for the answer we send back after a successful signup.
class SignupResponse(BaseModel):
    message: str  # The friendly text telling the user what happened.
    user_id: str  # The new user's ID number.
    email: EmailStr  # The email address that was used to sign up.
    needs_email_confirmation: bool  # True if the user must still click a link in their email before logging in.


# The box for sending user details back to the app (used by "show me" and profile routes).
class UserResponse(BaseModel):
    id: str  # The user's ID number.
    email: Optional[EmailStr] = None  # The user's email address (can be empty).
    role: Optional[str] = None  # The user's role, like "student" or "tutor" (can be empty).
    full_name: Optional[str] = None  # The user's full name (can be empty).
    created_at: Optional[str] = None  # When the account was created, as text (can be empty).


# The box for changing profile details (like name or role).
class UserProfileUpdate(BaseModel):
    full_name: Optional[str] = None  # The new full name to save (can be empty).
    role: Optional[str] = None  # The new role to save, like "student" or "tutor" (can be empty).


# The box for a "I forgot my password" request.
class PasswordResetRequest(BaseModel):
    email: EmailStr  # The email address the reset link should be sent to.