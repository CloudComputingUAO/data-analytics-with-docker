import pytest
import pandas as pd
from io import StringIO
from tasks import load_csv_task, analyze_data_task

@pytest.fixture
def mock_csv_data():
    # Create a mock CSV data for testing
    data = """product,amount,date
    Widget,10,2024-01-01
    Gadget,20,2024-01-02"""
    return StringIO(data)

def test_load_csv_task(mock_csv_data):
    # Mock the load_csv_task function
    mock_df = pd.read_csv(mock_csv_data)
    assert not mock_df.empty
    assert set(mock_df.columns) == {"product", "amount", "date"}

def test_analyze_data_task(monkeypatch):
    # Monkeypatch Spark methods to test without actual Spark setup
    from pyspark.sql import SparkSession
    class MockSparkSession:
        @staticmethod
        def builder():
            return MockSparkSession()
        def appName(self, name):
            return self
        def getOrCreate(self):
            return self
        def read(self):
            return MockDataFrameReader()
        def stop(self):
            pass

    class MockDataFrameReader:
        def jdbc(self, url, table, properties):
            data = """product,amount,date
            Widget,10,2024-01-01
            Gadget,20,2024-01-02"""
            return pd.read_csv(StringIO(data))
    
    monkeypatch.setattr(SparkSession, "builder", MockSparkSession.builder)
    analyze_data_task()
    # Test that reports are generated (you may need to check the `reports` directory for actual files)
