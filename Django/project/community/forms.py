from django import forms

from .models import Comment, Report


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        labels = {
            "body": "Comment"
        }
        help_texts = {
            "body": "Maximum 1000 characters."
        }
        error_messages = {
            "body": {
                "required": "Write a comment before submitting.",
                "max_length": "Comments cannot exceed 1000 characters."
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].widget.attrs.update({
            "placeholder": "Share your reaction",
            "rows": 4
        })

    def clean_body(self):
        body = self.cleaned_data["body"].strip()

        if len(body) < 2:
            raise forms.ValidationError("Comments must contain at least 2 characters.")
        return body


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["reason"]
        labels = {
            "reason": "Why should this meme be reviewed?"
        }
        help_texts = {
            "reason": "Explain the issue in 10–1000 characters."
        }
        error_messages = {
            "reason": {
                "required": "Explain why this meme should be reviewed.",
                "max_length": "The reason cannot exceed 1000 characters."
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reason"].widget.attrs.update({
            "placeholder": "Describe the concern",
            "rows": 5
        })

    def clean_reason(self):
        reason =self.cleaned_data["reason"].strip()

        if len(reason) < 10:
            raise forms.ValidationError("Please provide at least 10 characters.")
        return reason