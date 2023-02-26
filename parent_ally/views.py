from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from .models import Post, Profile, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def index(request):
    """The home page"""
    return render(request, 'parent_ally/index.html')


def view_posts_list(request):
    """Lists all available posts with the option for authenticated users to create a new post"""
    # If form submitted
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Add the form to the database
            posting = form.save(commit=False)
            posting.create_date = timezone.now()
            posting.like_count = 0
            profile = Profile.objects.get(user=request.user)
            posting.author = profile
            posting.save()

            return redirect('/')
    # GET request
    else:
        # Generate the context dictionary for the template
        form = PostForm()
        # Five most recent posts
        postings_list = Post.objects.order_by('-create_date')[:5]
        context = {'form': form, 'postings_list': postings_list}

    return render(request, 'parent_ally/dummy_list.html', context)


class ListViewNoImages(generic.ListView):
    """Lists all available posts in a template without showing image thumbnails"""
    template_name = 'parent_ally/dummy_list.html'
    context_object_name = 'postings_list'


def view_post(request, pk):
    """Provides a detailed view of a post with the comments section. One issue with this code is that both forms return similar arguments, and so it's hard to check which one I actually submitted. My hack solution is to check the most restrictive ones first.
    """

    post = get_object_or_404(Post, pk=pk)

    # If form submitted
    if request.method == 'POST':
        # See if the author edited the post
        form2 = PostForm(request.POST, instance=post)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.save()

            # GET request
            return redirect(f'/detail/{pk}/')

        # See if the user added a comment
        form = CommentForm(request.POST)
        if form.is_valid():
            # Add the comment to the database
            comment = form.save(commit=False)
            author = Profile.objects.get(user=request.user)
            comment.author = author
            comment.post = post
            comment.save()

            # GET request
            return redirect(f'/detail/{pk}/')

    # GET request (i.e. form not submitted)
    else:
        # Create the context dictionary for the template
        form = CommentForm()
        form2 = PostForm()
        context = {'form': form, 'form2': form2, 'post': post}

    return render(request, 'parent_ally/dummy_detail.html', context)


def edit_comment(request, pk):
  """
  Edit a comment if it exists. Only the commenter can do this. 
  Throw a 404 error if the comment does not exist. Redirect the 
  user to the post the comment responds to if successful.
  """
  comment = get_object_or_404(Comment, pk=pk)
  form = CommentForm(request.POST, instance=comment)
  if form.is_valid() and request.user == comment.author.user:
      comment = form.save()

  page_pk = comment.post.pk
  return redirect(f'/detail/{page_pk}')
  

@login_required(login_url='common:login')
def delete_post(request, pk):
    """Delete a post if the user is it exists and the user is the author"""
    posting = get_object_or_404(Post, pk=pk)
    if request.user == posting.author.user:
        posting.delete()

    return redirect('/')


def delete_comment(request, pk):
    """Delete a specified comment. Allowed if the user is the owner of the post the comment belongs to, or if the user is the commenter."""
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author.user or request.user == comment.post.author.user:
        post = comment.post
        comment.delete()

    return redirect(f'/detail/{post.pk}')


@login_required(login_url='common:login')
def create_post(request):
    """A page containing a form to submit a new post"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.create_date = timezone.now()
            posting.like_count = 0
            profile = Profile.objects.get(user=request.user)
            posting.author = profile
            posting.save()
            return redirect('/')
    else:
        # Generate the context dictionary for the template
        form = PostForm()
        context = {'form': form}

    return render(request, 'parent_ally/posting_form.html', context)
