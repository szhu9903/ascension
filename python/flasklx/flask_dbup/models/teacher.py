from resource import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker,scoped_session

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer,primary_key=True)
    name = Column(String(12))
    age = Column(String(2))
    city = Column(String(12))

    def __repr__(self):
        tp1 = "Teacher(id={},name={},age={},city={})"
        return tp1.format(self.id,self.name,self.age,self.city)

# 创建所有表
def create_db():
    Base.metadata.create_all(engine)

# 删除所有表
def drop_db():
    Base.metadata.drop_all(engine)

def add_data(data):
    session = scoped_session(Session)
    session.add(data)
    session.commit()
    session.close()

def search_teacher(table_name):
    session = scoped_session(Session)
    data = session.query(table_name).all()
    return data


if __name__ == '__main__':
    # teacher = Teacher(name='朱帅杰')
    # add_data(teacher)
    data = search_teacher(Teacher)
    print(data)