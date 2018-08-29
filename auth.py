import sys
import json
import spotipy.util as util
import spotipy.oauth2 as oauth2

class spotify_auth:
    def __init__(self, username, scope, client_id, client_secret, redirect_uri=None, user_token=None):
        self.username = username
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = "http://localhost/"
        if redirect_uri:
            self.redirect_uri = redirect_uri

        self.update_user_token()

    def get_username(self):
        return self.username

    def get_scope(self):
        return self.scope

    def get_client_id(self):
        return self.client_id

    def get_client_secret(self):
        return self.client_secret

    def get_redirect_uri(self):
        return redirect_uri

    def get_user_token(self):
        return self.user_token

    def add_scope(self, permission):
        self.scope += " {}".format(permission)

    def update_user_token(self):
        self.user_token = util.prompt_for_user_token(self.username,
                                                     self.scope,
                                                     client_id=self.client_id,
                                                     client_secret=self.client_secret,
                                                     redirect_uri=self.redirect_uri)

        print("New token registered:\t{}...".format(self.user_token[:47]))
        
        self.output_data()

        return self.user_token

    def output_data(self):
        data = {"username": self.username,
                "scope": self.scope,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_uri": self.redirect_uri }

        with open("auth.json", "w") as file:
            json.dump(data, file)
