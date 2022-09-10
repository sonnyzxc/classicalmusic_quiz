from xml.dom.minidom import CharacterData
from django.db import models
from django.utils.translation import gettext as _

class Question(models.Model):
    LEVEL = (
        (0, _('Any')),
        (1, _('Easy')),
        (2, _('Medium')),
        (3, _('Hard')), 
    )

    title = models.CharField(_("title"), max_length=255)
    points = models.SmallIntegerField(_("points"), default=0)
    difficulty = models.IntegerField(_("difficulty"), choices=LEVEL, default=0)
    is_active = models.BooleanField(_("is active"), default=True)
    created_at = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("updated"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', verbose_name=_("Question"), on_delete=models.CASCADE)
    answer = models.CharField(_("answer"), max_length=255)
    is_correct = models.BooleanField(_("correct answer"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    created_at = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("updated"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.answer