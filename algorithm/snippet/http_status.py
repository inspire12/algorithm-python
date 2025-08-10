def http_status(code: int) -> str:
    match code:
        case 200 | 204:
            return "success"
        case 400:
            return "bad request"
        case 401 | 403:
            return "auth error"
        case _ if 500 <= code < 600:
            return "server error"
        case _:
            return "unknown"

print(http_status(403))