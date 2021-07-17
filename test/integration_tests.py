# Databricks notebook source
import unittest
import numpy as np
import pandas as pd
from generic_library.code import ExampleClass, example_func

random_seed = 42
np.random.seed(random_seed)

#uncomment if you need pyspark:

#import findspark
#findspark.init()
#from pyspark import SparkContext
#from pyspark.sql import SparkSession, SQLContext
#import pyspark.sql.functions as F

#spark_url = "local[*]"
#app_name = "test lib"
#sc = SparkContext(appName=app_name)
#spark = SparkSession.builder.appName(app_name).master(spark_url).getOrCreate()
#sqlContext = SQLContext(sc)


class IntegrationTest(unittest.TestCase):
    """Test processing functions."""

    def setUp(self):
        pass

    def test_evaluator(self):
        pass


if __name__ in "__main__":
    unittest.main()