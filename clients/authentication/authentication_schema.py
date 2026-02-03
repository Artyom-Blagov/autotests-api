from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel): # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class LoginResponseSchema(BaseModel): # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры ответа на аутентификацию.
    """
    token: TokenSchema

class RefreshRequestSchema(BaseModel): # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")  # Название ключа совпадает с API