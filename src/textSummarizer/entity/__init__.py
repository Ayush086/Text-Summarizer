from dataclasses import dataclass
from pathlib import Path

# decorator ensures that it's umimmutable (once created then it can't be changed/modified)
@dataclass(frozen=True)
class DataIngestionConfig:
    """Data ingestion configuration class."""
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """Data Validation configuration class."""
    root_dir: Path          # root directory where validation is performed
    STATUS_FILE: str        # path to the file where validation status will be written
    ALL_REQUIRED_FILES: list  # list of required files to check for existence
