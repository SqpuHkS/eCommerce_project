from .signals import analytic_signal

class AnalyticMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(AnalyticMixin, self).get_context_data(*args, **kwargs)
        request = self.request
        instance = context['object']
        if instance:
            analytic_signal.send(instance.__class__, instance=instance, request=request)
        return context