# ShopVerse - Quick Start Guide

## ✅ Setup Complete!

Your ShopVerse e-commerce website is ready to use!

## What's Already Done

✓ Django project created  
✓ Database migrated  
✓ Sample categories and products added  
✓ All templates and styling configured  
✓ Shopping cart system ready  
✓ Authentication system ready  

## Next Steps

### 1. Create an Admin Account

Run this command to create a superuser:

```bash
python3 manage.py createsuperuser
```

Enter:
- Username (e.g., admin)
- Email (optional)
- Password (enter twice)

### 2. Start the Development Server

```bash
python3 manage.py runserver
```

### 3. Access the Website

Open your browser and visit:

**Main Site**: http://127.0.0.1:8000/  
**Django Admin**: http://127.0.0.1:8000/admin/  
**Custom Admin Dashboard**: http://127.0.0.1:8000/admin-dashboard/ (after making user staff)

## Sample Data Included

The site already has:
- 4 Categories (Trading Cards, Electronics, Clothing, Books)
- 8 Sample Products with prices and stock

## Testing the Site

### As a Customer:
1. Browse products on the home page
2. Click "Shop" to see all products
3. Click on a product to view details
4. Add products to cart
5. Sign up for an account
6. Go to checkout and place an order
7. View your orders in "My Orders"

### As an Admin:
1. Login to Django admin: http://127.0.0.1:8000/admin/
2. Or use the custom dashboard: http://127.0.0.1:8000/admin-dashboard/
3. Add/Edit/Delete products
4. Manage orders and update their status
5. Upload product images

## Making a User Staff

To access the custom admin dashboard:
1. Go to http://127.0.0.1:8000/admin/
2. Click "Users"
3. Select a user
4. Check "Staff status"
5. Save

## Adding Product Images

1. Go to Django admin
2. Click on "Products"
3. Select a product
4. Upload an image in the "Image" field
5. Save

## Project Structure

```
shopverse/          - Main project settings
store/              - Main app (models, views, forms)
templates/          - HTML templates
  └── store/        - Store-specific templates
static/             - CSS and JavaScript
  ├── css/          - Styling
  └── js/           - JavaScript
media/              - Uploaded images
```

## Key URLs

- `/` - Home page
- `/products/` - Product list
- `/product/<slug>/` - Product detail
- `/cart/` - Shopping cart
- `/checkout/` - Checkout (login required)
- `/my-orders/` - Order history (login required)
- `/login/` - Login page
- `/signup/` - Sign up page
- `/admin/` - Django admin
- `/admin-dashboard/` - Custom admin (staff only)

## Features

✓ User authentication (signup, login, logout)  
✓ Product browsing with pagination  
✓ Search and category filtering  
✓ Session-based shopping cart  
✓ Secure checkout process  
✓ Order management  
✓ Admin dashboard  
✓ Responsive mobile design  
✓ Django messages for user feedback  

## Customization

### Change Colors
Edit `static/css/main.css` and modify the CSS variables.

### Add More Products
Use Django admin or the custom admin dashboard.

### Change Site Name
Search and replace "ShopVerse" in templates.

## Troubleshooting

**Server won't start?**
- Make sure port 8000 is not in use
- Check for Python errors in the terminal

**Images not showing?**
- Upload images through Django admin
- Check that media folder exists

**Can't login to admin?**
- Make sure you created a superuser
- Check username and password

## Need Help?

Refer to the full README.md for detailed documentation.

---

**Ready to start?** Run: `python3 manage.py runserver`
