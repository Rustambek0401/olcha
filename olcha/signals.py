import os
import json
# from aiogram.utils.json import json
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete
# from rest_framework.utils import json

from config.settings import BASE_DIR
from config.settings import DEFAULT_FROM_EMAIL
from olcha.models import Product, Group


def post_save_product(sender,instance,created,**kwargs):
    if created:
        print(f'Product {instance.product_name}  created ')
        subject = 'Product '
        message = f'SIZNING BAZANGIZDA  => {instance.product_name} NOMLI Product YARATILDI '
        for_email = DEFAULT_FROM_EMAIL
        to = 'nikola19testla98@gmail.com'
        send_mail(subject,message,for_email,[to,],fail_silently=False)
    else:
        print(f'Product {instance.product_name}  updated ')
post_save.connect(post_save_product,sender=Product)

def post_save_group(sender,instance,created,**kwargs):
    if created:
        print(f'Group {instance.group_name}  created ')
        subject = 'Group '
        message = f'SIZNING BAZANGIZDA  => {instance.group_name} NOMLI Group  YARATILDI '
        for_email = DEFAULT_FROM_EMAIL
        to = 'nikola19testla98@gmail.com'
        send_mail(subject,message,for_email,[to,],fail_silently=False)
    else:
        print(f'Group {instance.group_name}  updated ')
post_save.connect(post_save_group, sender=Group)


# DELETE
def pre_delet_product(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'olcha/delete/Product', f'Product{instance.product_name}.json')
    category_data = {
        'id': instance.id,
        'Name': instance.product_name,
        'Price':instance.price,
        'Description':instance.description,
        'Quantity':instance.quantity,
        'Rating':instance.rating,
        'Discount':instance.discount,
        'Slug': instance.slug,
    }
    with open(file_path, 'w') as json_file:
        json.dump(category_data, json_file, indent=4)


    print(f'Groupni Ochirishdan oldin {instance.product_name}  json faylga saqlandi  ')
    subject = 'Product '
    message = f'SIZNING BAZANGIZDA  => {instance.product_name} NOMLI Product  O\'chirildi  VA olcha/delete/Product papkaga malumotlar saqlandi'
    for_email = DEFAULT_FROM_EMAIL
    to = 'nikola19testla98@gmail.com'
    send_mail(subject, message, for_email, [to, ], fail_silently=False)
pre_delete.connect(pre_delet_product, sender=Product)

def pre_delet_group(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'olcha/delete/Group', f'Group{instance.id}.json')
    category_data = {
        'id': instance.id,
        'Name': instance.group_name,
        'Slug': instance.slug,
    }
    with open(file_path, 'w') as json_file:
        json.dump(category_data, json_file, indent=4)
    print(f'Groupni Ochirishdan oldin {instance.group_name}  json faylga saqlandi  ')

    subject = 'Group '
    message = f'SIZNING BAZANGIZDA  => {instance.group_name} NOMLI Group  O\'chirildi  VA olcha/delete/Group papkaga malumotlar saqlandi '
    for_email = DEFAULT_FROM_EMAIL
    to = 'nikola19testla98@gmail.com'
    send_mail(subject, message, for_email, [to, ], fail_silently=False)
pre_delete.connect(pre_delet_group, sender=Group)


