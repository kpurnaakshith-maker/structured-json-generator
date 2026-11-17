from pydantic import ValidationError
from schemas import ProductInfo

invalid_data = {
    "product_name": "Samsung Galaxy S25",
    "brand": "Samsung",
    "storage": "256GB",
    "color": "Blue",
    "price": -85000,
    "camera": "50MP"
}

try:
    product = ProductInfo.model_validate(invalid_data)
    print("Validation successful!")
    print(product)

except ValidationError as error:
    print("Validation failed!")
    print(error)