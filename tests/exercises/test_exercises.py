import pytest

from http import HTTPStatus

from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from fixtures.courses import CourseFixture, function_course
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        create_request = CreateExerciseRequestSchema(
            course_id=function_exercise.response.exercise.course_id
        )
        create_response = exercises_client.create_exercise_api(create_request)
        create_response_data = CreateExerciseResponseSchema.model_validate_json(create_response.text)

        get_response = exercises_client.get_exercise_api(create_response_data.exercise.id)
        get_response_data = GetExerciseResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(get_response_data, create_response_data.exercise)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())