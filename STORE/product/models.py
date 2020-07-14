from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)

    def __str__(self) -> str:
        return f"{self.name} ({self.slug})"


class Value(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60)
    attribute = models.ForeignKey(
        "Attribute", related_name="values", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} [attribute={self.attribute}, name={self.name}]>"


class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)
    attributes = models.ManyToManyField("Attribute")
    has_variants = models.BooleanField(default=True)
    is_shipping_required = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.ForeignKey(Type, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to="product_covers", blank=True)
    video = models.URLField(blank=True)
    category = models.ForeignKey(
        "Category",
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.type} - {self.name}"


class Variant(models.Model):
    product = models.ForeignKey(
        "Product", related_name="variants", on_delete=models.CASCADE
    )
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    values = models.ManyToManyField(Value)

    def __str__(self) -> str:
        return f"{self.product} - {self.name}"


class Image(models.Model):
    variant = models.ForeignKey(
        "Variant", related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images")
    alt = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f'<{self.__class__.__name__} [variant="{self.variant}", alt="{self.image}"]>'
