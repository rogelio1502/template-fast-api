import bcrypt

from auth.schemas.auth import UserAuth, UserSignup
from auth.auth_handler import signJWT

from db.models_api.Users import Users
from .Exceptions import BadRequest


def get_user_auth_data(user: UserAuth, role: str):

    token = signJWT(user.email).get("access_token")

    return {"accessToken": token, "email": user.email}


def check_user(data: UserAuth):
    user = Users.get_user_by_email(data.email)
    if user:
        if bcrypt.checkpw(
            data.password.encode("utf-8"), user.get("password").encode("utf-8")
        ):
            return True

    raise Exception("Wrong Credentials or user does not exist.")


def sign_up(user: UserAuth):
    plain_password = user.password.encode("utf-8")

    user_normal = UserSignup(email=user.email, password=user.password)

    user_normal.password = bcrypt.hashpw(plain_password, bcrypt.gensalt())

    registered = Users.insert(user_normal.dict())
    if registered:
        return {"message": "User has been created."}
    raise Exception("Something Went Wrong")
