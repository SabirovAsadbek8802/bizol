from django.db.models import IntegerChoices

class ProductStatusChoices(IntegerChoices):
    IN_PREPARATION = 0
    ON_THE_WAY = 1
    DELIEVERED = 2
    