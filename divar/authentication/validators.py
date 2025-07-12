from django.core.validators import RegexValidator


phone_number_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message='Enter a valid  mobile number (e.g. 09xxxxxxxxx)',
        code='invalid_mobile'
    )
