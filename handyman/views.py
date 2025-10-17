from django.shortcuts import render,  redirect
from django.db.utils import OperationalError
from .models import Topic, Entry


def index(request):
    return render(request, 'handyman/index.html')

def topics(request):
    try:
        topics = Topic.objects.order_by("date_added")
    except OperationalError:
        topics = []
    context = {'topics': topics}
    return render (request, 'handyman/topics.html',context)

def topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
    except OperationalError:
        topic = type('T', (), {'text': 'Topic'})()
        entries = []
    context = {'topic': topic, 'entries': entries}
    return render(request, 'handyman/topic.html', context)


