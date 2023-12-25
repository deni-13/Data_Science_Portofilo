--alistirma 3: belli cironun ustunde satýs yapan magazalari getir

select

CITY,SUM(TOTALPRICE) TOTALSALE
from SALES

GROUP BY CITY

order by 2 desc

-- 100000 den fazla olani getir
select

CITY,SUM(TOTALPRICE) TOTALSALE
from SALES
where TOTALPRICE>100000  -- tek seferli yuzbin


GROUP BY CITY

order by 2 desc --calismadi burasi,istedigimiz deil

--not!! : aggregation kosulunda having gelir
select

CITY,SUM(TOTALPRICE) TOTALSALE
from SALES
GROUP BY CITY
having sum(TOTALPRICE) >100000
order by 2 desc
--butun illerin satýs fiyati 10000den buyuk olani getir

--alistirma 4:aylara gore satis
--TURKCE YAPALIM 
SELECT * 
FROM SALES

set language turkish
SELECT CITY,
--DATEPART(MONTH,DATE_) AS MONTHNUM,
DATENAME(MONTH,DATE_) AS MONTHNAME_,
SUM(TOTALPRICE) AS TOTALSALE
FROM SALES
GROUP BY CITY,DATEPART(MONTH,DATE_),
DATENAME(MONTH,DATE_)
--ORDER BY 1,2
ORDER BY CITY,DATEPART(MONTH,DATE_)

-- buda alpabetic geldi


--DATENAME KULLANIMI

SELECT DATENAME(MONTH,'2019-07-12 12:00:00')
