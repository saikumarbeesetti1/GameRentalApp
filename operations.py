import json
from logging import exception
import string
import random
from json import JSONDecodeError
from datetime import datetime


def Register(type,gamers_json_file,sellers_json_file,Email_ID,Username,Password,Contact_Number):
    '''Register Function || Already Given'''
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
        return True
    elif type.lower()=='gamer':
        f=open(gamers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
            "Wishlist":[],
            "Cart":[],
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()

def Login(type,gamers_json_file,sellers_json_file,Username,Password):
    '''Login Functionality || Return True if successfully logged in else False || Already Given'''
    d=0
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
    else:
        f=open(gamers_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        return False
    for i in range(len(content)):
        if content[i]["Username"]==Username and content[i]["Password"]==Password:
            d=1
            break
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()
    if d==0:
        return False
    return True

def AutoGenerate_ProductID():
    '''Return a autogenerated random product ID || Already Given'''
    product_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    return product_ID

def AutoGenerate_OrderID():
    '''Return a autogenerated random product ID || Already Given'''
    Order_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Order_ID

def days_between(d1, d2):
    '''Calculating the number of days between two dates || Already Given'''
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def Create_Product(owner,product_json_file,product_ID,product_title,product_type,price_per_day,total_stock_available):
    '''Creating a product || Return True if successfully created else False'''
    '''Write your code below'''
    d={"Seller Username": owner, "Product ID": product_ID, "Product Title":product_title, "Product Type": product_type, "Price Per Day":price_per_day, "Total Stock Available":total_stock_available}
    f=open(product_json_file,'r+')
    try:
        content=json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
        f.close()
        return True
    
    
    

def Fetch_all_Products_created_by_seller(owner,product_json_file):
    '''Get all products created by the seller(owner)'''
    '''Write your code below'''
    
    l=[]
    f=open(product_json_file,'r+')
    try:
        content=json.load(f)
        for i in range(len(content)):
            if content[i]["Seller Username"]==owner:
                #print(content[i]["Username"])
                print(content)

    except JSONDecodeError:
        pass
        return l
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()

def Fetch_all_products(products_json_file):
    '''Get all products created till now || Helper Function || Already Given'''
    All_Products_list=[]
    f=open(products_json_file,'r')
    try:
        content=json.load(f)
        All_Products_list=content
    except JSONDecodeError:
        pass
    return All_Products_list

def Fetch_Product_By_ID(product_json_file,product_ID):
    '''Get product deatils by product ID'''
    '''Write your code below'''
    
    file=open(product_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Product ID"] == product_ID:
             return content

    file.seek(0)
    file.truncate()
    json.dump(content,file)        
    file.close()


def Update_Product(Username,product_json_file,product_ID,detail_to_be_updated,new_value):
    '''Updating Product || Return True if successfully updated else False'''
    '''Write your code below'''
    file=open(product_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Product ID"] == product_ID:
            content[i]["Seller Username"]=Username
            content[i]["Price Per Day"]=detail_to_be_updated
            content[i][ "Total Stock Available"]=new_value
            file.seek(0)
            file.truncate()
            json.dump(content,file)
            file.close()
            return True

def Add_item_to_wishlist(Username,product_ID,gamers_json_file):
    '''Add Items to wishlist || Return True if added successfully else False'''
    '''Write your code below'''
    file=open(gamers_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Username"]==Username:
            content[i]["Wishlist"].append(product_ID)
            return True
    file.seek(0)
    file.truncate()
    json.dump(content,file)
    file.close()


def Remove_item_from_wishlist(Username,product_ID,gamers_json_file):
    '''Remove items from wishlist || Return True if removed successfully else False'''
    '''Write your code below'''
    file=open(gamers_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
            if content[i]["Username"]==Username:
                for j in range(len(content[i]["Wishlist"])):
                    if content[i]["Wishlist"][j]==product_ID:
                        del( content[i]["Wishlist"][j])
    file.seek(0)
    file.truncate()
    json.dump(content,file)
    return True
    

def Add_item_to_cart(Username,product_ID,Quantity,Price,gamers_json_file,booking_start_date,booking_end_date,products_json_file):
    '''Add item to the cart || Check whether the quantity mentioned is available || Return True if added successfully else False'''
    '''Add the Product ID, Quantity, Price, Booking Start Date, Booking End Date in the cart as list of dictionaries'''
    '''Write your code below'''
    file=open(gamers_json_file,'r+')
    file_2=open(products_json_file,"r+")
    item_file={
        "Product ID":product_ID,
        "Quantity":Quantity,
        "Price":Price,
        "Booking Start Date":booking_start_date,
        "Booking End Date":booking_end_date,
        
    }
    try:
        content=json.load(file)
        content_1=json.load(file_2)
        for i in range(len(content1)):
            if content_1[i]["Seller Username"]==Username and content_1[i]["Total Stock Available"]>=Quantity:
                content_1[i]["Total Stock Available"]-=Quantity
            for j in range(len(content_1)):
                if item_file not in content[j]["Cart"]:
                    content[j]["Cart"].append(item_file)
                    file.seek(0)
                    file.truncate()
                    json.dump(content,file)
                return True

    except JSONDecodeError:
        l=[]
        l.append(item_file)
        json.dump(l,file)
        return True
    file.close()

def Remove_item_from_cart(Username,product_ID,gamers_json_file):
    '''Remove items from the cart || Return True if removed successfully else False'''
    '''Write your code below'''
    file=open(gamers_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Username"]==Username:
            for j in range(len(content[i]["Cart"])):
                if content[i]["Cart"][j]["Product ID"]==product_ID:
                    del(content[i]["Cart"][j])
                    file.seek(0)
                    file.truncate()
                    json.dump(content,file)
                    file.close()
                    return True
                
    
                
    

def View_Cart(Username,gamers_json_file):
    '''Return the current cart of the user'''
    '''Write your code below'''
    file=open(gamers_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i][ "Username"] == Username:
            for j in range(len(content[i]["Cart"])):
                return content[i]["Cart"][j]
    file.seek(0)
    file.truncate()
    json.dump(content,file)
    file.close()
    

def Place_order(Username,gamers_json_file,Order_Id,orders_json_file,products_json_file):
    '''Place order || Return True is order placed successfully else False || Decrease the quantity of the product orderd if successfull'''
    '''Write your code below'''
    try:
        file=open(gamers_json_file,'r+')
        content=json.load(file)
        file_1=open(orders_json_file,'r+')
        content1=json.load(file_1)
        file_2=open(products_json_file,'r+')
        content2=json.load(file_2)
        for i in range(len(content1)):
                for j in range(len(content)):
                    if content[j]["Username"]==Username:
                        content[j]["Cart"].append(content1[i]["Items"])
                        return True
        
    except JSONDecodeError:
            file.seek(0)
            file.truncate()
            json.dump(content,file)
            file.close()
        
            file_1.seek(0)
            file_1.truncate()
            json.dump(content1,file_1)
            file_1.close()

            file_2.seek(0)
            file_2.truncate()
            json.dump(content2,file_2)
            file_2.close()

def View_User_Details(gamers_json_file,Username):
    '''Return a list with all gamer details based on the username || return an empty list if username not found'''
    '''Write your code below'''
    file=open(gamers_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Username"] == Username:
            return content[i]
    file.close()
    
    

def Update_User(gamers_json_file,Username,detail_to_be_updated,updated_detail):
    '''Update the detail_to_be_updated of the user to updated_detail || Return True if successful else False'''
    '''Write your code below'''
    file=open(gamers_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Username"] == Username:
            content[i]["Password"]=updated_detail
            content[i]["Contact Number"]= detail_to_be_updated
    file.seek(0)
    file.truncate()
    json.dump(content,file)
    file.close()
    return True
    

def Fetch_all_orders(orders_json_file,Username):
    '''Fetch all previous orders for the user and return them as a list'''
    '''Write your code below'''
    file=open(orders_json_file,"r+")
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Ordered by"]==Username:
            return content[i]

    file.seek(0)
    file.truncate()
    json.dump(content,file)
    file.close()