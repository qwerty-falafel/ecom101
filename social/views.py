from django.shortcuts import render, redirect
from actstream import action
from .forms import UserPostForm
from .models import UserProfilePost
from actstream.models import user_stream

def all_posts(request):
    posts = UserProfilePost.objects.all().order_by('-created_at')  # Ordering by most recent
    return render(request, 'social/all_posts.html', {'posts': posts})

def news_feed(request):
    if request.method == "POST":
        form = UserPostForm(request.POST)
        if form.is_valid():
            # Save the new post
            post = form.save(commit=False)
            post.user = request.user  # Make sure to use the correct field name
            post.save()

            # Log the action with django-activity-stream
            action.send(request.user, verb='posted', action_object=post)

            # Redirect to clean the form or avoid form resubmission
            return redirect('news_feed') 
    else:
        form = UserPostForm()

    activities = UserProfilePost.objects.all().order_by('created_at')
    print(activities) 
    return render(request, 'social/feed.html', {'activities': activities, 'form': form})
