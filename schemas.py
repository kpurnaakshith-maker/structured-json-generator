
from pydantic import BaseModel, Field


class ProductInfo(BaseModel):
    product_name: str = Field(description="Name of the product")
    brand: str = Field(description="Brand of the product")
    storage: str = Field(description="Storage capacity")
    color: str = Field(description="Product color")
    price: float = Field(ge=0, description="Product price")
    camera: str = Field(description="Camera details")
