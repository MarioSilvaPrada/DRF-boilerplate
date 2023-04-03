from celery import shared_task


@shared_task
def hello():
    print("Hello there!")

    from django.contrib.auth import get_user_model
