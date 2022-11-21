delimiter //
create procedure total_payment(in id integer(5))
begin
	declare final_amt decimal(10,2) default 0;
    select sum(Order_price) into final_amt from order_list where Order_ID = id;
    select final_amt;
    update orders set Payment_amt = final_amt where Order_ID = id;
end //
delimiter ;