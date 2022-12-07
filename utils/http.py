import requests


def request_handler(method, host, url, data, dry_run=True):
    if not dry_run:
        uri = host + url
        header = {
            "Content-Type": "application/json"
        }
        if method == 'GET':
            response = requests.get(
                uri,
                headers=header,
                json=data
            )
        elif method == 'POST':
            response = requests.post(
                uri,
                headers=header,
                json=data
            )
        elif method == 'PUT':
            response = requests.put(
                uri,
                headers=header,
                json=data
            )
        elif method == 'DELETE':
            response = requests.delete(
                uri,
                headers=header,
                json=data
            )
        else:
            return None, False

        return response, True
    else:
        return None, True


def response_handler(response):
    return_code = 0
    message = None
    if response.status_code != 200:
        if response.status_code == 400 or response.status_code == 404 or response.status_code == 422:
            result = response.json()
            return_code = result["return_code"]
            message = result["message"]
        if response.status_code == 403:
            return_code = 403
            message = "forbidden"

    else:
        result = response.json()
        return_code = result["return_code"]
        message = result["message"]

    return response.status_code, return_code, message
