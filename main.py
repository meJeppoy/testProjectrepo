import pandas as pd
import numpy as np
import streamlit
import kaggle
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_file("arshkon/linkedin-job-postings", file_name="job_postings.csv")

# Unzip the dataset downloaded from kaggle
with zipfile.ZipFile("job_postings.csv.zip", "r") as zipref:
    zipref.extractall()
