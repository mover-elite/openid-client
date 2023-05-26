provider = "my-provider"

credentials = {
    "google": {
        "base_url": "https://accounts.google.com",
        "id": "Google Client ID",
        "secret": "client secret",
    },
    "auth0": {
        "base_url": "autho provider url",  # this is always different for different application
        "id": "client id",
        "secret": "client secret",
    },
    "my-provider": {
        "base_url": "https://identity-provider.up.railway.app",  # this is always different for different application
        "id": "KgwZin4eDNrWv4miaVxrGn",
        "secret": "4fUYvcZbEpNYCNkR96ypEZ",
    },
}


odic_provider = credentials[provider]["base_url"]
client_id = credentials[provider]["id"]
client_secret = credentials[provider]["secret"]
redirect_uri = "http://127.0.0.1:5001/callback"
