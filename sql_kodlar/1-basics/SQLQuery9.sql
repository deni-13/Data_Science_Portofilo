--AL�ST�RMA 5

SELECT  
ITEMCODE,ITEMNAME,CATEGORY1,CATEGORY2,
SUM(AMOUNT) TOTALAMO,SUM(TOTALPRICE) TOTALSALE,
MIN(DATE_) FIRST_SALE,
MAX(DATE_) LAST_DATE,
MIN(PRICE) MINFIYAT,MAX(PRICE) MAXIMUMPRICE,AVG(PRICE) AVGPRICE
FROM SALES
GROUP BY ITEMCODE,ITEMNAME,CATEGORY1,CATEGORY2

--ALISTIRMA 6


SELECT CITY,COUNT(CUSTOMERCODE)

FROM SALES
WHERE CITY='YALOVA'
GROUP BY CITY
-- Msg 8120, Level 16, State 1, Line 15
--Column 'SALES.CITY' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.
--YAN� COUNT VARSA GROUPBY LAZIM


select *
FROM SALES
WHERE CITY='YALOVA'
--B�R MUTSER� BIRDEN FAZLA KEZ VAR

SELECT DISTINCT CUSTOMERCODE,CUSTOMERNAME
FROM SALES 
WHERE CITY='YALOVA'


SELECT CITY,COUNT( DISTINCT CUSTOMERCODE)

FROM SALES
GROUP BY CITY