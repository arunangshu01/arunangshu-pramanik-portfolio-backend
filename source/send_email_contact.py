from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from utility.settings import RECEIVER_EMAIL, RECEIVER_PASSWORD, EMAIL_SERVER, EMAIL_PORT, EMAIL_STARTTLS, EMAIL_SSL_TLS, USE_CREDENTIALS, VALIDATE_CERTS
from utility.logger import Logger

logger = Logger(__name__)

email_tls = True if EMAIL_STARTTLS == "True" else False
email_ssl = True if EMAIL_SSL_TLS == "True" else False
use_credentials = True if USE_CREDENTIALS == "True" else False
validate_certs = True if VALIDATE_CERTS == "True" else False


class SendContactEmail:

    def __init__(self, sender_name, sender_email, sender_content):
        self._sender_name = sender_name
        self._sender_email = sender_email
        self._sender_content = sender_content
        self._sender_subject = f"New Message from {self._sender_name}"
        self._receiver_email = RECEIVER_EMAIL
        self._receiver_password = RECEIVER_PASSWORD
        self._email_server = EMAIL_SERVER
        self._email_port = EMAIL_PORT
        self._email_tls = email_tls
        self._email_ssl = email_ssl
        self._use_credentials = use_credentials
        self._validate_certs = validate_certs

    async def _send_contact_email(self):
        email_conf = ConnectionConfig(
            MAIL_USERNAME=self._receiver_email,
            MAIL_PASSWORD=self._receiver_password,
            MAIL_FROM=self._receiver_email,
            MAIL_FROM_NAME=f"{self._sender_name} via Portfolio",
            MAIL_PORT=self._email_port,
            MAIL_SERVER=self._email_server,
            MAIL_STARTTLS=self._email_tls,
            MAIL_SSL_TLS=self._email_ssl,
            USE_CREDENTIALS=self._use_credentials,
            VALIDATE_CERTS=self._validate_certs
        )
        email_body = f"""
        
        Name: {self._sender_name}
        Email: {self._sender_email}
        
        Message: {self._sender_content}
        """

        email_message = MessageSchema(
            subject=self._sender_subject,
            recipients=[self._receiver_email],
            reply_to=[self._sender_email],
            body=email_body,
            subtype="plain"
        )
        fast_mail = FastMail(email_conf)
        await fast_mail.send_message(email_message)

    async def send_email(self):
        await self._send_contact_email()
