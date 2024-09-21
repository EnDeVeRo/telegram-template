import json
import requests


def delete_example():
    url = f"http://127.0.0.1/update"
    filters = {"user_name": "Ivan"}
    params = {"user_name": "Anton"}
    data = {"filters": json.dumps(filters), "params": json.dumps(params)}
    response = requests.get(url=url, params=data)
    print(response.json())


if __name__ == '__main__':
    delete_example()