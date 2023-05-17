"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Определение модели Работники
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
    position_id = Column(Integer, ForeignKey('positions.id'))
    position = relationship("Position", back_populates="employees")

# Определение модели Должности
class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", back_populates="position")

# Создание базы данных
engine = create_engine('sqlite:///company.db')
Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Функция для добавления новых должностей и работников
def add_employees_and_positions():
    # Добавление должностей
    position1 = Position(name="Менеджер")
    position2 = Position(name="Разработчик")
    session.add_all([position1, position2])
    session.commit()

    # Добавление работников
    employee1 = Employee(name="Иван", experience=3, position=position1)
    employee2 = Employee(name="Алексей", experience=7, position=position1)
    employee3 = Employee(name="Елена", experience=5, position=position2)
    employee4 = Employee(name="Дмитрий", experience=8, position=position2)
    employee5 = Employee(name="Ольга", experience=2, position=position1)
    employee6 = Employee(name="Сергей", experience=6, position=position2)
    session.add_all([employee1, employee2, employee3, employee4, employee5, employee6])
    session.commit()

# Функция для вывода всех должностей заданного работника
def get_employee_positions(employee_name):
    employee = session.query(Employee).filter_by(name=employee_name).first()
    if employee:
        position = employee.position
        if position:
            print(f"Должности работника {employee_name}:")
            print(position.name)
        else:
            print("У работника нет должностей.")
    else:
        print("Работник не найден.")

# Функция для вывода всех работников по должности
def get_employees_by_position(position_name):
    position = session.query(Position).filter_by(name=position_name).first()
    if position:
        employees = [employee.name for employee in position.employees]
        if employees:
            print(f"Работники с должностью {position_name}:")
            for employee in employees:
                print(employee)
        else:
            print("На данной должности нет работников.")
    else:
        print("Должность не найдена.")

# Функция для вывода всех работников определенной должности со стажем больше 5
def get_employees_by_position_and_experience(position_name):
    employees = session.query(Employee).join(Position).filter(Position.name == position_name, Employee.experience > 5).all()
    if employees:
        print(f"Работники на должности {position_name} со стажем больше 5:")
        for employee in employees:
            print(f"Имя: {employee.name}, Стаж: {employee.experience}")
    else:
        print(f"На должности {position_name} нет работников со стажем больше 5.")

# Добавление новых должностей и работников
add_employees_and_positions()

# Получение выбора пользователя
choice = input("Введите номер действия, которое хотите выполнить:\n"
               "1 - Вывести все должности заданного работника\n"
               "2 - Вывести всех работников по должности\n"
               "3 - Вывести всех работников определенной должности со стажем больше 5\n")

if choice == "1":
    employee_name = input("Введите имя работника: ")
    get_employee_positions(employee_name)
elif choice == "2":
    position_name = input("Введите название должности: ")
    get_employees_by_position(position_name)
elif choice == "3":
    position_name = input("Введите название должности: ")
    get_employees_by_position_and_experience(position_name)
else:
    print("Некорректный выбор.")
