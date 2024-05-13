from django.shortcuts import render
from .models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# class IssueListView(ListView):
#     model = Issue
#     template_name = "issues/issue_list.html"

# class IssueDetailView(DetailView):
#     model = Issue
#     template_name = "issues/issue_detail.html"

class IssueCreateView(CreateView):
    model = Issue
    template_name = "issues/board.html"
    fields = ["name", "summary", "description", "reporter", "assignee", "is_done"]

# class IssueUpdateView(UpdateView):
#     model = Issue
#     template_name = "issues/issue_form.html"
#     fields = ["name", "summary", "description", "reporter", "assignee", "is_done"]

# class IssueDeleteView(DeleteView):
#     model = Issue
#     template_name = "issues/issue_confirm_delete.html"