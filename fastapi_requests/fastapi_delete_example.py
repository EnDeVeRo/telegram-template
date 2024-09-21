import json
import requests


def delete_example():
    url = f"http://127.0.0.1/delete"
    filters = {"user_name": "Ivan"}
    data = {"filters": json.dumps(filters)}
    response = requests.get(url=url, params=data)
    print(response.json())


if __name__ == '__main__':
    delete_example()