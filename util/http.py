import requests


def request_handler(method, host, header, url, data, dry_run=True):
    if not dry_run:
        uri = host + url
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
    data = None
    if response.status_code != 200:
        if response.status_code in (400, 401, 404, 422):
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
        data = result["data"]

    return response.status_code, return_code, message, data
