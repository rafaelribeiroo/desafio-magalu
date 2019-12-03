from django.db import models


class Product(models.Model):
    # Por padrão, o django já cria uma coluna de id
    title = models.CharField(
        'Título',
        max_length=50,
        unique=True,
        # A nível DB
        null=False,
        # ... template
        blank=True
    )
    price = models.DecimalField(
        'Preço',
        max_digits=6,
        decimal_places=2,
        null=False
    )
    image = models.URLField('URL da imagem', max_length=200, null=False)
    brand = models.CharField('Marca', max_length=50, null=False)
    reviewScore = models.DecimalField(
        'Pontuação do produto',
        max_digits=3,
        decimal_places=1
    )
