import sys
import os
import json
import requests
from requests.exceptions import ConnectionError

HOST = os.environ.get('CONVERTOR_HOST', 'http://localhost')
PORT = os.environ.get('CONVERTOR_PORT', '7575')
BASE_URL = HOST + ":" + PORT + "/convert/"


def convert_file(file_path: str, target: str, out=sys.stdout) -> None:
    with open(file_path) as f:
        index = 0
        while True:
            index = index + 1
            line = f.readline()
            if not line:
                break  # This has a caveat that it will not process the rest of the file in case of an empty line in the middle of the file
            try:
                data = json.loads(line.strip())
                value = data["value"]
                currency = data["currency"]
                url = BASE_URL + target
                response = requests.get(
                    url, params={"currency": currency, "value": value}
                )
                if response.ok:
                    out.write(response.text + '\n')
                else:
                    raise ValueError(response.json()["detail"])
            except KeyError as e:
                out.write(
                    "Invalid input format at line: "
                    + str(index)
                    + " | Key Error: "
                    + str(e)
                )
            except ValueError as e:
                out.write(
                    "Invalid input for API at line: "
                    + str(index)
                    + " | Error Msg: "
                    + str(e)
                )
            except ConnectionError as e:
                out.write(
                    f"Are you sure the server is running on {BASE_URL}? \n"
                )
                return
