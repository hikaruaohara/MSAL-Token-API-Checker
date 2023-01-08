import requests
import sys
from get_token import acquire_token

# Add endpoints to this dictionary
url_dict = {
    'graph': 'https://graph.microsoft.com/v1.0/me'
}


def call_api(mode, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url_dict.get(mode), headers=headers)

    return response


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: 'python get_token_and_call_api.py <mode>'")
        exit(1)

    acquire_tokens_result = acquire_token(mode=sys.argv[1])
    responce = call_api(
        mode=sys.argv[1],
        access_token=acquire_tokens_result['access_token']
    )
    print(f'Status Code: {responce.status_code}')
    print(responce.text)
