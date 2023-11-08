import streamlit as st
import json
import tools


tab1, tab2 = st.tabs(['Login', 'Register'])

pass_requirements = '''
        At least one capital letter\n
        At least one number\n
        At least one special character\n
        Characters allowed: !@#$&*\n
        Between 8 and 20 characters
        '''

with tab1:
    with st.form("login_form"):
        user_login = st.text_input('Username')
        user_psswd = st.text_input('Password', type='password')
        submit = st.form_submit_button('Sign in', use_container_width=True)
        if submit:
            response = tools.login(login=user_login, psswd=user_psswd)
            if response == 1:
                st.text('ENTROU')
            else:
                st.text('NAO ENTROU')
with tab2:
    with st.form("sign_up"):
        st.text_input('E-mail', max_chars=40, key='get_email')
        name = st.text_input('Username', type='default', 
            max_chars=20, help="Use . instead of spaces", key='get_user')
        psswd = st.text_input('Password', type='password', 
            help='' ,key='get_psswd')
        psswd_confirm = st.text_input('Confirm your password', type='password',
                                        key='get_confirm_psswd')
        pass_expander = st.expander('Password requirements:')
        pass_expander.write(pass_requirements)
        submit = st.form_submit_button('Sign up', use_container_width=True)

st.session_state