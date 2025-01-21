import mysql.connector # type: ignore

mycon=mysql.connector.connect(host="localhost",user="root",passwd="Success@1234#",database="grocery_store")
if mycon.is_connected() == False:
    print("not connected")  

     
cursor=mycon.cursor()

def chatbot():
    print("Welcome to the Simple Chatbot!")
    print("You can type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            # Simple echo response
            print("Chatbot:", user_input)


if __name__ == "__main__":
    chatbot()


   
def Del_unit():
    
    print("\n\n\n")
    print(" "*25, "In Delete Unit function ")
    print("\n\n\n")

    cursor.execute("SELECT * FROM grocery_store.uom")
    
    dt=cursor.fetchall()
    
    for row in dt:
        print(row)  
        
    uom_id = int(input("Enter the Unit's Id : "))
    
    qr="delete FROM grocery_store.uom where uom_id=%s"%(uom_id)
    
    print("Department details Deleted Successfully ")
    
    cursor.execute(qr)
    
    mycon.commit()
    
    print("Record for ",uom_id," Department is deleted Successfully")

    print("="*77)
    
def Mod_unit():
    print("\n\n\n")
    print(" " * 25, "In Modify Unit details function ")
    print("\n\n\n")

    cursor.execute("SELECT * FROM grocery_store.uom")

    dt = cursor.fetchall()

    for row in dt:
        print(row)

    uom_id = int(input("Enter the Unit's Id : "))

    qr = "SELECT * FROM grocery_store.uom WHERE uom_id = %s" % uom_id

    cursor.execute(qr)
    dt = cursor.fetchall()

    for row in dt:
        uom_name = row[1]

    print(" " * 25, "1. Unit's Name ")
    print(" " * 25, "0. Exit")

    ch = int(input("Please enter the right choice (1/0) : "))

    while True:
        if ch == 1:
            uom_name = input("Enter the Unit's Name : ")
            break
        elif ch == 0:
            break
        else:
            print("Please enter the right choice (1/0) : ")

    qr = "UPDATE `grocery_store`.`uom` SET `uom_name` = '%s' WHERE (`uom_id` = %s)" % (uom_name, uom_id)
    print("Unit is updated successfully")

    cursor.execute(qr)
    mycon.commit()

    print("=" * 77)

def Add_unit():
    
    uom_id = int(input("enter the Unit's Id : "))
    uom_name = input("enter the Unit's Name : ")
    
    qr="INSERT INTO `grocery_store`.`uom` (`uom_id`, `uom_name`) VALUES (%s, '%s')"%(uom_id, uom_name)
    
    print("Unit Details Added Successfully")
    cursor.execute(qr)
    
    mycon.commit()
    
    print("="*77)

            
def Unit():
    
    print("\n\n\n")
    print(" "*25, "In Unit details function ")
    
    while True :
        print("="*20,"GROCERY STORE MANAGEMENT SYSTEM","="*20)
        print(" "," "*25,"1. Add New Unit"," ")
        print(" "," "*25,"2. Modify Unit Details"," ")
        print(" "," "*25,"3. Delete Unit"," ")
        print(" "," "*25,"0. Exit"," ")
        print("="*77)
        ch=input(" Enter your coice (1/2/3/0) : ")

        if ch== "1":
            print(" Write Add Unit function above and call it here ")
            Add_unit()
        elif ch=="2" :
            print(" Write Modify Unit function above and call it here ")
            Mod_unit()
        elif ch=="3" :
            print(" Write Delete function above and call it here ")
            Del_unit()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! "," ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) : ")

def Del_order():
    
    print("\n\n\n")
    print(" "*25, "In Delete Order function ")
    print("\n\n\n")

    cursor.execute("SELECT * FROM grocery_store.orders")
    
    dt=cursor.fetchall()
    
    for row in dt:
        print(row)  
        
    order_id= int(input("Enter order Id : "))
    
    qr="delete from grocery_store.orders where order_id=%s"%(order_id)
    
    print("Order Deleted Successfully ")
    
    cursor.execute(qr)
    
    mycon.commit()
    
    print("Record for ",order_id," Order is deleted Successfully")

    print("="*77)

