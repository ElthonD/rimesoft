import streamlit as st
import streamlit_authenticator as stauth
from dependencias import sign_up, fetch_users

st.set_page_config(page_title='RIMESOFT', page_icon='☄️', initial_sidebar_state='collapsed')


try:

    # --- USER AUTHENTICATION ---
    #users = user_db.fetch_all_users()
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    usernames = [user["key"] for user in users]
    names = [user["name"] for user in users]
    hashed_passwords = [user["password"] for user in users]

    #authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "ai27_ainsurance", "abcdef", cookie_expiry_days=30)
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "rimesoft", "abcdef")

    col4, col5, col6 = st.columns([1,1,1])

    with col5:
        name, authentication_status, username = authenticator.login("Ingresar", "main")
        
        if authentication_status == False:
            st.error("Usuario/Contraseña is incorrecta")
            
        if authentication_status == None:
            st.warning("Por favor, ingresa usuario y contraseña")

    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                # let User see app
                st.sidebar.subheader(f'Bienvenido {username}')
                Authenticator.logout('Salir', 'sidebar')

                st.subheader('This is the home page')
                st.markdown(
                    """
                    ---
                    Creado con ❤️ por Elthon Rivas
                    
                    """
                )

            elif not authentication_status:
                with info:
                    st.error('Usuario o Contraseña Incorrecta')
            else:
                with info:
                    st.warning('Por favor introduzca sus credenciales')
        else:
            with info:
                st.warning('Usuario no existe, por favor registrarse')


except:
    st.success('Actualizar Página')
