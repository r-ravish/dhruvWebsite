# ShopVerse - E-Commerce Website

A fully functional e-commerce website built with Django for the backend and HTML, CSS, and vanilla JavaScript for the frontend.

## Features

- **User Authentication**: Sign up, login, and logout functionality
- **Product Management**: Browse products with pagination, search, and category filtering
- **Shopping Cart**: Session-based cart with add, update, and remove functionality
- **Checkout Process**: Secure checkout with order placement
- **Order Management**: Users can view their order history
- **Admin Dashboard**: Custom admin interface for managing products and orders
- **Django Admin**: Full Django admin panel access for staff users
- **Responsive Design**: Mobile-first responsive layout

## Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Authentication**: Django's built-in authentication system

## Project Structure

```
shopverse/
├── shopverse/          # Main project directory
│   ├── settings.py     # Project settings
│   ├── urls.py         # Main URL configuration
│   └── wsgi.py         # WSGI configuration
├── store/              # Main app directory
│   ├── models.py       # Database models (Product, Category, Order, OrderItem)
│   ├── views.py        # View functions
│   ├── urls.py         # App URL configuration
│   ├── forms.py        # Django forms
│   ├── admin.py        # Django admin configuration
│   ├── cart.py         # Shopping cart logic
│   └── context_processors.py  # Custom context processors
├── templates/          # HTML templates
│   ├── base.html       # Base template with navbar and footer
│   └── store/          # Store app templates
├── static/             # Static files
│   ├── css/            # CSS files
│   └── js/             # JavaScript files
├── media/              # User-uploaded files (product images)
└── manage.py           # Django management script
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project

```bash
cd /path/to/dhruvWebsite
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install django pillow
```

### Step 4: Run Database Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Step 5: Create a Superuser (Admin Account)

```bash
python3 manage.py createsuperuser
```

Follow the prompts to create an admin account with:
- Username
- Email (optional)
- Password

### Step 6: Create Some Sample Data (Optional)

You can add categories and products through the Django admin panel or the custom admin dashboard.

1. Start the development server (see Step 7)
2. Go to http://127.0.0.1:8000/admin/
3. Login with your superuser credentials
4. Add categories first (e.g., "Trading Cards", "Electronics", "Clothing")
5. Add products with images, prices, and stock

### Step 7: Run the Development Server

```bash
python3 manage.py runserver
```

The website will be available at: http://127.0.0.1:8000/

## Usage Guide

### For Customers

1. **Browse Products**: Visit the home page or click "Shop" to see all products
2. **Search & Filter**: Use the search bar or category filters to find products
3. **View Product Details**: Click on any product to see full details
4. **Add to Cart**: Click "Add to Cart" on product pages
5. **Manage Cart**: View and update quantities in your cart
6. **Checkout**: Click "Proceed to Checkout" (requires login)
7. **Place Order**: Fill in shipping information and place your order
8. **View Orders**: Check "My Orders" to see your order history

### For Administrators

#### Django Admin Panel (Full Control)

1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Manage all aspects of the site:
   - Add/Edit/Delete Categories
   - Add/Edit/Delete Products
   - View and Update Orders
   - Manage Users

#### Custom Admin Dashboard

1. Login as a staff user
2. Click "Admin" in the navigation menu
3. Access the custom admin dashboard at http://127.0.0.1:8000/admin-dashboard/
4. Features:
   - View all products in a table
   - Add new products with a form
   - Edit existing products
   - Delete products (with confirmation)
   - View recent orders
   - Update order status (Pending → Shipped → Completed)

### Creating Staff Users

To give a user access to the admin dashboard:

1. Go to Django admin: http://127.0.0.1:8000/admin/
2. Click on "Users"
3. Select the user you want to make staff
4. Check the "Staff status" checkbox
5. Save

## Models

### Category
- name: Category name
- slug: URL-friendly version of name

### Product
- name: Product name
- slug: URL-friendly version of name
- description: Product description
- price: Product price (decimal)
- stock: Available quantity
- category: Foreign key to Category
- image: Product image (optional)
- condition: New/Used/Mint (optional)
- rarity: Common/Uncommon/Rare/Ultra Rare (optional)
- created_at: Creation timestamp
- updated_at: Last update timestamp

### Order
- user: Foreign key to User (nullable)
- full_name: Customer name
- email: Customer email
- phone: Customer phone
- address: Shipping address
- city: City
- postal_code: Postal code
- country: Country
- status: Pending/Shipped/Completed/Cancelled
- created_at: Order date

### OrderItem
- order: Foreign key to Order
- product: Foreign key to Product
- quantity: Quantity ordered
- price_at_time: Price when ordered

## Key Features Explained

### Session-Based Shopping Cart

The cart is stored in Django sessions, allowing users to add items without logging in. The cart persists across page loads and is only cleared after checkout.

### Authentication & Authorization

- Users must sign up/login to place orders
- Staff users have access to the admin dashboard
- Superusers have full Django admin access

### Order Processing

When an order is placed:
1. Order and OrderItem records are created
2. Product stock is automatically reduced
3. Cart is cleared
4. User is redirected to order confirmation page

### Responsive Design

The site uses CSS Grid and Flexbox for a mobile-first responsive layout that works on all screen sizes.

## Customization

### Changing Colors

Edit `/static/css/main.css` and modify the CSS variables in the `:root` selector:

```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #64748b;
    /* ... other colors */
}
```

### Adding More Product Fields

1. Add fields to the Product model in `store/models.py`
2. Run migrations: `python3 manage.py makemigrations && python3 manage.py migrate`
3. Update forms, templates, and admin as needed

### Changing Site Name

Search and replace "ShopVerse" in templates and update the logo in `templates/base.html`.

## Troubleshooting

### Images Not Displaying

Make sure:
1. `MEDIA_URL` and `MEDIA_ROOT` are set in `settings.py`
2. Media URLs are included in `urls.py`
3. Images are uploaded through the admin panel

### Static Files Not Loading

Run:
```bash
python3 manage.py collectstatic
```

### Database Errors

Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3
python3 manage.py migrate
python3 manage.py createsuperuser
```

## Security Notes

**Important**: This is a development setup. For production:

1. Set `DEBUG = False` in `settings.py`
2. Change `SECRET_KEY` to a secure random value
3. Set `ALLOWED_HOSTS` appropriately
4. Use a production database (PostgreSQL/MySQL)
5. Use a proper web server (Gunicorn + Nginx)
6. Enable HTTPS
7. Configure proper media file storage (e.g., AWS S3)
8. Add payment gateway integration for real transactions

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please refer to the Django documentation at https://docs.djangoproject.com/
