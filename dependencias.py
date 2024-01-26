import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
from dotenv import load_dotenv
import os

#Cargar las variables de entorno

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

# Inicializar con una clave de proyecto

deta = Deta(DETA_KEY)

# Esto es como crear/conectar una base de datos

db = deta.Base("dependencias")

def insert_user(email, username, password):
    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """
    date_joined = str(datetime.datetime.now())

    return db.put({'key': email, 'username': username, 'password': password, 'date_joined': date_joined})


def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """
    users = db.fetch()
    return users.items


def get_user_emails():
    """
    Fetch User Emails
    :return List of user emails:
    """
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user['key'])
    return emails


def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user['key'])
    return usernames


def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

    if re.match(pattern, email):
        return True
    return False


def validate_username(username):
    """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
    """

    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False


def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input(':blue[Correo]', placeholder='Ingresar Correo')
        username = st.text_input(':blue[Usuario]', placeholder='Ingresar Usuario')
        password1 = st.text_input(':blue[Contraseña]', placeholder='Ingresar Contraseña', type='password')
        password2 = st.text_input(':blue[Confirmar Contraseña]', placeholder='Confirmar Contraseña', type='password')

        if email:
            if validate_email(email):
                if email not in get_user_emails():
                    if validate_username(username):
                        if username not in get_usernames():
                            if len(username) >= 2:
                                if len(password1) >= 6:
                                    if password1 == password2:
                                        # Add User to DB
                                        hashed_password = stauth.Hasher([password2]).generate()
                                        insert_user(email, username, hashed_password[0])
                                        st.success('¡Cuenta Creada Satisfactoriamente!')
                                        st.balloons()
                                    else:
                                        st.warning('Contraseñas no coinciden')
                                else:
                                    st.warning('Contraseña es muy corta')
                            else:
                                st.warning('Usuario es muy corto')
                        else:
                            st.warning('¡Usuario ya existe!')

                    else:
                        st.warning('Usuario Inválido')
                else:
                    st.warning('¡Correo ya existe!')
            else:
                st.warning('Correo Inválido')

        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn3:
            st.form_submit_button('Registrarse')

# sign_uo()







