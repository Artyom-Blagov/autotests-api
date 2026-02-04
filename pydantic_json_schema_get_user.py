from api_client_get_user import private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.fakers import get_random_email
from tools.assertions.schema import validate_json_schema
import jsonschema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user_api(create_user_request)
private_users_client.get_user_api(create_user_response)