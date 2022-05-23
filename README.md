# sql_examples
Creates a database, tables and runs queries on them.

Requires MySQL

(The database will be named "sql_examples")

## setup
```sh
git clone https://github.com/alf248/sql_examples.git

cd sql_examples

pipenv install

pipenv run python main.py
```

It will ask for MySQL credentials. Put them in an .env with this content:
```sh
USERNAME=<username>\
PASSWORD=<password>
```

## schema
This schema is about cars. It could be the schema for a car dealer, for example.
- brands (like Toyota)
- models (like Corolla)
- customers
- orders

### schema

    CREATE TABLE brands (
        brand_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        country VARCHAR(100)
    )

    CREATE TABLE models (
        model_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        brand_id INT,
        FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
        top_speed INT
    )

    CREATE TABLE customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        country VARCHAR(100)
    )

    CREATE TABLE orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        
        price INT,
        date DATE,
        customer_id INT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        model_id INT,
        FOREIGN KEY (model_id) REFERENCES models(model_id)
    )
    
  
