from django.contrib import admin

from store.models import Brand,Tag,Size,Category,Product,User

admin.site.register(User)

admin.site.register(Brand)

admin.site.register(Tag)

admin.site.register(Size)

admin.site.register(Category)

admin.site.register(Product)