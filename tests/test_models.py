# products/tests/test_models.py
from django.test import TestCase, override_settings
from decimal import Decimal
from products.models import Category, Product

@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class ContactoEmailTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic devices and accessories"
        )

    def test_category_is_created(self):
        self.assertEqual(Category.objects.count(), 1)

    def test_category_str(self):
        # __str__ should return the name
        self.assertEqual(str(self.category), "Electronics")

    def test_description_can_be_blank(self):
        # blank=True means this should save fine with no description
        category = Category.objects.create(name="No Description")
        self.assertEqual(category.description, "")

    def test_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, "Categories")


class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Wireless Mouse",
            description="A smooth wireless mouse",
            price=Decimal("29.99"),
            category=self.category,
            stock=50,
        )

    def test_product_is_created(self):
        self.assertEqual(Product.objects.count(), 1)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Wireless Mouse")

    def test_product_price_precision(self):
        # DecimalField with 2 decimal places should store exactly
        self.assertEqual(self.product.price, Decimal("29.99"))

    def test_product_image_is_optional(self):
        # image has blank=True, null=True — should be None when not provided
        self.assertIsNone(self.product.image.name)

    def test_product_belongs_to_category(self):
        self.assertEqual(self.product.category.name, "Electronics")

    def test_created_at_is_set_automatically(self):
        # auto_now_add=True means it should never be None after saving
        self.assertIsNotNone(self.product.created_at)

    def test_product_stock(self):
        self.assertEqual(self.product.stock, 50)

    def test_deleting_category_deletes_product(self):
        # on_delete=CASCADE — product should disappear when category is deleted
        self.category.delete()
        self.assertEqual(Product.objects.count(), 0)