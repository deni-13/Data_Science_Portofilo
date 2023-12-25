select * from customers

-- delete from customers  --:dersem hepsini silecek

 --truncate table customers

 update customers set COUNTRY='turkiye',AGE=DATEDIFF(YEAR,BIRTHDATE,GETDATE())

 SELECT * FROM customers
WHERE GENDER='K'


 SELECT * FROM customers
WHERE GENDER<>'K'



 SELECT * FROM customers
WHERE id<50

 SELECT * FROM customers
WHERE id>=50

 SELECT * FROM customers
WHERE id between 100 and 200 -- 200 ve 100 arasi


-- baslama

 SELECT * FROM customers
WHERE NAMESURNAME like 'Ali%'  
-- bitme
 SELECT * FROM customers
WHERE NAMESURNAME like '%ÇE' 


-- içerme

 SELECT * FROM customers
WHERE NAMESURNAME like '%ÇE%' 


 SELECT * FROM customers
WHERE CITY in ('30','34') 

 SELECT * FROM customers
WHERE CITY not in ('38','34') 

-- sehri istanbul yas 30

-- and 
select * from customers where CITY='30' and AGE>25 and GENDER='K'

-- or operatoru

select * from customers where CITY='34' or AGE>25 



select * from customers where CITY='34' and (AGE>30 or GENDER='K')
-- 34 olan oncelikli!
-- delete/update from with where

update customers set AGE_GROUP ='GENÇ' where age between 20 and 40


update customers set AGE_GROUP ='ORTA' where age between 41 and 55


update customers set AGE_GROUP ='YAÞLI' where age>50

--DELETE KULLANIMI

DELETE FROM customers where id =1
--distinct


select	CITY FROM customers

select	distinct CITY FROM customers  -- her bir sehrin ne kadar bulundugu

select	 CITY,TOWN FROM customers WHERE CITY='40' -- 40 olan yerin sehir kodlari
select distinct	 CITY,TOWN FROM customers WHERE CITY='40' -- 40 olan yerin sehir kodlari tekillenmis



-- order by

select * from customers order by NAMESURNAME asc
-- asc yazip yazmamak onemli egil default asc zaten



--top 


select top 20 * from customers order by GENDER 

-- % sel olarak


select top  25 PERCENT * from customers order by age


