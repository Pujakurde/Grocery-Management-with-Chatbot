# Grocery Store Management System

This project is a basic Python-based management system for a grocery store. It integrates with a MySQL database to manage various aspects of the store, such as units of measurement (UOM), orders, and product details. The system provides functionalities for adding, modifying, and deleting units, orders, and products.

## Features

- **Unit Management**:
  - Add a new unit.
  - Modify an existing unit's details.
  - Delete a unit.

- **Order Management**:
  - Add new orders.
  - Modify existing orders.
  - Delete orders.

- **Product Management**:
  - Add new products.
  - Modify existing product details.
  - Delete products.

- **Chatbot**:
  - Simple text-based interaction for a personalized experience.

## Prerequisites

- Python 3.x
- MySQL 5.x or above
- MySQL Connector for Python

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install required packages**:
   Install the necessary Python packages:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up the MySQL Database**:
   Ensure that you have MySQL running and create a database called `grocery_store`:
   ```sql
   CREATE DATABASE grocery_store;
   ```

4. **Configure Database Credentials**:
   Update the database credentials in the Python code (e.g., host, username, password).

## Usage

1. **Running the Program**:
   To run the grocery store management system:
   ```bash
   python grocery_store_management.py
   ```

2. **Interacting with the System**:
   The program will display menus for managing units, orders, and products. Simply follow the prompts to add, modify, or delete entries in the database.

3. **Chatbot**:
   The system includes a simple chatbot. Type `exit` to end the conversation.

## Database Tables

The system assumes the following database schema:

### 1. **Units of Measurement (uom)**
   - `uom_id` (INT, Primary Key)
   - `uom_name` (VARCHAR)

### 2. **Orders**
   - `order_id` (INT, Primary Key)
   - `customer_name` (VARCHAR)
   - `total` (DECIMAL)
   - `datetime` (DATETIME)

### 3. **Products**
   - `product_id` (INT, Primary Key)
   - `name` (VARCHAR)
   - `uom_id` (INT, Foreign Key references `uom(uom_id)`)
   - `price_per_unit` (DECIMAL)

## Example Usage

1. **Unit Management**:
   - Add a new unit (e.g., "Kg", "Litre").
   - Modify existing units.
   - Delete a unit by ID.

2. **Order Management**:
   - Add a new order, specifying the customer name, total price, and date.
   - Modify or delete orders using their unique order IDs.

3. **Product Management**:
   - Add a new product, specifying the product name, unit ID, and price per unit.
   - Modify or delete product details.

