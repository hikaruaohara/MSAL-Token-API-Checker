from msal import PublicClientApplication
import sys

CLIENT_ID = 'YOUR CLIENT ID'
TENANT_ID = 'YOUR TENANT ID'

# Add Scopes to this dictionary
scope_dict = {
    'graph': 'user.read'
}


def acquire_token(mode):
    app = PublicClientApplication(
        client_id=CLIENT_ID,
        authority="https://login.microsoftonline.com/" + TENANT_ID
    )

    try:
        acquire_tokens_result = app.acquire_token_interactive(
            scopes=[scope_dict[mode]]
            )
    except KeyError:
        print(create_error_message())
        exit(1)

    if 'error' in acquire_tokens_result:
        print("Error: " + acquire_tokens_result['error'])
        print("Description: " + acquire_tokens_result['error_description'])
        exit(1)
    else:
        return acquire_tokens_result


def create_error_message():
    keys = scope_dict.keys()
    error_message = f'Mode must be one of the following. <{" ".join(keys)}>'

    return error_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: 'python get_token.py <mode>'")
        exit(1)

    acquire_tokens_result = acquire_token(mode=sys.argv[1])

    print(f'Access token:\n{acquire_tokens_result["access_token"]}')
    print(f'\nRefresh token:\n{acquire_tokens_result["refresh_token"]}')
