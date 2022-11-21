delimiter //

create function order_price(O_num int(8)) RETURNS decimal(10,2)
reads sql data deterministic
begin
	declare i_id int(6);
	declare o_price decimal(10,2);
	declare quant int(3);
	declare pri int(10);
    
	select Item_ID into i_id from order_list where Order_num = O_Num;
	select Quantity into quant from order_list where Order_num = O_Num;
	select Price into pri from inventory where inventory.Item_id = i_id;
	set o_price = quant * pri;
return o_price;
end //

delimiter ;