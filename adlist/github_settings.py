# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App - GIve it a name

# If you are running on localhost, make the callback url be
# http://127.0.0.1:8000/oauth/complete/github/

# If you are on the real internet (or using ngrok) make the callback url be
# https://samples.dj4e.com/oauth/complete/github/

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = '44b6692fc8966b150f7f'
SOCIAL_AUTH_GITHUB_SECRET = 'e3f4d481c371e679f82afe71dba492c3a33a49ef'
#okay oath is not working. 