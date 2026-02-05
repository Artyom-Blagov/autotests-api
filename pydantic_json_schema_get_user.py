from pydantic.json_schema import model_json_schema

from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from tools.assertions.schema import validate_json_schema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user_api(create_user_request)

# Валидируем Response через Pydantic схему
create_user_data = CreateUserResponseSchema.model_validate(create_user_response.json())

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос о созданном пользователе
get_user_response = private_users_client.get_user_api(user_id=create_user_data.user.id)
print(get_user_response.json())

# Валидируем GET Response через Pydantic схему
get_user_data = GetUserResponseSchema.model_validate(get_user_response.json())

# Валидация JSON схемы
get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_data.model_dump(by_alias=True), schema=get_user_response_schema)

