from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def main(request, **kwargs):
    return render(request, 'gameplay/index.html')


class FormMessagesMixin:
    """フォームのエラーメッセージをmessagesで表示するためのMixinクラス

    使用時はform.is_valid()の代わりにself.validate_formを使用する
    """

    def __init__(self):
        self.request = None
        self.cleaned_data = dict()

    def validate_form(self, form):
        if form.is_valid():
            self.cleaned_data = form.cleaned_data
        else:
            # フォームのエラーを表示する
            error_l = []
            if form.errors:
                error_l = sum(form.errors.values(), [])
            else:
                error_l.append('フォームの入力を確認してください。')
            for msg in error_l:
                messages.error(self.request, msg)

        return form.is_valid()
