from django.core.mail import send_mail



def send_mail_without_celery():
    send_mail(
        'CELERY WORKED YEAH',"CELERY IS COOL",
        "teja842223@gmail.com",
        ['teja84222@gmail.com'],
        fail_silently=False
        )
    return None