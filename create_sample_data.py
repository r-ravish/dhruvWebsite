import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopverse.settings')
django.setup()

from store.models import Category, Product

def create_sample_data():
    print("Creating sample categories...")
    
    categories_data = [
        {'name': 'Trading Cards', 'slug': 'trading-cards'},
        {'name': 'Electronics', 'slug': 'electronics'},
        {'name': 'Clothing', 'slug': 'clothing'},
        {'name': 'Books', 'slug': 'books'},
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        categories[cat_data['slug']] = category
        print(f"{'Created' if created else 'Found'} category: {category.name}")
    
    print("\nCreating sample products...")
    
    products_data = [
        {
            'name': 'Pikachu Trading Card',
            'description': 'Rare holographic Pikachu card from the original set. In excellent condition.',
            'price': 49.99,
            'stock': 5,
            'category': 'trading-cards',
            'condition': 'mint',
            'rarity': 'rare',
        },
        {
            'name': 'Charizard Trading Card',
            'description': 'Ultra rare Charizard card. A must-have for any collector.',
            'price': 299.99,
            'stock': 2,
            'category': 'trading-cards',
            'condition': 'mint',
            'rarity': 'ultra_rare',
        },
        {
            'name': 'Wireless Headphones',
            'description': 'Premium wireless headphones with noise cancellation and 30-hour battery life.',
            'price': 149.99,
            'stock': 15,
            'category': 'electronics',
            'condition': 'new',
        },
        {
            'name': 'Smart Watch',
            'description': 'Feature-rich smartwatch with fitness tracking, heart rate monitor, and GPS.',
            'price': 199.99,
            'stock': 10,
            'category': 'electronics',
            'condition': 'new',
        },
        {
            'name': 'Graphic T-Shirt',
            'description': 'Comfortable cotton t-shirt with unique graphic design. Available in multiple sizes.',
            'price': 24.99,
            'stock': 50,
            'category': 'clothing',
            'condition': 'new',
        },
        {
            'name': 'Denim Jacket',
            'description': 'Classic denim jacket perfect for any season. Durable and stylish.',
            'price': 79.99,
            'stock': 20,
            'category': 'clothing',
            'condition': 'new',
        },
        {
            'name': 'Python Programming Book',
            'description': 'Comprehensive guide to Python programming for beginners and intermediate developers.',
            'price': 39.99,
            'stock': 30,
            'category': 'books',
            'condition': 'new',
        },
        {
            'name': 'Web Development Handbook',
            'description': 'Complete handbook covering HTML, CSS, JavaScript, and modern frameworks.',
            'price': 44.99,
            'stock': 25,
            'category': 'books',
            'condition': 'new',
        },
    ]
    
    for prod_data in products_data:
        category_slug = prod_data.pop('category')
        product, created = Product.objects.get_or_create(
            name=prod_data['name'],
            defaults={
                **prod_data,
                'category': categories[category_slug]
            }
        )
        print(f"{'Created' if created else 'Found'} product: {product.name}")
    
    print("\n✓ Sample data created successfully!")
    print("\nYou can now:")
    print("1. Run the server: python3 manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/")
    print("3. Create a superuser: python3 manage.py createsuperuser")
    print("4. Access admin: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    create_sample_data()
