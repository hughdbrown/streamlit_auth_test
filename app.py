#!/usr/bin/env python3
import streamlit as st
import streamlit_authenticator as stauth

COOKIE_NAME = "application_cookie_name"
SIGNATURE_KEY = "honestly, I don't know what this does"
COOKIE_EXPIRY_DAYS = 30

CREDENTIALS = {
    'usernames': {
        "admin1": {
            "email": "admin@example.com",
            "password": "abc",
            "name": "Mark Zuckerberg",
        },
        "maint1": {
            "email": "maint1@example.com",
            "password": "def",
            "name": "Bill Gates",
        },
        "maint2": {
            "email": "maint2@example.com",
            "password": "ghi",
            "name": "Elon Musk",
        },
        "maint3": {
            "email": "maint3@example.com",
            "password": "jkl",
            "name": "Jeff Bezos",
        },
    }
}

def main():
    for d in CREDENTIALS["usernames"].values():
        d["password"] = stauth.Hasher([d["password"]]).generate()[0]

    authenticator = stauth.Authenticate(
        CREDENTIALS,
        COOKIE_NAME,
        SIGNATURE_KEY,
        COOKIE_EXPIRY_DAYS,
        {"emails": []},
    )
    name, status, username = authenticator.login('Login', 'main')

    if status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.title('Some content')
    elif status is False:
        st.error('Username/password is incorrect')
    elif status is None:
        st.warning('Please enter your username and password')

if __name__ == '__main__':
    main()

