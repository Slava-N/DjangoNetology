from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.FloatField(label="Стоимость товара")
    rate = forms.DecimalField(label="Процентная ставка")
    months_count = forms.FloatField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean(self):
        # общая функция валидации
        rate = self.cleaned_data.get('rate')
        months_count = self.cleaned_data.get('months_count')

        if not rate or rate <= 0:
            raise forms.ValidationError('Ставка не может быть ниже 0.')
        if not months_count or months_count <= 0:
            raise forms.ValidationError('Срок не может быть меньше 1 месяца.')

        return self.cleaned_data
