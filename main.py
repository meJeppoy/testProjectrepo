# from utils import pandas as pd
# from utils import numpy as np
from utils import streamlit
import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_file("arshkon/linkedin-job-postings", file_name="job_postings.csv")
