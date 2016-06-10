from django.forms import TextInput


class CustomTextField(TextInput):

    def __init__(self, placeholder):
        super(CustomTextField, self).__init__()
        self.attrs.update(
            {
                'type': 'text',
                'class': 'text_field',
                'placeholder': placeholder
            }
        )
