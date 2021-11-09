from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class TicketAdminForm(forms.ModelForm):

    incident = forms.CharField(label="Инцидент", widget=CKEditorUploadingWidget())

    class Meta:
        model = Ticket
        fields = '__all__'


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'incident', 'answer', 'dateOfIncident', 'is_done')
    list_editable = ('is_done',)
    list_display_links = ('name', 'incident', 'answer')
    form = TicketAdminForm


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('solutionOfProblem', 'dateOfAnswer')
    list_display_links = ('solutionOfProblem',)