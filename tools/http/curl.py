'''from httpx import Request
def make_curl_from_request(request: Request) -> str:
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    if
'''