from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentForm

# Класс ListView для списка постов
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Указываем шаблон
    context_object_name = 'posts'  # Имя переменной, которая будет передана в шаблон
    paginate_by = 5  # Количество постов на одной странице

    def get_queryset(self):
        # Мы просто возвращаем все посты
        return Post.objects.all().order_by('-created_at')  # Сортировка по дате публикации (от новых к старым)


# Класс DetailView для детальной страницы поста
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Указываем шаблон
    context_object_name = 'post'  # Имя переменной, которая будет передана в шаблон

    def get_object(self, queryset=None):
        # Получаем объект по slug
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def post(self, request, *args, **kwargs):
        # Обработка комментариев
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
        return render(request, self.template_name, {
            'post': post,
            'form': form
        })