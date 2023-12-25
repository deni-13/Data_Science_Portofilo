select
PT.PTEXP,
SUM(PAYMENTTOTAL) PAYMENTTOTAL 
FROM PAYMENTS P
JOIN PAYMENT_TYPE PT ON PT.PT_CODE=P.PAYMENTTYPE
GROUP BY PT.PTEXP

--alistirma 6: 81*7 hangi gun ne kadar satýs --SATIS BÝLGÝSÝ+SEHÝR + GUN
SET LANGUAGE turkish
select C.CITY,datepart(DW,O.DATE_) DAYNR ,
datename(DW,O.DATE_) DAYNAME_,SUM(O.TOTALPRICE) TOTAL_PPRICE  from
ORDERS O
JOIN  ADDRESS A  ON A.ID=O.ADDRESSID
JOIN CITIES C ON C.ID=A.CITYID
GROUP BY 
C.CITY,datepart(DW,O.DATE_),datename(DW,O.DATE_)
order BY C.CITY,datepart(DW,O.DATE_)
--order b ve groupby'a alias veremiyoruz

-- dil ve gun !!

SET LANGUAGE turkish

select datepart(DW,'2019-07-15 20:40:41.000') --sali gunu 
select getdate() --7

select datepart(DW, GETDATE()),datename(DW,getdate()) --1  AMA BÝZDE 7

