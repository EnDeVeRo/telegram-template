import json
import requests


def create_example():
    url = f"http://127.0.0.1/create"
    filters = {"user_name": "Ivan"}
    params = {"user_id": 666, "user_name": "Ivan"}
    data = {"filters": json.dumps(filters), "params": json.dumps(params)}
    response = requests.get(url=url, params=data)
    print(response.json())


if __name__ == '__main__':
    create_example()