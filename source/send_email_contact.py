from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from utility.settings import RECEIVER_EMAIL, RECEIVER_PASSWORD, EMAIL_SERVER, EMAIL_PORT, EMAIL_STARTTLS, EMAIL_SSL_TLS, USE_CREDENTIALS, VALIDATE_CERTS
from utility.logger import Logger

logger = Logger(__name__)


class SendContactEmail:

    def __init__(self, sender_name, sender_email, sender_subject, sender_content):
        self._sender_name = sender_name
        self._sender_email = sender_email
        self._sender_subject = sender_subject
        self._sender_content = sender_content
        self._receiver_email = RECEIVER_EMAIL
        self._receiver_password = RECEIVER_PASSWORD
        self._email_server = EMAIL_SERVER
        self._email_port = EMAIL_PORT
        self._email_tls = EMAIL_STARTTLS
        self._email_ssl = EMAIL_SSL_TLS
        self._use_credentials = USE_CREDENTIALS
        self._validate_certs = VALIDATE_CERTS

    async def _send_contact_email(self):
        email_conf = ConnectionConfig(
            MAIL_USERNAME=self._receiver_email,
            MAIL_PASSWORD=self._receiver_password,
            MAIL_FROM=self._sender_email,
            MAIL_FROM_NAME=self._sender_name,
            MAIL_PORT=self._email_port,
            MAIL_SERVER=self._email_server,
            MAIL_STARTTLS=self._email_tls,
            MAIL_SSL_TLS=self._email_ssl,
            USE_CREDENTIALS=self._use_credentials,
            VALIDATE_CERTS=self._validate_certs
        )

        email_message = MessageSchema(
            subject=self._sender_subject,
            recipients=[self._receiver_email],
            body=self._sender_content,
            subtype="plain"
        )
        fast_mail = FastMail(email_conf)
        await fast_mail.send_message(email_message)

    async def send_email(self):
        await self._send_contact_email()

