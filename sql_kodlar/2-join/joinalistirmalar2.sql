-- al�st�rma 4: musterilerin cinsiyetine gore siparis dagilimi

select U.GENDER from orders o
join users u on u.ID = O.USERID



select * from users
--sonuc olarak!!!
select * from ORDERS
select u.GENDER, sum(O.TOTALPRICE) 
from orders O
join users u on u.ID = O.USERID
group by u.GENDER


select *
from users

select * from ORDERS
--sonuc olarak!!!

select u.GENDER, sum(O.TOTALPRICE) 
from orders O
join users u on u.ID = O.USERID
group by u.GENDER


-- e yerine erkek k yerine kad�n
select 
case 
when u.GENDER ='E' THEN 'ERKEK'
when u.GENDER='K' THEN 'KADIN'

END AS GENDER, sum(O.TOTALPRICE) totalsale
from orders O
join users u on u.ID = O.USERID
group by u.GENDER



--al�stirma 5:odeme turune gore siparis dag�l�m�
--joinsiz
select 
CASE WHEN PAYMENTTYPE=1 THEN 'KRED� KARTI'
ELSE 'HAVALE' END AS PAYMENTTYPE

,sum(PAYMENTTOTAL) from PAYMENTS p

GROUP BY(PAYMENTTYPE)