def Modify_order():
    print("\n\n\n")
    print(" "*25, "In Modify Order function ")
    print("\n\n\n")
    
    cursor.execute("SELECT * FROM grocery_store.orders")
    dt = cursor.fetchall()
    
    for row in dt:
        print(row)
        
    order_id = int(input("Enter order Id : "))
    qr = "SELECT * FROM grocery_store.orders WHERE order_id = %s" % order_id
        
    cursor.execute(qr)
    mad = cursor.fetchall()

    for row in mad:
        customer_name = row[1]
        total = row[2]
        datetime = row[3]  # Assuming datetime is stored as string in database
        
    print(" "*25, "1. Customer Name ")
    print(" "*25, "2. Total")
    print(" "*25, "3. Datetime")
    print(" "*25, "0. Exit")
        
    ch = int(input("Please enter right choice (1/2/3/0) : "))
                    
    while True:
        if ch == 1:
            customer_name = input("Enter the Customer name : ")
            break
        elif ch == 2:
            total = int(input("Enter the Total bill of the customer : "))
            break
        elif ch == 3:
            datetime = input("Enter datetime in format of YYYY-MM-DD HH:MM:SS : ")
            break
        elif ch == 0:
            break
        else:
            print(" "*25, "Please enter right choice (1/2/3/0) : ")

    qr = "UPDATE grocery_store.orders SET customer_name = '%s', total = %s, datetime = '%s' WHERE order_id = %s" % (customer_name, total, datetime, order_id)
    print("Order updated successfully")

    cursor.execute(qr)
    mycon.commit()

    print("="*77)


def Add_Order():
    print("\n\n\n")
    print(" "*25, "In Add Order function ")
    print("\n\n\n")
    cursor.execute("SELECT * FROM grocery_store.orders")
    Ad = cursor.fetchall()
    for row in Ad:
        print(row)

    order_id = int(input("Enter order Id : "))
    customer_name = input("Enter the Customer name : ")
    total = int(input("Enter the Total Price of the order : "))
    datetime = input("Enter datetime in format of YYYY-MM-DD HH:MM:SS : ")

    qr = "INSERT INTO `grocery_store`.`orders` (`order_id`, `customer_name`, `total`, `datetime`) VALUES (%s, '%s', %s, %s)"%(order_id, customer_name, total, datetime)
    cursor.execute(qr) 

    mycon.commit()
    print("New order Added Successfully")



def Order():
    
    print("\n\n\n")
    print(" "*25, "In Order_details function ")
    
    while True :
        print("="*20,"GROCERY STORE MANAGEMENT SYSTEM","="*20)
        print(" "," "*25,"1. Add New Order"," ")
        print(" "," "*25,"2. Modify Order "," ")
        print(" "," "*25,"3. Delete Order"," ")
        print(" "," "*25,"0. Exit"," ")
        print("="*77)
        ch=input(" Enter your choice (1/2/3/0) : ")

        if ch== "1":
            print(" Write Add Order function above and call it here ")
            Add_Order()
        elif ch=="2" :
            print(" Write Modify Order Details function above and call it here ")
            Modify_order()
        elif ch=="3" :
            print(" Write Delete function above and call it here ")
            Del_order()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! "," ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) : ")
            

def Del_order_details():
    
    print("\n\n\n")
    print(" "*25, "In Delete Order function ")
    print("\n\n\n")

    cursor.execute("SELECT * FROM grocery_store.order_details")
    
    dt=cursor.fetchall()
    
    for row in dt:
        print(row)  
        
    order_id= int(input("Enter order Id"))
    
    qr="delete from grocery_store.order_details where order_id=%s"%(order_id)
    
    print("Order Details Deleted Successfully ")
    
    cursor.execute(qr)
    
    mycon.commit()
    
    print("Record for ",order_id," Order is deleted Successfully")

    print("="*77)


