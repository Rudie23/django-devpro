from website import facade


def list_modules(request):
    return {'MODULES': facade.list_ordered_modules()}
