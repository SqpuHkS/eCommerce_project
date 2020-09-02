from django.dispatch import Signal

analytic_signal = Signal(providing_args=['instance', 'request'])
