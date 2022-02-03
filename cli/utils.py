import json
import requests


BASE_URL = "http://localhost:7575/convert/"


def convert_file(file_path, target):
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
                    print(response.json())
                else:
                    raise ValueError(response.json()["detail"])
            except KeyError as e:
                print(
                    "Invalid input format at line: "
                    + str(index)
                    + " | Key Error: "
                    + str(e)
                )
            except ValueError as e:
                print(
                    "Invalid input for API at line: "
                    + str(index)
                    + " | Error Msg: "
                    + str(e)
                )
