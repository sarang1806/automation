import mysql.connector
from mysql.connector import Error

# from steps.customer import customer_name


def get_connection():
    conn = mysql.connector.connect(host='localhost',database='demo_guru99',user='root',password='root')
    if conn.is_connected():
        print(conn.get_server_info())
        return conn
# get_connection()

def get_credentials(role):
    conn= get_connection()
    cursur= conn.cursor()
    sql_query= "select username, password from common_info where role='" + str(role)+"';"
    # sql_query= "select * from common_info where role='" + str(role)+"';"
    print(sql_query)
    cursur.execute(sql_query)
    val = cursur.fetchone()
    # val = cursur.fetchall()
    # for i in val:
    #     print(i)
    #     print(val)
    print(type(val))  # for type
    if val is not None:
        print(val)
        # return val[0]
        return val[0],val[1]
# get_credentials("manager")


# customer---------------------------

def get_custinfo(customer_id):
    conn = get_connection()
    cursur = conn.cursor()
    sql_query = "select customer_name,date_0f_birth,customer_adrdress,city,state,pin,mobile_number,email_id,customer_password from customer_info where customer_id='" + str(customer_id) + "';"
    # sql_query = "select * from customer_info where customer_id='"+str(customer_id)+"';"
    # print(sql_query)
    cursur.execute(sql_query)
    val = cursur.fetchone()
    if val is not None:
        print(val)
        # return val[0]
        return val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8]
# get_custinfo("1")

def custUpdate(customer_id, val):
    conn = get_connection()
    cursur = conn.cursor()

    print("cust_id="+ val)
    sql_query = "update customer_info set cust_id ='"+ str(val) +"' where customer_id ='"+str(customer_id)+"';"
    # sql_query = "update account_info set customer_id ='"+ str(val) +"' where id ='"+str(id)+"';"
    cursur.execute(sql_query)
    conn.commit()

