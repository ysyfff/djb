Deploy Django:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


Turning Off Debug Mode:::::::::::::::::::::::::::::::
set DEBUG to False.

Turning Off Template Debug Mode::::::::::::::::::::::
Similarly, you should set TEMPLATE_DEBUG to False in production.

Implementing a 404 Template::::::::::::::::::::::::::
Here’s a sample 404.html you can use as a starting point. 
It assumes you’re using template inheritance and 
have defined a base.html with blocks called title and content.

{% extends "base.html" %}

{% block title %}Page not found{% endblock %}

{% block content %}
<h1>Page not found</h1>

<p>Sorry, but the requested page could not be found.</p>
{% endblock %}

To test that your 404.html is working, 
just change DEBUG to False and visit a nonexistent URL. 
(This works on the runserver just as well as it works on a production server.)

Implementing a 500 Template::::::::::::::::::::::::::
Similarly, if DEBUG is False, 
then Django no longer displays its useful error/traceback pages 
in case of an unhandled Python exception. 
Instead, it looks for a template called 500.html and renders it. 
Like 404.html, this template should live in your root template directory.

Therefore, the best approach is to avoid template 
inheritance and use something very simple.
Here’s an example 500.html as a starting point:

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>
    <title>Page unavailable</title>
</head>
<body>
    <h1>Page unavailable</h1>

    <p>Sorry, but the requested page is unavailable due to a
    server hiccup.</p>

    <p>Our engineers have been notified, so check back later.</p>
</body>
</html>

Setting Up Error Alerts::::::::::::::::::::::::::::::::
Django is configured to send an e-mail to the site developers 
whenever your code raises an unhandled exception 
– but you need to do two things to set it up.

First, change your ADMINS setting to include your e-mail address, 
along with the e-mail addresses of any other people who need to be notified. 
This setting takes a tuple of (name, email) tuples, like this:

ADMINS = (
    ('John Lennon', 'jlennon@example.com'),
    ('Paul McCartney', 'pmacca@example.com'),
)

Second, make sure your server is configured to send e-mail. 
Setting up postfix, sendmail or any other mail server is outside the scope of this book, 
but on the Django side of things, 
you’ll want to make sure your EMAIL_HOST setting is set to the proper hostname 
for your mail server. It’s set to 'localhost' by default, 
which works out of the box for most shared-hosting environments. 
You might also need to set EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, 
EMAIL_PORT or EMAIL_USE_TLS, depending on the complexity of your arrangement.

Setting Up Broken Link Alerts::::::::::::::::::::::::::::
set SEND_BROKEN_LINK_EMAILS to True (it’s False by default), 
and set your MANAGERS setting to a person or people who will receive these broken-link e-mails. 
MANAGERS uses the same syntax as ADMINS. For example:

MANAGERS = (
    ('George Harrison', 'gharrison@example.com'),
    ('Ringo Starr', 'ringo@example.com'),
)

DJANGO_SETTINGS_MODULE:::::::::::::::::::::::::::::::::::
The instructions are different for each environment, 
but one thing remains the same: in each case, 
you will have to tell the Web server your DJANGO_SETTINGS_MODULE. 
This is the entry point into your Django application. 
The DJANGO_SETTINGS_MODULE points to your settings file, 
which points to your ROOT_URLCONF, which points to your views, and so on.

DJANGO_SETTINGS_MODULE is the Python path to your settings file. 
For example, assuming the mysite directory is on your Python path, 
the DJANGO_SETTINGS_MODULE for our ongoing example is 'mysite.settings'.