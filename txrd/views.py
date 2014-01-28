# Create your views here.

import datetime
from django.http import *
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from models import MemberProfile, MembershipPoint

def login_member(request):
    logout(request)
    username = password = ''
    if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/portal/')
    return render_to_response('login_form.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def portal(request):
    profile = MemberProfile.objects.get(user_id=request.user.id)
    points = MembershipPoint.objects.filter(member=profile.id)
    profile_points = profile.points_for_date()
    dict = {
        'member_profile': profile,
        'current_date': datetime.datetime.now(),
        'points': points,
        'profile_points': profile_points,
    }
    return render_to_response('portal.html', dict, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def portal_points(request):
    return render_to_response('portal_points.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def logout_member(request):
    logout(request)
    return render_to_response('login_form.html', context_instance=RequestContext(request))

