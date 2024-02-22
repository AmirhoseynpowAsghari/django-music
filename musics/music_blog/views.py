from django.views.generic.edit import FormView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from .forms import MusicForm
from .models import Music
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.db.models import Count




class AddMusicView(FormView):
    template_name = 'music_blog/add_music.html'
    form_class = MusicForm
    success_url = reverse_lazy('add_music')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submitted'] = self.request.GET.get('submitted') == 'True'
        return context


class MusicListView(ListView):
    model = Music
    template_name = 'music_blog/musics_list.html'
    context_object_name = 'musics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the count of all music objects
        context['music_count'] = self.model.objects.count()

        # Get the count of music objects in each category
        categories = Music.objects.values('category').annotate(count=Count('category'))
        context['category_counts'] = categories
        return context
    
class MusicInfoView(TemplateView):
    template_name = 'music_blog/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the count of all music objects
        context['music_count'] = Music.objects.count()

        # Get the count of music objects in each category
        category_counts = Music.objects.values('category').annotate(count=Count('category'))
        context['category_counts'] = category_counts

        # Count the number of distinct categories
        context['num_categories'] = len(category_counts)
        return context


class DeleteMusicView(DeleteView):
    model = Music
    success_url = reverse_lazy('music_list')
    template_name = 'music_blog/delete_music.html'

    def get_object(self, queryset=None):
        # Try to get the Music object by ID
        try:
            music = super().get_object(queryset)
        except (ValueError, Music.DoesNotExist):
            # If the provided pk is not a valid ID or Music object not found by ID,
            # try to get the Music object by name
            music_name = self.kwargs.get('pk')
            music = get_object_or_404(Music, name=music_name)
        return music

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Instead of deleting the music object, mark it as removed
        self.object.removed_for_representation = True
        self.object.save()
        return self.render_to_response(self.get_context_data())