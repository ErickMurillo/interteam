from configuracion.models import OrgCooperantes

def global_vars(request):
    coop = OrgCooperantes.objects.order_by('id')
    return {'coop':coop}