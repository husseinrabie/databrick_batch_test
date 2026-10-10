from pyspark import pipelines as dp
from pyspark.sql.functions import current_timestamp


@dp.table(
    name="silver_test"
)

def silver_test():
    return(
        spark.readStream
        .table('lake_flow_cdc_demo.landing.test_batch')
        .withColumn('time', current_timestamp())
        .filter('id is not null')
    )

@dp.materialized_view(
    name='gold_test_mv'
)
def gold_test_mv():
    return(
        spark.read
        .table('silver_test')
        .groupBy('id')
        .count()
        )