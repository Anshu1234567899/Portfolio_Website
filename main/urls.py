from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('skills/html/', views.html_skill, name='html'),
    path('skills/css/', views.css_skill, name='css'),
    path('skills/javascript/', views.javascript_skill, name='javascript'),
    path('skills/python/', views.python_skill, name='python'),
    path('skills/django/', views.django_skill, name='django'),
    path('skills/flask/', views.flask_skill, name='flask'),
    path('skills/wordpress/', views.wordpress_skill, name='wordpress'),

    path('skills/ai/', views.ai_skill, name='ai'),
    path('skills/powerbi/', views.powerbi_skill, name='powerbi'),

    path('skills/communication/', views.communication_skill, name='communication'),
    path('skills/msword/', views.msword_skill, name='msword'),
    path('skills/powerpoint/', views.powerpoint_skill, name='powerpoint'),
    path('qualification/', views.qualification, name='qualification'),
    path('certifications/', views.certifications, name='certifications'),
    path('resume/', views.resume_view, name='resume'),
]