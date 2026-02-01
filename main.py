
from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
except Exception as e:
    logger.exception(e)
    raise e


