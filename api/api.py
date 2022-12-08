from entity.user import user
from util.http import request_handler, response_handler


def login(host, account, password):
    header = {
        "User-Agent": "application",
        "Cache-Control": "no-cache",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Connection": "keep-alive"
    }
    data = dict(
        email=account,
        password=password,
        device_id="macOS",
        device_token="",
        device_type="laptop"
    )
    try:
        response, flag = request_handler(
            method="POST",
            host=host,
            header=header,
            url="/api/v4/login",
            data=data,
            dry_run=False
        )

        if not flag:
            message = "failed"
            return False, message
        status_code, return_code, message, data = response_handler(response)
        user.set_user_default(
            access_token=data.get("access_token"),
            account=account,
            device_id="macOS"
        )
        return True, message
    except ConnectionError:
        message = "ConnectionError"
        print(message)
        return False, message
    except Exception as e:
        print(e)
        message = "Exception"
        return False, message


def launch(host):
    header = {
        "User-Agent": "application",
        "Cache-Control": "no-cache",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "X-Access-Token": user.access_token,
        "X-Device-Id": user.device_id,
        "X-App-Version": "1.0.0"
    }
    data = dict()
    try:
        response, flag = request_handler(
            method="GET",
            host=host,
            header=header,
            url="/api/v2/launch",
            data=data,
            dry_run=False
        )

        if not flag:
            message = "failed"
            return False, message

        status_code, return_code, message, data = response_handler(response)
        user.set_user_name(
            first_name=data["profile"].get("first_name"),
            last_name=data["profile"].get("last_name")
        )
        user.set_user_glucose_unit(
            glucose_unit=data["settings"].get("glucose_unit")
        )
        return True, message
    except ConnectionError:
        message = "ConnectionError"
        return False, message
    except Exception:
        message = "failed"
        return False, message
