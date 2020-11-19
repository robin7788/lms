from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

class IssueBookDetailForm(ModelForm):

    class Meta:
        model = IssueBookDetail

    book = AutoCompleteSelectField('book', required=True, help_text=None)
    user = AutoCompleteSelectField('user', required=True, help_text=None)