def Modify_order_details():
    print("\n\n\n")
    print(" "*25, "In Modify Order details function ")
    print("\n\n\n")

    cursor.execute("SELECT * FROM grocery_store.order_details")
    dt = cursor.fetchall()

    for row in dt:
        print(row)

    order_id = int(input("Enter order Id : "))
    qr = "SELECT * FROM grocery_store.order_details WHERE order_id = %s" % order_id

    cursor.execute(qr)
    mad = cursor.fetchall()

    for row in dt:
        product_id = row[1]
        quantityl = row[2]
        total_price = row[3]

    print(" "*25, "1. Product Id ")
    print(" "*25, "2. Quantity")
    print(" "*25, "3. Total Price")
    print(" "*25, "0. Exit")

    ch = int(input("Please enter right choice (1/2/3/0) : "))

    while True:
        if ch == 1:
            product_id = int(input("Enter the Product Id : "))
            break
        elif ch == 2:
            quantityl = int(input("Enter the quantity of product : "))
            break
        elif ch == 3:
            total_price = int(input("Enter the total price : "))
            break
        elif ch == 0:
            break
        else:
            print(" "*25, "Please enter right choice (1/2/3/0) : ")

    qr = "UPDATE grocery_store.order_details SET product_id = %s, quantityl = %s, total_price = %s WHERE order_id = %s" % (product_id, quantityl, total_price, order_id)

    print("Order's details updated successfully")
    cursor.execute(qr)
    mycon.commit()

    print("=" * 77)


def Add_Order_details():
    
    print("\n\n\n")
    print(" "*25, "In Add Order function ")
    print("\n\n\n")
    cursor.execute("SELECT * FROM grocery_store.order_details")
    Ad=cursor.fetchall()
    for row in Ad:
        print(row)
        
    order_id= int(input("Enter order Id : "))    
    product_id = int(input("Enter the Product Id : "))
    quantityl = int(input("Enter the quantity of product : "))
    total_price= int(input("Enter the total price : "))
    
    qr="INSERT INTO `grocery_store`.`order_details` (`order_id`, `product_id`, `quantityl`, `total_price`) VALUES (%s,%s,%s,%s)"%(order_id, product_id, quantityl, total_price)
    print("New order Added Successfully ")

    cursor.execute(qr)
    
    mycon.commit()

        
def Order_details():
    
    print("\n\n\n")
    print(" "*25, "In Order_details function ")
    
    while True :
        print("="*20,"GROCERY STORE MANAGEMENT SYSTEM","="*20)
        print(" "," "*25,"1. Add Order Details"," ")
        print(" "," "*25,"2. Modify Order Details"," ")
        print(" "," "*25,"3. Delete Order"," ")
        print(" "," "*25,"0. Exit"," ")
        print("="*77)
        ch=input(" Enter your choice (1/2/3/0) : ")

        if ch== "1":
            print(" Write Add Order function above and call it here ")
            Add_Order_details()
        elif ch=="2" :
            print(" Write Modify Order Details function above and call it here ")
            Modify_order_details()
        elif ch=="3" :
            print(" Write Delete function above and call it here ")
            Del_order_details()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! "," ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) : ")
            

def Del_Product():
    
    print("\n\n\n")
    print(" "*25, "In Delete Product function ")
    print("\n\n\n")
    cursor.execute("SELECT * FROM grocery_store.products")
    dt=cursor.fetchall()
        
       
    for row in dt:
        print(row)  
        
    product_id = int(input("Enter the Product Id : "))
                          
    qr="Delete from Product where product_id = %s"%(product_id)
    print("Product Details Deleted Successfully")
    
    cursor.execute(qr)
    
    mycon.commit()
    
    print("Record for Product",qr,"has been deleted Successfully")
    
    print("="*77)



