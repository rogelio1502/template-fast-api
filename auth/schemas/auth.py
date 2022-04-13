from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="user@domain.com",
    )


class UserAuth(UserBase):
    password: str = Field(
        ...,
        min_length=7,
        max_length=50,
        example="passwordsopro",
    )


class UserSignUpOut(BaseModel):
    message: str = Field(..., example="done")


class UserLoginOut(BaseModel):

    accessToken: str = Field(..., example="user.token.value")
    email: str = Field(...)


class UserSignup(BaseModel):
    email: EmailStr = Field(
        ...,
        example="user@domain.com",
    )
    password: str = Field(
        ...,
        min_length=7,
        max_length=50,
        example="passwordsopro",
    )
