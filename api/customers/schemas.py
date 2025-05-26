from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    phone: str

class CustomerCreate(CustomerBase):
    pass

class CustomerSchemas(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True