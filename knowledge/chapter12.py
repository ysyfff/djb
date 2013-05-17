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



