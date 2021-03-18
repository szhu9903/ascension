from sqlalchemy import create_engine
from tqdm import tqdm
import random,uuid,string
import multiprocessing

db_url = "mysql+mysqlconnector://root:1017@127.0.0.1:3306/db_test"
engine = create_engine(db_url)

def new_sql_data(num):
    try:

        connection = engine.connect()
        name = ['张吉惟','林国瑞','林玟书','林雅南','江奕云','刘柏宏','阮建安','林子帆','夏志豪',
                '吉茹定','李中冰','黄文隆','谢彦文','傅智翔','洪振霞','刘姿婷','荣姿康','吕致盈',
                '方一强','黎芸贵','郑伊雯','雷进宝','吴美隆','吴心真','王美珠','郭芳天','李雅惠',
                '陈文婷','曹敏侑','王依婷','陈婉璇','吴美玉','蔡依婷','郑昌梦','林家纶','黄丽昆',
                '李育泉','黄芸欢','吴韵如','李肇芬','卢木仲','李成白','方兆玉','刘翊惠','丁汉臻',
                '吴佳瑞','舒绿珮','周白芷','张姿妤','张虹伦','周琼玟','倪怡芳','郭贵妃','杨佩芳',
                '黄文旺','黄盛玫','郑丽青','许智云','张孟涵','李小爱','王恩龙','朱政廷','邓诗涵',
                '陈政倩','吴俊伯','阮馨学','翁惠珠','吴思翰','林佩玲','邓海来','陈翊依','李建智',
                '武淑芬','金雅琪','赖怡宜','黄育霖','张仪湖','王俊民','张诗刚','林慧颖','沈俊君',
                '陈淑妤','李姿伶','高咏钰','黄彦宜','周孟儒','潘欣臻','李祯韵','叶洁启','梁哲宇']
        fname = random.choice(name)
        lname = random.choice(string.ascii_lowercase)+str(num)
        age = random.randint(18,50)
        sex = random.choice([0,1])
        sql = """
        insert into person(fname, lname, age, sex)
        VALUES ('%s','%s','%s','%s')
        """%(fname,lname,age,sex)
        connection.execute(sql)
        connection.close()
    except Exception as er:
        print(er)
        return None



def run(num,th):
    print(th)
    for i in tqdm(range(num)):
        new_sql_data(i)



if __name__ == '__main__':
    p = multiprocessing.Pool(multiprocessing.cpu_count())

    for i in range(multiprocessing.cpu_count()):
        p.apply_async(run,args=(10000,i))
    p.close()
    p.join()






