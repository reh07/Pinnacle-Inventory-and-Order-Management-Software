insert into inventory values(755101, "Nordstrom Trench Coat", "Coats", 45, 6500);
insert into inventory values(755102, "Nike Puffer", "Jackets", 43, 4000);
insert into inventory values(755103, "Adidas Hoodie", "Jackets", 23, 3000);
insert into inventory values(755104, "Armani Blazer", "Coats", 43, 6000);
insert into inventory values(755105, "Dior Shades", "Accesories", 76, 3000);
insert into inventory values(755106, "Fossil Bracelet", "Accesories", 54, 1500);
insert into inventory values(755107, "Biba Plazzo", "Pants", 23, 1000);
insert into inventory values(755108, "Marks and Spencers Culotte", "Pants", 15, 3600);
insert into inventory values(755109, "Hush Puppies Belt", "Accesories", 56, 1300);
insert into inventory values(755110, "Superdry Bomber Jacket", "Jackets", 34, 9000);


insert into supplier values(1001, "Nordstrom", 755101, "nordstrom@gmail.com", 5046218927);
insert into supplier values(1002,"Nike", 755102,"nike@gmail.com", 8102929388);
insert into supplier values(1003, "Adidas", 755103, "adidas@gmail.com", 8566368749);
insert into supplier values(1004, "Armani", 755104, "armani@gmail.com", 9073854412);
insert into supplier values(1005, "Dior", 755105, "dior@gmail.com", 5135701893);
insert into supplier values(1006, "Fossil", 755106, "fossil@gmail.com", 4195032484);
insert into supplier values(1007, "Biba", 755107, "biba@gmail.com", 7735736914);
insert into supplier values(1008, "Marks and Spencers", 755108, "marksandspencers@gmail.com", 4087523500);
insert into supplier values(1009, "Hush Puppies", 755109, "hushpuppies@gmail.com", 6054142147);
insert into supplier values(1010, "Superdry", 755110, "superdry@gmail.com", 4106558723);


insert into orders values(21001, 678771, null, 6127966008, 'alfonso64@yahoo.com');
insert into orders values(21002, 679763, null, 9740382461, 'sparshagarwalla@gmail.com');
insert into orders values(21003, 789362, null, 9435012626, 'vineeshnayak@gmail.com');
insert into orders values(21004, 539271, null, 9864091624, 'gokulbabu@gmail.com');
insert into orders values(21005, 677382, null, 9706011393, 'mehulmaheshgmail.com');
insert into orders values(21006, 789263, null, 9706011395, 'bibanachdi@gmail.com');
insert into orders values(21007, 876345, null, 9435011393, 'satyajitkumar@gmail.com');

insert into Order_List values(1,21001,755101,4,23123);
insert into Order_List values(2,21001,755102,5,43234);
insert into Order_List values(3,21002,755103,4,23412);
insert into Order_List values(4,21002,755104,6,30212);
insert into Order_List values(5,21003,755105,7,30357);
insert into Order_List values(6,21004,755106,2,30501);
insert into Order_List values(7,21005,755107,7,30646);
insert into Order_List values(8,21005,755108,12,30790);
insert into Order_List values(9,21006,755109,22,30935);
insert into Order_List values(10,21007,755110,4,31079);

insert into supplier_orders values(91110001,1001,755101,12);
insert into supplier_orders values(91110002,1002,755102,11);
insert into supplier_orders values(91110003,1003,755103,8);
insert into supplier_orders values(91110004,1004,755104,21);
insert into supplier_orders values(91110005,1005,755105,17);