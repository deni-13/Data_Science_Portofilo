SELECT * 
FROM customers


-- 2. Customers tablosundan ad� �A� harfi ile ba�layan ki�ileri �eken sorguyu yaz�n�z.


SELECT CUSTOMERNAME

FROM customers where CUSTOMERNAME LIKE 'A%'


-- 3. 1990 ve 1995 y�llar� aras�nda do�an m��terileri �ekiniz. 1990 ve 1995 y�llar� dahildir.

SELECT CUSTOMERNAME

FROM customers

WHERE YEAR(BIRTHDATE) 
BETWEEN 1990 AND 1995


--4. �stanbul�da ya�ayan ki�ileri Join kullanarak getiren sorguyu yaz�n�z.

SELECT * 


FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id -- birlesmis hal

--2
SELECT  c.CUSTOMERNAME,ct.city


FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id
where ct.city='�STANBUL'


--5 �stanbul�da ya�ayan ki�ileri subquery kullanarak getiren sorguyu yaz�n�z.


SELECT CUSTOMERNAME
FROM customers
WHERE CITY_ID IN (SELECT id FROM cities WHERE city = '�STANBUL') -- alt sorgu : cities table


--6  Hangi �ehirde ka� m��terimizin oldu�u bilgisini getiren sorguyu yaz�n�z.


SELECT  ct.city,count(*)


FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id
GROUP BY ct.city

--7 10�dan fazla m��terimiz olan �ehirleri m��teri say�s� ile birlikte m��teri say�s�na g�re fazladan aza do�ru s�ral� �ekilde getiriniz

SELECT  ct.city,count(*) sayilar

FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id
GROUP BY ct.city 
having  count(*) >10
order by 2 desc

--8 Hangi �ehirde ka� erkek, ka� kad�n m��terimizin oldu�u bilgisini getiren sorguyu yaz�n�z

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

--9 Customers tablosuna ya� grubu i�in yeni bir alan ekleyiniz. Bu i�lemi hem management studio ile hem de sql kodu ile yap�n�z. Alan� ad� AGEGROUP veritipi Varchar(50)

ALTER TABLE customers ADD  AGEGROUP VARCHAR(50);

SELECT * 
FROM customers

--10 Customers tablosuna ekledi�iniz AGEGROUP alan�n� 20-35 ya� aras�,36-45 ya� aras�,46-55 ya� aras�,55-65 ya� aras� ve 65 ya� �st� olarak g�ncelleyiniz
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

-- 11. �stanbul�da ya�ay�p il�esi �Kad�k�y� d���nda olanlar� listeleyiniz.

SELECT c.CUSTOMERNAME,dt.distr

FROM customers c 
JOIN cities ct on c.CITY_ID=ct.id 
JOIN district dt on ct.id=dt.cityid 
where  ct.city='�stanbul' and  distr!='Kad�k�y'


select * from district

-- 12 . M��terilerimizin telefon numalar�n�n operat�r bilgisini getirmek istiyoruz. TELNR1 ve TELNR2 alanlar�n�n yan�na
--operat�r numaras�n� (532),(505) gibi getirmek istiyoruz. Bu sorgu i�in gereken SQL c�mlesini yaz�n�z.

ALTER TABLE customers ADD Operator1 VARCHAR(50);
ALTER TABLE customers ADD Operator2 VARCHAR(50);

UPDATE customers
SET Operator1 = SUBSTRING(TELN1, 2, CHARINDEX(')', TELN1) - 2),
    Operator2 = SUBSTRING(TELN2, 2, CHARINDEX(')', TELN2) - 2);

SELECT * FROM customers;

--13. M��terilerimizin telefon numaralar�n�n operat�r bilgisini getirmek istiyoruz. �rne�in telefon numaralar� �50�
--ya da �55� ile ba�layan �X� operat�r� �54� ile ba�layan �Y� operat�r� �53� ile ba�layan �Z� operat�r� olsun.
--Burada hangi operat�rden ne kadar m��terimiz oldu�u bilgisini getirecek sorguyu yaz�n�z.



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



-- 14. Her ilde en �ok m��teriye sahip oldu�umuz il�eleri m��teri say�s�na g�re �oktan aza do�ru s�ral� �ekilde �ekildeki gibi getirmek i�in gereken sorguyu yaz�n�z.
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
