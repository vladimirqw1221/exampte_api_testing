import datetime
import os
from requests import Response



class Logger:
    logger_patch = f"logs/logs_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}" + ".log"

    @classmethod
    def _write_logs_file(cls, data: str):
        with open(cls.logger_patch, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def request_logs(cls, url : str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        add_as_data = f"\n-----\n"
        add_as_data += f"Test name: {test_name}\n"
        add_as_data += f"Date: {datetime.datetime.now()}\n"
        add_as_data += f"URL: {url}\n"
        add_as_data += f"Method: {method}\n"
        add_as_data += f"-----\n"

        cls._write_logs_file(add_as_data)

    @classmethod
    def response_logs(cls, response: Response):
        headers_logs = dict(response.headers)
        cookie_logs = dict(response.cookies)

        add_as_data = f"Status code: {response.status_code}\n"
        add_as_data += f"Headers: {headers_logs}\n"
        add_as_data += f"Cokkie: {cookie_logs}\n"
        add_as_data += f"-----\n"

        cls._write_logs_file(add_as_data)


