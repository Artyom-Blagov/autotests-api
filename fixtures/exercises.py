import pytest
from pydantic import BaseModel

from fixtures.users import UserFixture
from clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema

class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercise_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture
def function_client(exercise_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExerciseRequestSchema()
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)