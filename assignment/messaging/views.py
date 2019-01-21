from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .forms import MailForm
from django.utils import timezone


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            inmails = get_list_or_404(InMessage, user_id=request.user.id)
            mails = list(map(lambda d: get_object_or_404(CustomMessage, id=d.mail_id), inmails))
            return HttpResponse(mails)
        else:
            return HttpResponse("hi")
    else:
        return HttpResponse("invalid request")


def outMessageDetails(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            outmails = get_list_or_404(OutMessage, user_id=request.user.id)
            mails = list(map(lambda d: get_object_or_404(CustomMessage, id=d.mail_id), outmails))
            return HttpResponse(mails)
        else:
            return HttpResponse("hi")
    else:
        return HttpResponse("invalid request")


def mail_new(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            mail = form.save(commit=False)
            mail.message_from = request.user.email
            mail.pub_date = timezone.now()
            mail.save()
            tolist = mail.message_to.split(',')
            l2 = list(map(lambda l: l.strip(), tolist))
            for i in range(0, len(l2)):
                toUser = get_object_or_404(User, email=l2[i])
                inmessage = InMessage(mail_id=mail.id, user_id=toUser.id)
                inmessage.save()
            outmessage = OutMessage(mail_id=mail.id, user_id=request.user.id)
            outmessage.save()
            return redirect('home')
    else:
        form = MailForm()
    return render(request, 'mail_edit.html', {'form': form})
