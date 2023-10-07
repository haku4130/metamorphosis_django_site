from .models import ProjectTheme


def project_themes(request):
    themes = ProjectTheme.objects.all()
    return {'project_themes': themes}
