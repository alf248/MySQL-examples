# sql_examples
Creates tables and runs queries on them.

## car dealer
The tables are those of a "car dealer".
- brands (like Toyota)
- models (like Corolla)
- customers
- orders

### queries

count all models for each car manufacturer:
```sh
SELECT brands.name, COUNT(models.model_id)
FROM brands
LEFT JOIN models
    ON models.brand_id = brands.brand_id
GROUP BY (brands.brand_id)
```

count all *fast* models for each car manufacturer:
```sh
SELECT brands.name, COUNT(CASE WHEN models.top_speed > 200 THEN 1 ELSE NULL END) AS count, MAX(models.top_speed) AS max
FROM brands
LEFT JOIN models
    ON models.brand_id = brands.brand_id
GROUP BY (brands.brand_id)
```

total sum of money each model has sold for:
```sh
SELECT models.name, SUM(orders.price) AS total
FROM models
INNER JOIN orders
    ON models.model_id = orders.model_id
GROUP BY (models.model_id)
```

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

## setup
```sh
git clone https://github.com/alf248/sql_examples.git
cd sql_examples
pipenv install
pipenv run python main.py
```
