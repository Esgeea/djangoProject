from trainer.models import Trainer


def get_all_trainers(request):
    get_trainers = Trainer.objects.filter(active=True)
    return {'trainers': get_trainers}