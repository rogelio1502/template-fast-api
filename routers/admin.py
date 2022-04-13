from sqlalchemy.exc import IntegrityError, OperationalError
from fastapi import APIRouter, Body

from auth.schemas.auth import UserAuth, UserLoginOut, UserSignUpOut

from utils.handler_exceptions import handler_exception
from utils.Auth import sign_up, check_user, get_user_auth_data


router_admin = APIRouter(
    prefix="",
    tags=["User"],
)


@router_admin.post(
    path="/signup",
    response_model=UserSignUpOut,
)
async def create_user(user: UserAuth = Body(...)):

    """
    - This Path Operation Function create an user in the app/db

    - Gets a Json Body/ UserAuth Model with the following data:
        - email
        - password

    - Returns an UserSingUpOut Model with the following data:
        - email
        - token
    """
    try:
        return sign_up(user)
    except IntegrityError as e:
        handler_exception(e, 400)
    except OperationalError as e:
        handler_exception(e, 500)
    except Exception as e:
        try:
            if e.status_code:
                pass
        except:
            handler_exception(e, 500)
        else:
            handler_exception(e, e.status_code)


@router_admin.post(path="/login", response_model=UserLoginOut, summary="Login.")
async def user_login(user: UserAuth = Body(...)):
    """
    ### Login.

    This Path Operation Function allows the user login in the app.

    Gets an UserAuth model with the following data:
       - *email*
       - *password*

    Returns a JSON base on the UserLoginOut model that contains only one value: *token*.

    """
    try:
        first_validation = check_user(user)
        if first_validation == True:
            return get_user_auth_data(user)
        raise Exception("Wrong Credentials")

    except Exception as e:
        if "Wrong Credentials" in str(e):
            handler_exception(e, 401)
        handler_exception(e, 500)
