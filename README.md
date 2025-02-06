# Shopping Cart Management System
This is a Python-based Shopping Cart Management System that allows customers and administrators to manage an inventory of products, maintain user accounts, and handle secure transactions. The system supports user registration, login, and secure password storage.

---

# Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Password Security](#password-security)
- [Conventions](#conventions)
- [Modules Used](#modules-used)
- [Future Enhancements](#future-enhancements)

---

## Features

### For Customers
- Register as a customer with secure password storage
- View available products
- Add/remove products to/from the cart
- View past purchase history
- Checkout and store purchase details

### For Admins
- Register as an admin
- Add/remove products in the store inventory
- Manage personal details
- Secure admin login and operations

---

## Project Structure

```plaintext
├── main.py            # Main application file
├── products.txt        # Stores product information (auto-generated)
├── {username}.txt      # Stores customer details (auto-generated)
└── {username}_admin.txt# Stores admin details (auto-generated)

