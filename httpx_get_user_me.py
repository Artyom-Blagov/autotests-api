import httpx

login_payload = {
    "email": "admin@mail.ru",
    "password": "12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",json=login_payload)
login_response_data = login_response.json()

print("Status code:", login_response.status_code)
print("Login response:",login_response_data)

access_token = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {access_token}"}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
me_response_data = me_response.json()

print("Status code:", me_response.status_code)
print("Me response:",me_response_data)