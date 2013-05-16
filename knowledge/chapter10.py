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


Accessing Many-to-Many Values:::::::::::::::::::::::::::::::::::::::

>>> b = Book.objects.get(id=50)
>>> b.authors.all()
[<Author: Adrian Holovaty>, <Author: Jacob Kaplan-Moss>]
>>> b.authors.filter(first_name='Adrian')
[<Author: Adrian Holovaty>]
>>> b.authors.filter(first_name='Adam')
[]

It works in reverse, too. To view all of the books for an author, use author.book_set, like this:

>>> a = Author.objects.get(first_name='Adrian', last_name='Holovaty')
>>> a.book_set.all()
[<Book: The Django Book>, <Book: Adrian's Other Book>]
