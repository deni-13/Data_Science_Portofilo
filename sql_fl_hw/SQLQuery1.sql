/*
CREATE TABLE FLO2 (
	master_id							VARCHAR(50),
	order_channel						VARCHAR(50),
	last_order_channel					VARCHAR(50),
	first_order_date					DATE,
	last_order_date						DATE,
	last_order_date_online				DATE,
	last_order_date_offline				DATE,
	order_num_total_ever_online			INT,
	order_num_total_ever_offline		INT,
	customer_value_total_ever_offline	FLOAT,
	customer_value_total_ever_online	FLOAT,
	interested_in_categories_12			VARCHAR(50),
	store_type							VARCHAR(10)
)
*/



select * from FLO2




--2. kac musteri
SELECT  count(distinct(master_id)) musteri_sayisi

FROM FLO2
--group by master_id


-- deneme :master id ler 
SELECT master_id mus
FROM FLO2


--3. toplam  yapýlan a/v sayýsý
SELECT  SUM(order_num_total_ever_offline+order_num_total_ever_online) AS toplam_Alisveris,
ROUND(SUM(customer_value_total_ever_offline+customer_value_total_ever_online),2) AS toplam_ciro

FROM FLO2


--4 ortalama ciro

select 
ROUND((SUM(customer_value_total_ever_offline+customer_value_total_ever_online)/
SUM(order_num_total_ever_offline+order_num_total_ever_online)
),2)
from 
FLO2;

--5
select  ROUND(SUM(customer_value_total_ever_offline+customer_value_total_ever_online),2) AS toplam_ciro,
SUM(order_num_total_ever_offline+order_num_total_ever_online) AS toplam_Alisveris,last_order_channel


from FLO2

group by last_order_channel



--6


select store_type,ROUND(SUM(customer_value_total_ever_offline+customer_value_total_ever_online),2) 
toplam_ciro


FROM FLO2
GROUP BY store_type

/*
SELECT Value,SUM(TOPLAM_CIRO/COUNT_) 
FROM
(
SELECT store_type MAGAZATURU,(SELECT COUNT(VALUE) FROM  string_split(store_type,',') ) COUNT_,
       ROUND(SUM(customer_value_total_ever_offline + customer_value_total_ever_online), 2) TOPLAM_CIRO 
FROM FLO 
GROUP BY store_type) T
CROSS APPLY (SELECT  VALUE  FROM  string_split(T.MAGAZATURU,',') ) D
GROUP BY Value

*/


--7
SELECT YEAR(first_order_date) yýl, SUM(order_num_total_ever_offline+order_num_total_ever_online) AS toplam_Alisveris


FROM FLO2
GROUP BY YEAR(first_order_date)
order by 1 desc





--8

SELECT last_order_channel,ROUND((SUM(customer_value_total_ever_offline+customer_value_total_ever_online)/
SUM(order_num_total_ever_offline+order_num_total_ever_online)
),2) AS ORTALAMA_CIRO


FROM  FLO2

GROUP BY last_order_channel -- son alisveris gunleri  tekillesti.

--subquery --->
/*
SELECT 
last_order_channel KANAL, 
ROUND(TOPLAM_CIRO / TOPLAM_SIPARIS_SAYISI,2) AS ALISVERIS_BAS_ORT
FROM
(
SELECT 
	last_order_channel,
	ROUND(SUM(customer_value_total_ever_offline + customer_value_total_ever_online),2) TOPLAM_CIRO,
	SUM(order_num_total_ever_offline + order_num_total_ever_online) TOPLAM_SIPARIS_SAYISI
FROM FLO2
GROUP BY last_order_channel
) T
*/


--9 --en son alisveris 
SELECT interested_in_categories_12,COUNT(*) FRQ
FROM FLO2
GROUP BY  interested_in_categories_12
ORDER BY 2 desc



--10 AGGREGATION
SELECT TOP 1
(store_type),count(*) frq

FROM FLO2
GROUP BY store_type
ORDER BY 2 desc


--11 subquery !
SELECT last_order_channel, T1.interested_in_categories_12, SUM(order_num_total_ever_online + order_num_total_ever_offline)
FROM FLO2 T2 
INNER JOIN 
(
	SELECT top 1 interested_in_categories_12
	FROM FLO2
	group by interested_in_categories_12
	order by 
	SUM(order_num_total_ever_online+order_num_total_ever_offline) desc
) T1
ON T1.interested_in_categories_12 = T2.interested_in_categories_12
GROUP BY T1.interested_in_categories_12, last_order_channel



--12
SELECT TOP 1 (master_id)
FROM 
FLO2
GROUP BY master_id 
ORDER BY SUM(customer_value_total_ever_offline + customer_value_total_ever_online)  DESC 


--13
SELECT 
	D.master_id, 
	ROUND((D.top_ciro / D.siparis),2) sip_ortalama,
	ROUND((DATEDIFF(DAY, first_order_date, last_order_date)/D.siparis),1) 
FROM
(
	SELECT TOP 1 master_id, first_order_date, last_order_date,
			   SUM(customer_value_total_ever_offline + customer_value_total_ever_online) top_ciro,
			   SUM(order_num_total_ever_offline + order_num_total_ever_online) siparis
		FROM FLO2 
		GROUP BY master_id, first_order_date, last_order_date
	ORDER BY top_ciro DESC
) D



--select * from FLO2 where master_id='cc294636-19f0-11eb-8d74-000d3a38a36f'

--14  !!
SELECT TOP 100 (master_id),datediff(day,first_order_date,last_order_date) --avg
FROM 
FLO2
GROUP BY master_id,datediff(day,first_order_date,last_order_date)
ORDER BY SUM(customer_value_total_ever_offline + customer_value_total_ever_online)  DESC 


--15 !!!
SELECT DISTINCT last_order_channel,
(
	SELECT TOP 1 master_id
	FROM FLO2
	WHERE last_order_channel=f.last_order_channel
	GROUP BY master_id
	ORDER BY SUM(customer_value_total_ever_offline+customer_value_total_ever_online) DESC 
) EN_COK_ALISVERIS_YAPAN_MUSTERI,
(
	SELECT TOP 1 SUM(customer_value_total_ever_offline+customer_value_total_ever_online)
	FROM FLO2  WHERE last_order_channel=f.last_order_channel
	GROUP BY master_id
	ORDER BY SUM(customer_value_total_ever_offline+customer_value_total_ever_online) DESC 
) CIRO
FROM FLO2 F

--Msg 144, Level 15, State 1, Line 135
--Cannot use an aggregate or a subquery in an expression used for the group by list of a GROUP BY clause.

--meali : groupby'da aggregation yok!
,
--16


SELECT master_id, last_order_date 
FROM FLO2
WHERE last_order_date=(SELECT MAX(last_order_date) FROM FLO2)
