import allure


@allure.step("Building API client")
def build_api_client():
    with allure.step("Get user authentication tokens"):
        ...

    with allure.step("Create new API client"):
        ...


@allure.step("Creating course")
def create_course():
    ...


@allure.step("Deleting course")
def delete_course():
    ...


def test_feature():
    build_api_client()
    delete_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwrights")