from django.core.mail import EmailMessage

from django.conf import settings


def send_login_details_to_email(username, password, user_email,
                                from_email=settings.DEFAILT_SEND_EMAIL, title='Your login details'):
    body_email = f"""
        Username: {username}
        Password: {password}
    """

    email = EmailMessage(title, body_email, from_email, to=[user_email])
    email.send()
