from app.services.email_service import send_email

def send_parent_alert(email, student_name):

    message = f"""
    Your child {student_name}
    was absent today.
    """

    send_email(email, message)