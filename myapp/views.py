# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Submission
import datetime
from django.http import HttpResponseRedirect

def submission(request):
    x= Submission.objects.all()
    submission_list = []
    for abc in x:
        submission_list.append({
            "id": abc.id,
            "votes": abc.votes,
            "name": abc.name
        })
    if request.method == "POST":
        id_list = request.POST.getlist('submission_id')
        for id in id_list:
            tools = Submission.objects.filter(id = id)[0]
            tools_votes = tools.votes
            tools.votes = tools_votes + 1
            tools.save()
        return render(request, 'myapp/template/feedback_page.html', {"submissions_by_vote_count":submission_list, "display": "block"})
    return render(request, 'myapp/template/feedback_page.html', {"submissions_by_vote_count":submission_list, "display": "none"})