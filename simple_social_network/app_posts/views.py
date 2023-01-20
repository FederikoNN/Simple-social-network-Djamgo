# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse
from .forms import PostCommentForm, PhotoPostForm
from .models import PhotoPost, Comment, LikePhoto, LikeComment, Subscribe


class PostCreationFormView(LoginRequiredMixin, CreateView):
    model = PhotoPost
    form_class = PhotoPostForm
    template_name = 'posts/post_creation_page.html'
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect(reverse('main'))


class PostsListView(ListView):
    model = PhotoPost
    ordering = ['-date_create']
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts_list'


class PostsListViewTop10(ListView):
    model = PhotoPost
    queryset = PhotoPost.objects.order_by('-likes')[:10]
    template_name = 'posts/top10.html'
    context_object_name = 'posts_list'


class PostListViewSubscribe(ListView):
    model = PhotoPost
    template_name = 'posts/subscribe.html'
    context_object_name = 'posts_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            users_follow = User.objects.get(
                id=self.request.user.id).followers.all()
            context['subscribes'] = users_follow
            context['posts_follow'] = PhotoPost.objects.filter(
                user_id__in=users_follow.values('user_following_id')).order_by(
                '-date_create').all()
        return context


class PostSinglePageView(DetailView):
    model = PhotoPost
    template_name = 'posts/post_single_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        context['comments'] = self.object.post.all()
        context['comment_form'] = PostCommentForm
        if self.request.user.is_authenticated:
            users_follow = User.objects.get(
                id=self.request.user.id).followers.all()
            context['subscribes'] = users_follow
        return context

    # @login_required
    def post(self, request, **kwargs):
        post_object = self.get_object()
        comment_form = PostCommentForm(request.POST)
        if comment_form.is_valid():
            post_object.activity += 1
            new_comment = comment_form.save(commit=False)
            new_comment.post_comment = post_object
            new_comment.user = request.user
            new_comment.save()
        if 'like_photo' in request.POST:
            like, created = LikePhoto.objects.get_or_create(user=request.user,
                                                            photo_id=post_object.id)
            if created:
                post_object.likes += 1
        if 'like_comment' in request.POST:
            comment_id = request.POST.get('like_comment')
            like, created = LikeComment.objects.get_or_create(user=request.user,
                                                              comment_id=comment_id)
            if created:
                comment = Comment.objects.get(id=comment_id)
                comment.likes += 1
                comment.save()
        if 'subscribe' in request.POST:
            Subscribe.objects.get_or_create(user_follower_id=request.user.id,
                                            user_following_id=post_object.user.id)
        post_object.save()
        return redirect(reverse('comments', kwargs={'pk': post_object.id}))
