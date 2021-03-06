from django.conf.urls import patterns, include, url
from treeherder.webapp.api import views

from rest_framework import routers

# router for views that are bound to a project
# i.e. all those views that don't involve reference data
project_bound_router = routers.DefaultRouter()
project_bound_router.register(
    r'objectstore',
    views.ObjectstoreViewSet,
    base_name='objectstore',
)
project_bound_router.register(
    r'jobs',
    views.JobsViewSet,
    base_name='jobs',
)
project_bound_router.register(
    r'resultset',
    views.ResultSetViewSet,
    base_name='resultset',
)

project_bound_router.register(
    r'artifact',
    views.ArtifactViewSet,
    base_name='artifact',
)

project_bound_router.register(
    r'note',
    views.NoteViewSet,
    base_name='note',
)

project_bound_router.register(
    r'revision-lookup',
    views.RevisionLookupSetViewSet,
    base_name='revision-lookup',
)

project_bound_router.register(
    r'bug-job-map',
    views.BugJobMapViewSet,
    base_name='bug-job-map',
)


# this is the default router for plain restful endpoints

# refdata endpoints:
default_router = routers.DefaultRouter()
default_router.register(r'product', views.ProductViewSet)
default_router.register(r'machine', views.MachineViewSet)
default_router.register(r'machinenote', views.MachineNoteViewSet)
default_router.register(r'machineplatform', views.MachinePlatformViewSet)
default_router.register(r'buildplatform', views.BuildPlatformViewSet)
default_router.register(r'jobgroup', views.JobGroupViewSet)
default_router.register(r'jobtype', views.JobTypeViewSet)
default_router.register(r'repository', views.RepositoryViewSet)
default_router.register(r'repositoryversion', views.RepositoryVersionViewSet)
default_router.register(r'option', views.OptionViewSet)
default_router.register(r'optioncollection', views.OptionCollectionViewSet)
default_router.register(r'bugscache', views.BugscacheViewSet)
default_router.register(r'failureclassification', views.FailureClassificationViewSet)


urlpatterns = patterns(
    '',
    url(r'^project/(?P<project>[\w-]{0,50})/',
        include(project_bound_router.urls)),
    url(r'^',
        include(default_router.urls)),
)
