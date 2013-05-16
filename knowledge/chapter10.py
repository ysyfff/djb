Accessing Foreign Key Values:::::::::::::::::::::::::::::::::::::::::

#----------------m:1--------------------------#
>>> b = Book.objects.get(id=50)
>>> b.publisher
<Publisher: Apress Publishing>

#---------------1:m---------------------------#
>>> p = Publisher.objects.get(name='Apress Publishing')
>>> p.book_set.filter(title__icontains='django')
[<Book: The Django Book>, <Book: Pro Django>]

The attribute name book_set is generated by appending the lower case model name to _set.



