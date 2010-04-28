Django Banner:
==============
**Django banner adverising app.**


Dependancies:
=============
django-content
    git@github.com:praekelt/django-content.git


Models:
=======

CodeBanner:
-----------
class models.CodeBanner
    
CodeBanner model extends content.models.ModelBase. Add code-based banner to CMS containing HTML / Javascript tags.


API Reference:
~~~~~~~~~~~~~~

FIELDS
******
code
    Text Field with the full HTML/Javascript code snippet to be embedded for the banner.
extends django-content fields
    See django-content README

METHODS
*******
None

MANAGERS
********
None

ImageBanner:
-----------
class models.ImageBanner
    
ImageBanner model extends content.models.ModelBase. Add image-based banners linked to either an internal or external URL to CMS.


API Reference:
~~~~~~~~~~~~~~

FIELDS
******
url
    Char Field containing URL to an internal or external web page.
extends django-content fields
    See django-content README

METHODS
*******
None

MANAGERS
********
None


Tag Reference
=============

Inclusion Tags
--------------
None

Template Tags
-------------
None
