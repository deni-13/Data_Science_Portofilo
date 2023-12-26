SELECT * 
FROM customers


-- 2. Customers tablosundan adý ‘A’ harfi ile baþlayan kiþileri çeken sorguyu yazýnýz.


SELECT CUSTOMERNAME

FROM customers where CUSTOMERNAME LIKE 'A%'


-- 3. 1990 ve 1995 yýllarý arasýnda doðan müþterileri çekiniz. 1990 ve 1995 yýllarý dahildir.

SELECT CUSTOMERNAME

FROM customers

WHERE YEAR(BIRTHDATE) 
BETWEEN 1990 AND 1995


--4. Ýstanbul’da yaþayan kiþileri Join kullanarak getiren sorguyu yazýnýz.

SELECT * 


FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id -- birlesmis hal

--2
SELECT  c.CUSTOMERNAME,ct.city


FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id
where ct.city='ÝSTANBUL'


--5 Ýstanbul’da yaþayan kiþileri subquery kullanarak getiren sorguyu yazýnýz.


SELECT CUSTOMERNAME
FROM customers
WHERE CITY_ID IN (SELECT id FROM cities WHERE city = 'ÝSTANBUL') -- alt sorgu : cities table


--6  Hangi þehirde kaç müþterimizin olduðu bilgisini getiren sorguyu yazýnýz.


SELECT  ct.city,count(*)


FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id
GROUP BY ct.city

--7 10’dan fazla müþterimiz olan þehirleri müþteri sayýsý ile birlikte müþteri sayýsýna göre fazladan aza doðru sýralý þekilde getiriniz

SELECT  ct.city,count(*) sayilar

FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id
GROUP BY ct.city 
having  count(*) >10
order by 2 desc

--8 Hangi þehirde kaç erkek, kaç kadýn müþterimizin olduðu bilgisini getiren sorguyu yazýnýz

SELECT * from cities

SELECT * 
FROM customers


--joinleme

select ct.city,c.GENDER,count(*) as musteri_sayisi

from 
customers c
JOIN cities ct on  c.CITY_ID=ct.id
group by ct.city,c.GENDER
order by 1


--alternatif
 
 SELECT 
    ct.city,
    SUM(CASE WHEN c.GENDER = 'E' THEN 1 ELSE 0 END) AS ERKEK,
    SUM(CASE WHEN c.GENDER = 'K' THEN 1 ELSE 0 END) AS KADIN
FROM 
    customers c
JOIN 
    cities ct ON c.CITY_ID = ct.id
GROUP BY 
    ct.city;

--9 Customers tablosuna yaþ grubu için yeni bir alan ekleyiniz. Bu iþlemi hem management studio ile hem de sql kodu ile yapýnýz. Alaný adý AGEGROUP veritipi Varchar(50)

ALTER TABLE customers ADD  AGEGROUP VARCHAR(50);

SELECT * 
FROM customers

--10 Customers tablosuna eklediðiniz AGEGROUP alanýný 20-35 yaþ arasý,36-45 yaþ arasý,46-55 yaþ arasý,55-65 yaþ arasý ve 65 yaþ üstü olarak güncelleyiniz
select DATEDIFF(year, BIRTHDATE, GETDATE()) as age
from customers

UPDATE customers
set AGEGROUP=
	case 
	when  DATEDIFF(year, BIRTHDATE, GETDATE()) BETWEEN 25 AND 35 THEN '20-35'
	when  DATEDIFF(year, BIRTHDATE, GETDATE()) BETWEEN 36 AND 45  THEN '36-45'
	when  DATEDIFF(year, BIRTHDATE, GETDATE()) BETWEEN 46 AND 55  THEN '46-55 '
	when  DATEDIFF(year, BIRTHDATE, GETDATE()) BETWEEN 56 AND 65 THEN  '56-65 '
	else '65+'
	end;

-- 11. Ýstanbul’da yaþayýp ilçesi ‘Kadýköy’ dýþýnda olanlarý listeleyiniz.

SELECT c.CUSTOMERNAME,dt.distr

FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id 
JOIN district dt on ct.id=dt.cityid 
where  ct.city='Ýstanbul' and  distr!='Kadýköy'


select * from district

-- 12 . Müþterilerimizin telefon numalarýnýn operatör bilgisini getirmek istiyoruz. TELNR1 ve TELNR2 alanlarýnýn yanýna
--operatör numarasýný (532),(505) gibi getirmek istiyoruz. Bu sorgu için gereken SQL cümlesini yazýnýz.

ALTER TABLE customers ADD Operator1 VARCHAR(50);
ALTER TABLE customers ADD Operator2 VARCHAR(50);

UPDATE customers
SET Operator1 = SUBSTRING(TELN1, 2, CHARINDEX(')', TELN1) - 2),
    Operator2 = SUBSTRING(TELN2, 2, CHARINDEX(')', TELN2) - 2);

SELECT * FROM customers;

--13. Müþterilerimizin telefon numaralarýnýn operatör bilgisini getirmek istiyoruz. Örneðin telefon numaralarý “50”
--ya da “55” ile baþlayan “X” operatörü “54” ile baþlayan “Y” operatörü “53” ile baþlayan “Z” operatörü olsun.
--Burada hangi operatörden ne kadar müþterimiz olduðu bilgisini getirecek sorguyu yazýnýz.



ALTER TABLE customers ADD HANE VARCHAR(50);
UPDATE customers
   set HANE=
    LEFT(Operator1, 2) 


ALTER TABLE customers ADD HANE2 VARCHAR(50);
UPDATE customers
   set HANE2=
    LEFT(Operator2, 2) 





SELECT
  CASE 
    WHEN LEFT(Operator1, 2) IN ('50', '55') THEN 'X'
    WHEN LEFT(Operator1, 2) = '54' THEN 'Y'
    WHEN LEFT(Operator1, 2) = '53' THEN 'Z'
  END AS OPERATOR_NAME
FROM customers;



-- 14. Her ilde en çok müþteriye sahip olduðumuz ilçeleri müþteri sayýsýna göre çoktan aza doðru sýralý þekilde þekildeki gibi getirmek için gereken sorguyu yazýnýz.
/*
SELECT dt.distr,count(*) as sayi
FROM customers c 
join cities ct  on c.CITY_ID=ct.id
JOIN district dt on ct.id=dt.cityid 
group by ct.id,dt.distr
order by 2 desc

select * from district
--deneme
SELECT *
FROM customers c 
join cities ct  on c.CITY_ID=ct.id
JOIN district dt on ct.id=dt.cityid 

*/ 
