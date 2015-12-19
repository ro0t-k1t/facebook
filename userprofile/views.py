from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required


def user_profile(request):
    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')

    else:

        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)


    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render(request, 'profilesetup.html', args)

    #must use render to pass the session, render to response doesnt work


