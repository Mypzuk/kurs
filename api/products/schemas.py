from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int
    image: str
    category: str


class ProductCreate(ProductBase):
    pass


class ProductSchemas(ProductBase):
    product_id: int

    class Config:
        from_attributes = True
