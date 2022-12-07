from utils.http import request_handler, response_handler


def login(host, data):
    output_data = {}
    try:
        response, flag = request_handler(
            method="PUT",
            host=host,
            url="/api/v4/login",
            data=data,
            dry_run=False
        )

        if not flag:
            message = "failed"
            return False, message, output_data

        response_handler(response)

        message = "success"
        return True, message, output_data
    except ConnectionError:
        message = "ConnectionError"
        return False, message, output_data
    except Exception:
        message = "failed"
        return False, message, output_data

