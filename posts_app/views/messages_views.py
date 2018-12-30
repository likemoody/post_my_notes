import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View

from ..forms import SendMessageForm, SendMessageToForm
from ..models import Message


class MessagesView(LoginRequiredMixin, View):
    def get(self, request):
        private_messages = Message.objects.filter(
            Q(user_to=request.user.id) |
            Q(user_from=request.user.id)).order_by('-date_sent')
        send_message_form = SendMessageForm(initial={'user_from': request.user})

        # note exclude current user from queryset
        send_message_form.fields["user_to"].queryset = User.objects.exclude(pk=request.user.id)

        return render(request, 'posts_app/messages.html', locals())

    def post(self, request):
        send_message_form = SendMessageForm(request.POST)
        if send_message_form.is_valid():
            user_from = User.objects.get(pk=request.user.id)
            user_to = send_message_form.cleaned_data.get('user_to')
            content = send_message_form.cleaned_data.get('content')
            sent_message = Message(user_from=user_from, user_to=user_to, content=content)
            sent_message.save()
            messages.success(request, 'Message has been sent.')
        return redirect('messages')


class SingleMessageView(LoginRequiredMixin, View):
    def get(self, request, message_id):
        private_message = Message.objects.get(pk=message_id)
        if request.user.id == private_message.user_to.id:
            private_message.is_read = True
            private_message.date_read = datetime.datetime.now()
            private_message.save()
        return render(request, 'posts_app/message_single.html', locals())


class SendMessageView(LoginRequiredMixin, View):
    def get(self, request):
        send_message_form = SendMessageForm(initial={'user_from': request.user})
        return render(request, 'posts_app/send_pm.html', locals())

    def post(self, request):
        send_message_form = SendMessageForm(request.POST)
        if send_message_form.is_valid():
            user_from = User.objects.get(pk=request.user.id)
            user_to = send_message_form.cleaned_data.get('user_to')
            content = send_message_form.cleaned_data.get('content')
            sent_message = Message(user_from=user_from, user_to=user_to, content=content)
            sent_message.save()
            messages.success(request, 'Message has been sent.')
        return redirect('messages')


class SendMessageToView(LoginRequiredMixin, View):
    def get(self, request, uid):
        user_to = User.objects.get(pk=uid)
        send_message_to_form = SendMessageToForm()
        return render(request, 'posts_app/send_pm_to.html', locals())

    def post(self, request, uid):
        send_message_to_form = SendMessageToForm(request.POST)
        if send_message_to_form.is_valid():
            user_from = User.objects.get(pk=request.user.id)
            user_to = User.objects.get(pk=uid)
            content = send_message_to_form.cleaned_data.get('content')
            sent_message = Message(user_from=user_from, user_to=user_to, content=content)
            sent_message.save()
            messages.success(request, 'Message has been sent.')
        return redirect('messages')
