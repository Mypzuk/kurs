from pydantic import BaseModel


class OrderBase(BaseModel):
    customer_id: int
    total_amount: float



class OrderCreate(OrderBase):
    pass

class OrderSchemas(OrderBase):
    order_id: int

    class Config:
        from_attributes = True
