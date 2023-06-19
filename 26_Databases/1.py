# pip install SQLAlchemy

"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine('sqlite:///products.db')


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    title = Column(String)
    is_stock = Column(Boolean)
    price = Column(Integer)


Base.metadata.create_all(bind=engine)

session = Session(autoflush=False, bind=engine)


def add_product(quantity, title, is_stock, price):
    product = Product(quantity=quantity, title=title, is_stock=is_stock, price=price)
    session.add(product)
    session.commit()
    return product.id


add_product(10, 'Product 1', True, 100)
add_product(5, 'Product 2', False, 200)
add_product(8, 'Product 3', True, 150)


def delete_product(product_id):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        return True
    else:
        return False


def search_product_by_title(title):
    products = session.query(Product).filter(Product.title.ilike(f'%{title}%')).all()
    return products


def update_product_price(product_id, new_price):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        product.price = new_price
        session.commit()
        return True
    else:
        return False
    
delete_product(2)
print(search_product_by_title('Product 2'), 'нашел ')
