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
    image = models.URLField(
        'URL da imagem',
        max_length=200,
        null=False
    )
    brand = models.CharField(
        'Marca',
        max_length=50,
        null=False
    )
    reviewScore = models.DecimalField(
        'Pontuação do produto',
        max_digits=3,
        decimal_places=1,
        null=True
    )

    # Human-readable para o nome de entidades
    class Meta:
        ordering = ['title']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    # Representação dos objetos em strings
    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(
        'Nome',
        max_length=150,
        null=False,
        blank=True
    )
    email = models.EmailField(
        'Endereço de e-mail',
        max_length=255,
        unique=True
    )
    favorite = models.ManyToManyField(
        Product,
        verbose_name='Produtos favoritos'
    )

    # Human-readable para o nome de entidades
    class Meta:
        ordering = ['name']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    # Representação dos objetos em strings
    def __str__(self):
        return self.name
