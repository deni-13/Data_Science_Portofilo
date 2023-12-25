--siparisleri toplam listele sehre gore


select * from ORDERS O
select ct.CITY,SUM(o.TOTALPRICE) toplam_Fiyat from ORDERS o
join ADDRESS a on a.ID=o.ADDRESSID
join CITIES ct on ct.ID=a.CITYID -- cities joinlendi

GROUP BY ct.CITY
order by 2 desc 

-- al�st�rma 2: kategorilere gore siparis daglimi

select 
I.CATEGORY1,I.CATEGORY2,SUM(O.LINETOTAL)AS TOPLAM_S�PAR�S -- S�PARIS TOPLAMI

from ITEMS I
join ORDERDETAILS o  on  O.ITEMID = I.ID 
-- items + order details baglandi

GROUP BY I.CATEGORY1,CATEGORY2
ORDER BY I.CATEGORY1,CATEGORY2,SUM(O.LINETOTAL) desc


select * from ORDERDETAILS -- �TEM �DLER VAR


-- al�st�rma 3: musterilere gore sip dag�l�m�
select * from users u
select * from orders  o


select U.ID,U.NAMESURNAME,SUM(O.TOTALPRICE) TOTAL_SALE,
count(O.ID) ORDER_COUNT
from USERS U
join ORDERS O ON O.USERID=U.ID

GROUP BY U.ID,U.NAMESURNAME
order by TOTAL_SALE desc