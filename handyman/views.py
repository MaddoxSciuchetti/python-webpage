from django.shortcuts import render,  redirect
from .models import Topic, Entry


def index(request):
    return render(request, 'handyman/index.html')

def topics(request):
    topics = Topic.objects.order_by("date_added")
    context = {'topics':topics}
    return render (request, 'handyman/topics.html',context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'handyman/topic.html', context)


