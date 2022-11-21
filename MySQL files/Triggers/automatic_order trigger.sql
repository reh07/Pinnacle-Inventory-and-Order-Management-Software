delimiter //
create trigger automatic_order before update on inventory for each row
begin
	declare supplyid int(8) default 9111000;
    declare supplierid int(6) default 0;
    declare quant int(5);
    
    select Supply_ID into supplyid from supplier_orders order by Supply_ID desc limit 1;
    
    set supplyid = supplyid + 1;
    
    
    set quant = 100;
    select Supplier_ID into supplierid from Supplier where Item_ID = new.Item_ID;
    
	
	if new.Stock_Quantity < 10 then
		insert into supplier_orders values(supplyid, supplierid, new.Item_ID, quant);
	end if;
end //

delimiter ;
