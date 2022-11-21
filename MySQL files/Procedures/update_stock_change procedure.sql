delimiter //
create procedure update_stock_change(in o_num integer(8), itemid integer(6))
begin
		declare quant integer(5) default 0;
        declare stock integer(5) default 0;
        declare remaining integer(5) default 0;
        
        select Quantity into quant from order_list where Order_NUm = o_num;
        select Stock_Quantity into stock from inventory where Item_ID = itemid;
        
        set remaining = stock - quant;
        update inventory set Stock_Quantity = remaining where Item_ID = itemid;
end //

delimiter ;