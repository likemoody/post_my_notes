import datetime

from django.db.models.query_utils import Q

from posts_app.models import Message


def version_date(request):
    ctx = {
        'project_version': 'alpha 0.1',
        'current_date'   : datetime.datetime.now(),
    }
    return ctx


def unread_messages(request):
    private_messages = Message.objects.filter(
        Q(user_to=request.user.id) |
        Q(user_from=request.user.id))
    unread_pm = len(private_messages.filter(
        is_read=False,
        user_to=request.user.id))
    ctx = {
        'unread_messages': unread_pm,
    }
    return ctx
