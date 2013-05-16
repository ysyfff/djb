
#---------------The use of context processors(request)-------------------------#
django.core.context_processors.request
If this processor is enabled, 
every RequestContext will contain a variable request, 
which is the current HttpRequest object. 
Note that this processor is not enabled by default; 
you have to activate it.

You might want to use this 
if you find your templates needing to access 
attributes of the current HttpRequest such as the IP address:

{{ request.REMOTE_ADDR }}
#---------------The use of context processors(request)-------------------------#