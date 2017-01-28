from celery import Celery
from .models import Message
#app = Celery('tasks', broker='amqp://localhost')

@app.task
def add(x, y):
    msg = Message()
    msg.author = str(x)
    msg.content = str(y)
    msg.save()
    return x + y
