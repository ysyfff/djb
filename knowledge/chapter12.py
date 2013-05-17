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
