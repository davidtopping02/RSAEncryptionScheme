# -----------------------------------------------------------
# Holds the user class for an asymetric encryption scheme
#
# (C) David Topping
# https://github.com/davidtopping02/ELGamalEncryption
# -----------------------------------------------------------

from Crypto.Util import number


class User:

    def __init__(self, name) -> None:
        self.name = name
        self.user_ID = 0
        self.public_key = ""
        self.private_key = ""

    def generate_private_key(self):

        pass

    def generate_public_key(self):
        pass
