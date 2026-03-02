# dlt_workshop
1. 2009-06-01 to 2009-07-01
SELECT
  min(trip_pickup_date_time)
  , max(trip_dropoff_date_time)
FROM "taxi_data"
LIMIT 1000

2. 26.66%
SELECT
  sum(if(payment_type = 'Credit',1,0))/count(*)
FROM "taxi_data"
LIMIT 1000

3. $6,063.41
SELECT
  sum(tip_amt)
FROM "taxi_data"
LIMIT 1000