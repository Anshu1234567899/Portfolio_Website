from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')

def skills(request):
    return render(request, 'main/skills.html')


def projects(request):
    return render(request, 'main/projects.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        email_message = Mail(
            from_email='patyaldeepanshu05@gmail.com',  # Verified sender
            to_emails='patyaldeepanshu05@gmail.com',
            subject=subject,
            plain_text_content=full_message,
        )

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            sg.send(email_message)
            return render(request, "main/contact.html", {"success": True})
        except Exception as e:
            print(str(e))
            return render(request, "main/contact.html", {"error": True})

    return render(request, "main/contact.html")

def html_skill(request):
    return render(request, "main/skills/html.html")

def css_skill(request):
    return render(request, "main/skills/css.html")

def javascript_skill(request):
    return render(request, "main/skills/javascript.html")

def python_skill(request):
    return render(request, "main/skills/python.html")

def django_skill(request):
    return render(request, "main/skills/django.html")

def flask_skill(request):
    return render(request, "main/skills/flask.html")

def wordpress_skill(request):
    return render(request, "main/skills/wordpress.html")

def ai_skill(request):
    return render(request, "main/skills/ai.html")

def powerbi_skill(request):
    return render(request, "main/skills/powerbi.html")

def communication_skill(request):
    return render(request, "main/skills/communication.html")

def msword_skill(request):
    return render(request, "main/skills/msword.html")

def powerpoint_skill(request):
    return render(request, "main/skills/powerpoint.html")

def qualification(request):
    return render(request, 'main/qualification.html')

def certifications(request):
    return render(request, 'main/certifications.html')

def resume_view(request):
    return render(request, 'main/resume.html')