from pydantic import BaseModel, Field, EmailStr, constr

# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: constr(str, min_length=1) = Field(alias="lastName")
    first_name: constr(str, min_length=1) = Field(alias="firstName")
    middle_name: constr(str, min_length=1) = Field(alias="middleName")

# Добавили модель CreateUserRequestSchema
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: constr(str, min_length=8)
    last_name: constr(str, min_length=1) = Field(alias="lastName")
    first_name: constr(str, min_length=1) = Field(alias="firstName")
    middle_name: constr(str, min_length=1) = Field(alias="middleName")

# Добавили модель CreateUserResponseSchema
class CreateUserResponseSchema(BaseModel):
    user: UserSchema