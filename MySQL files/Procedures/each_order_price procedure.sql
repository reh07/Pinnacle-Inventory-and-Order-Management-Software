delimiter //
create procedure each_order_price(in order_no int(8))
begin
	declare final decimal(10,2);
    	set final = order_price(order_no);
    	select final;
end //
delimiter ;