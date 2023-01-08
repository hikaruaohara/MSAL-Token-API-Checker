# MSAL-Token-API-Checker
This program is for testing AccessToken acquisition and API calls using MSAL.

## Prepare

### Azure AD settings

Create an Web application in Azure AD, and set `http://localhost:3000` as the redirect URI.

### Python settings

Install MSAL for Python library.

```shell
$ pip install msal
```

Replace the client id and tenant id in get_token.py with yours.

```python
CLIENT_ID = 'YOUR CLIENT ID'
TENANT_ID = 'YOUR TENANT ID'
```

## How to use get_token.py
This program obtains and displays an access token and a refresh token.

Specify the scope you defined in get_token.py as an argument.

```shell
# If you want an access token for the Graph API
$ python get_token.py graph
```

When executed, you will be asked to authenticate on your browser.

Once authentication is complete, the access token and refresh token obtained will be displayed on the terminal.

## How to use get_token_and_call_api.py
Same usages as get_token.py.

```shell
# If you want to call the Graph API
$ python get_token_and_call_api.py graph
```

When executed, you will be asked to authenticate on the your browser.

Once authentication is complete, the API response will be displayed on the terminal.
