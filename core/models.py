from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True, nullable=False)

    # Связи
    orders = relationship(
        "Orders", back_populates="customer"
    )  # Исправлено: back_populates="customer"


class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(
        String, nullable=True
    )  # TEXT в SQL, но в SQLite String подходит
    price = Column(Float, nullable=False)  # Для цен, например, 99.99
    stock_quantity = Column(Integer, nullable=False)  # Количество на складе
    image = Column(String, nullable=True)  # Путь к изображению (например, URL или путь к файлу)
    category = Column( String(100), nullable=True)  # Название категории (можно сделать отдельной таблицей, если нужно)
    # Добавляем отношение для order_items
    order_items = relationship("OrderItem", back_populates="product")



class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(
        Integer, ForeignKey("customers.customer_id", ondelete="CASCADE"), nullable=False
    )
    total_amount = Column(Float, nullable=False)  # Общая сумма заказа

    # Связи
    customer = relationship("Customers", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Float, nullable=False)

    order = relationship("Orders", back_populates="items")
    product = relationship("Products", back_populates="order_items")