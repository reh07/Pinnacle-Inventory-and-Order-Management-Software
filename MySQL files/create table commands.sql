create table inventory(Item_ID integer(6) primary key, Item_Name varchar(30) not null, Category varchar(20), Stock_Quantity integer(5) not null, Price decimal(10,2));

create table supplier(Supplier_ID integer(4) primary key, Supplier_Company varchar(20) not null, Item_ID integer(6), Email varchar(30) unique, Phone_num varchar(10) unique, 
foreign key (Item_ID) references inventory(Item_ID) ON DELETE CASCADE);

create table supplier_orders(Supply_ID integer(8) primary key, Supplier_ID integer(4),Item_ID integer(6), Item_Quantity integer(5), 
foreign key (Item_ID) references Inventory(Item_ID) ON DELETE CASCADE, foreign key (Supplier_ID) references Supplier(Supplier_ID) ON DELETE CASCADE);





create table orders(Order_ID integer(5) primary key, Delivery_pincode integer(6), Payment_amt decimal(10,2) default 0, Contact_Num varchar(10), Contact_Email varchar(40));

create table order_list(Order_Num integer(8) primary key, Order_ID integer(5), Item_ID integer(5), Quantity integer(3),  Order_Price decimal(10,2) default 0, 
foreign key (Order_ID) references Orders(Order_ID) ON DELETE CASCADE, foreign key (Item_ID) references Inventory(Item_ID) ON DELETE CASCADE);