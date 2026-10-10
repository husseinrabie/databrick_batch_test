create or refresh streaming table bronz_test as
select
  *,
  current_timestamp() as ingestion_datetime
from
  stream lake_flow_cdc_demo.landing.test_batch;