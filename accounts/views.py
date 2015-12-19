from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.utils import timezone
from forms import MyRegistrationForm
from userprofile.forms import StatusForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.models import UserProfile, Status, Friendship, Poke
from django.db.models import Q
from itertools import chain
from userprofile.views import user_profile


def register_user(request):

    if request.user.is_authenticated():
        return redirect(profile)
    else:
        if request.method == 'POST':
            form = MyRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/register_success')


        args = {}
        args.update(csrf(request))
        args['form'] = MyRegistrationForm()

        return render_to_response('landing.html', args)



def login(request):

    c = {}
    c.update(csrf(request))
    return render_to_response('landing.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return redirect(register_user)

def invalid_login(request):
    return render_to_response('invalid.html')

def loggedin(request):
    return redirect(profile)


def logout(request):
    auth.logout(request)
    return redirect(register_user)

def register_success(request):
    return render_to_response('registersuccess.html')







@login_required
def profile(request, id=None):

    if request.method == "POST":

        form = StatusForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            print post.author
            post.save()
            return redirect(profile)

    else:

        form = StatusForm()


    if id: #if navigating to another page

        username = User.objects.get(pk=id)

        if username == request.user:

            me = True
        else:

            me = False


        switch = True

        posts = Status.objects.filter(author_id=id).order_by('-created_date')

        a = Friendship.objects.filter(Q(creator=username) | Q(friend=username))

        creator = request.user
        friend = User.objects.get(pk=id)

        if Friendship.objects.filter(creator=creator, friend=friend) or Friendship.objects.filter(creator=friend, friend=creator):

            thefriends = True

            return render(request, 'profile.html', {'var': username, 'switch': switch, 'form': form, 'posts': posts, 'thereisfriend': thefriends, 'thefriends': a, 'me': me })

        else:

            thefriends = False
            return render(request, 'profile.html', {'var': username, 'switch': switch, 'form': form, 'posts': posts, 'thereisfriend': thefriends, 'thefriends': a, 'me': me })




    else: #if naviagting to your own profile



        posts = Status.objects.filter(author_id=request.user).order_by('-created_date')

        this = request.user

        a = Friendship.objects.filter(Q(creator=request.user) | Q(friend=request.user))

        return render(request, 'profile.html', {'friendlist': a, 'var': this, 'form': form, 'posts': posts, 'thefriends': a})



def createfriendship(request, id):

    #the creator is the user
    #the friend is the id

    creator = request.user
    friend = User.objects.get(pk=id)

    if Friendship.objects.filter(creator=creator, friend=friend):

        return redirect(profile)

    else:

        a = Friendship.objects.create(creator=creator, friend=friend)
        a.save()

        return redirect(profile)












def like(request, id2):

    usercheck = request.user
    likes = Status.objects.get(id=id2)

    if usercheck != likes.author:


        likes.likes += 1
        likes.save()

        return redirect(profile, id=likes.author_id)
    else:

        return redirect(profile, id=likes.author_id)


def dislike(request, id2):

    usercheck = request.user
    likes = Status.objects.get(id=id2)


    if usercheck != likes.author:

        if likes.likes < -3:

            likes.delete()

        else:

            likes.likes -= 1
            likes.save()

        return redirect(profile, id=likes.author_id)

    else:

        return redirect(profile, id=likes.author_id)





def search_titles(request):
    if request.method == "POST":

        search_text = request.POST['search_text']

    else:

        search_text = ''
    #the exlcude method makes sure the user is not in the search
    results = User.objects.filter(first_name__contains=search_text).exclude(username=request.user)



    return render_to_response('ajax_search.html', {'results' : results})



def newsfeed(request):


    if request.method == "POST":

        form = StatusForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            print post.author
            post.save()
            return redirect(newsfeed)

    else:

        form = StatusForm()


    a = Poke.objects.filter(receiver=request.user)


    posts = Status.objects.order_by('-created_date')

    #isfriend = Friendship.objects.filter(Q(creator=request.user) | Q(friend=request.user))


    #request.user.freinds.post.all()

    return render(request, 'newsfeed.html', {'form': form, 'posts': posts, 'pokes': a})


def createpoke(request, id):

    initiator = request.user
    receiver = User.objects.get(pk=id)

    if Poke.objects.filter(Q(initiator=initiator, receiver=receiver) | Q(initiator=receiver, receiver=initiator)):

        a = Poke.objects.filter(Q(initiator=initiator, receiver=receiver) | Q(initiator=receiver, receiver=initiator))

        a.delete()

        b = Poke.objects.create(initiator=initiator, receiver=receiver)
        b.save()

        return redirect(profile)

    else:

        a = Poke.objects.create(initiator=initiator, receiver=receiver)
        a.save()

        return redirect(profile)
















