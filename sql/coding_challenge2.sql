--Query 1
DECLARE @StartOfYear datetime
DECLARE @EndOfYear datetime
SELECT @StartOfYear = dateadd(yy, datediff(yy, 0, getdate()), 0),
 @EndOfYear = dateadd(yy, datediff(yy, 0, getdate()) + 1, -1);

with cte as (
      select dateadd(day, 1 - day(@StartOfYear), @StartOfYear) as som,
             eomonth(@StartOfYear) as eom
      union all
      select dateadd(month, 1, som), eomonth(dateadd(month, 1, som))
      from cte
      where dateadd(month, 1, som) < @EndOfYear
     )
select month(eom) as month_with_30_days
from cte
where day(eom) = 30;

--Query 2
DECLARE  @MaxDate DATE, 
         @MinDate DATE, 
         @iDate  DATE 
-- SQL Server table variable 
DECLARE  @DateSequence TABLE( 
                          DATE DATE 
                          ) 
SELECT @MaxDate = Convert(DATE,Max(dateDay)), 
       @MinDate = Convert(DATE,Min(dateDay)) 
FROM   tblDimDate

SET @iDate = @MinDate 

WHILE (@iDate <= @MaxDate) 
  BEGIN 
    INSERT @DateSequence
    SELECT @iDate 
     
    SET @iDate = Convert(DATE,Dateadd(DAY,1,@iDate)) 
  END 

SELECT Gaps = DATE 
FROM   @DateSequence
EXCEPT 
SELECT DISTINCT Convert(DATE,dateDay) 
FROM   tblDimDate
GO

--Query 3

SELECT ord.id, ord.dateStart
FROM tblOrder ord
WHERE MONTH(ord.dateStart) = 11 AND NOT EXISTS
(SELECT *
   FROM  tblAdvertiserLineItem adv
   WHERE ord.id = adv.idOrder)

--Query 4
SELECT campaign_duration, COUNT(campaign_duration) as number_of_campaigns
FROM (
SELECT ord.id as id_order, datediff(dd, ord.dateStart, ord.dateEnd) as "campaign_duration"
FROM tblOrder ord 
) sub
GROUP BY campaign_duration