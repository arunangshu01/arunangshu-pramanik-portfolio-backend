from fastapi import Depends, BackgroundTasks, APIRouter, HTTPException, status
from source.send_email_contact import SendContactEmail
from model.base_models_send_contact_email import ContactForm
from model.base_models_send_contact_email import SendMessageSuccess
from model.base_models_errors import ErrorResponseModel
from utility.logger import Logger

logger = Logger(__name__)

router = APIRouter(tags=["Drop Me A Message"])


@router.post('/send_email', status_code=status.HTTP_201_CREATED)
async def send_email(background_tasks: BackgroundTasks, contact_form: ContactForm = Depends(ContactForm.as_form)):
    try:
        send_contact_email = SendContactEmail(
            sender_name=contact_form.name,
            sender_email=contact_form.email,
            sender_content=contact_form.message
        )
        background_tasks.add_task(send_contact_email.send_email)
        success_message = f"Your message has been sent successfully."
        logger.info(success_message)
        email_success = SendMessageSuccess(
            message=success_message
        )
        return email_success.model_dump()
    except Exception as e:
        error_message = f"Error: There was an error sending your message. Please try again later."
        logger.error(error_message)
        error_detail = ErrorResponseModel(
            error_message=error_message,
            error_type=type(e).__name__
        )
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_detail.model_dump())


