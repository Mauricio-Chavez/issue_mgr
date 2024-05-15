from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Issue, Status


class IssueCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Issue
    template_name = "issues/new.html"
    fields = ["name", "summary", "description", "assignee", "status"]
    success_url = reverse_lazy('board')
    def test_func(self):
        return str(self.request.user.role) == 'product owner'

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class BoardView(LoginRequiredMixin,ListView):
    template_name = 'issues/board.html'
    model = Issue

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name='to do')
        in_prog = Status.objects.get(name='in progress')
        done = Status.objects.get(name='done')
        team = self.request.user.team
        context['to_do_list'] = Issue.objects.filter(
            status=to_do,
            assignee__team=team
            ).order_by('created_on').reverse()
        context['in_prog_list'] = Issue.objects.filter(
            status=in_prog,
            assignee__team=team
            ).order_by('created_on').reverse()
        context['done_list'] = Issue.objects.filter(
            status=done,
            assignee__team=team
            ).order_by('created_on').reverse()
        return context

class StatusUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = 'issues/status_update.html'
    model = Issue
    fields = ['status']
    success_url = reverse_lazy('board')
    def test_func(self):
        if self.get_object().status.name == 'done':
            return str(self.request.user.role) == 'scrum master'
        
        return True


