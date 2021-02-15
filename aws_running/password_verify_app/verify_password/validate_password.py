import re

class password_checker():

    def __init__(self):
        self.password_checker = re.compile(password_checker.password_regex_expression())

    def password_regex_expression():
        ## Regex Explanation
        # (?=.*[a-z]) positive lookahead must to have some lowercase 
        # (?=.*[A-Z]) positive lookahead must to have some uppercase
        # (?=.*[\d]) positive lookahead must to have some digit
        # (?=.*[!@#$%^&*()-+]) positive lookahead must contain some especial character of group
        # (?!.*(.).*\1) negative lookahead must not contain any repeated character
        # [a-zA-Z\d!@#$%^&*()-+] get characters of especified set of allow characters
        # {9,} minimum of 9 characters (allowed characters)
        return r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[!@#$%^&*()-+])(?!.*(.).*\1)[a-zA-Z\d!@#$%^&*()-+]{9,}$"

    def is_valid_password(self, password):
        return self.password_checker.match(str(password)) != None