def modify_product():
    
    print("\n\n\n")
    print(" "*25, "In Modify_Product_details function ")
    print("\n\n\n")
    cursor.execute("SELECT * FROM grocery_store.products;")
    me=cursor.fetchall()
    
    for row in me :
        print(row)
        
    product_id = int(input("Enter the Product Id : "))
    qr="SELECT * FROM grocery_store.products where product_id=%s"%(product_id)
        
    cursor.execute(qr)
    me=cursor.fetchall()
        

    for row in me:
            name = row[1]
            uom_id = row[2]
            price_per_unit = row[3]
            
           
        
    print(" "*25,"1. Product Name ")
    print(" "*25,"2. Product's Unit id ")
    print(" "*25,"3. Product's Price Per Unit")
    print(" "*25,"0. Exit")
        
    ch=int(input("Pls enter which field you wish to modify : "))
                    
    while True :
        if ch==1:
            name = input("Enter the Product's Name : ")
            break
        elif ch==2:
            uom_id = int(input("Enter the  Unit Id : "))
            break
        elif ch==3:
            price_per_unit = int(input("Enter price per Unit for the product : "))
            break
        elif ch==0 :
            break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) :")

    query = "UPDATE grocery_store.products SET name = %s, uom_id = %s, price_per_unit = %s WHERE product_id = %s"

# Provide the values separately as a tuple or list
    values = (name, uom_id, price_per_unit, product_id)

# Execute the query with the provided values
    cursor.execute(query, values)

    mycon.commit()
                    
    print("="*77)
        
    print("Product's details updated sucessfully!")
        
def New_product():
    product_id = int(input("Enter the Product Id : "))
    name = input("Enter the Product's Name : ")
    uom_id = int(input("Enter the Unit Id(1:'Each',2:'Kg',3:'Litre') : "))
    price_per_unit = int(input("Enter price per Unit for the product : "))

    qr = "INSERT INTO grocery_store.products (name, uom_id, price_per_unit) VALUES ('%s', %s, %s)" % (name, uom_id, price_per_unit)

    print("Product Details Added Successfully")

    cursor.execute(qr)
    mycon.commit()

    print("=" * 77)


def product_details():
    
    print("\n\n\n")
    print(" "*25, "In Product_details function ")
    
    while True :
        print("="*20,"GROCERY STORE MANAGEMENT SYSTEM","="*20)
        print(" "," "*25,"1. Add New Product details"," ")
        print(" "," "*25,"2. Modify Product Details"," ")
        print(" "," "*25,"3. Delete Product details"," ")
        print(" "," "*25,"0. exit"," ")
        print("="*77)
        ch=input(" Enter your choice (1/2/3/0) : ")

        if ch== "1":
            print(" Write Add Product function above and call it here ")
            New_product()

        elif ch=="2" :
            print(" Write Modify Product function above and call it here ") 
            modify_product()
        elif ch=="3" :
            
            Del_Product()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! "," ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) : ")



def Main_menu() :
    print("\n"*30 )
    
    while True :
        print("="*20,"GROCERY STORE MANAGEMENT SYSTEM","="*20)
        print(" "*25,"1. Product details  " )
        print(" "*25,"2. New Order  ")
        print(" "*25,"3. Order Details")
        print(" "*25,"4. Unit")
        print(" "*25,"5. Interaction with chatbot")
        print(" "*25,"0. Exit")
        print("="*77)
        ch=input(" Enter your choice (1/2/3/4/5/0) : ")
        if ch== "1":
            product_details()
        elif ch=="2" :
            Order()
        elif ch=="3" :
            Order_details()
        elif ch=="4" :
            Unit()
        elif ch=="5" :
            chatbot()
        elif ch=="0" :
            print(" "*30," THANK YOU!!! "," ")
            break
        else :
            print(" "*25,"Please enter right choice (1/2/3/4/0) : ")

Main_menu()

