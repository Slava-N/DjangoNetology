from django.contrib import admin

from .models import Article, Topics, TopicsLogs

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_topic=0
        # try:
        #     count_main_topics = lambda x: int(x.get('primary_topic', 0))
        #     print(list(self.forms))
        #
        #     main_topic = sum(map(count_main_topics, self.forms))
        # except:
        #     pass
        # main_topic = lambda x: sum([y['primary_topic'] for y.cleaned_data in self.forms])
        # print(main_topic)
        for form in self.forms:
            main_topic += int(form.cleaned_data.get('primary_topic', 0))

            # if form.cleaned_data['primary_topic']
            # print(form.cleaned_data)
        if main_topic != 1:
            raise ValidationError('Должен быть выделен ОДИН главный раздел')

            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = TopicsLogs
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

    pass

@admin.register(Topics)
class TopicsAdmin(admin.ModelAdmin):
    pass



