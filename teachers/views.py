import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from . import models


@login_required
def teacher_list(request):
    teachers = models.Teacher.objects.all()
    return render(
        request=request,
        template_name='teachers/teacher_list.html',
        context={
            "teachers": teachers
        }
    )


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = models.Teacher
    template_name = "teachers/teacher_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TeacherCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Teacher
    fields = '__all__'
    success_message = "New teacher successfully added."

    def get_form(self):
        form = super().get_form()
        form.fields['subject_taught'].widget = widgets.Textarea(
            attrs={
                'rows': 2
            }
        )
        return form


class TeacherUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = models.Teacher
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        form = super().get_form()
        form.fields['subject_taught'].widget = widgets.Textarea(
            attrs={
                'rows': 2
            }
        )
        return form


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Teacher
    success_url = reverse_lazy('teacher-list')


class TeacherBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.TeacherBulkUpload
    template_name = 'teachers/teachers_upload.html'
    fields = ['csv_file']
    success_url = '/teacher/list'
    success_message = 'Successfully uploaded teachers'


@login_required
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="teachers_record_template.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'First Name',
        'Last Name',
        'Profile picture',
        'Email Address',
        'Phone Number',
        'Room Number',
        'Subjects taught',
    ])

    return response
