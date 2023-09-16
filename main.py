import zipfile
import pandas as pd
import streamlit as st


# Downloading dataset using Kaggle API

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_file("arshkon/linkedin-job-postings", file_name="job_postings.csv")

# Unzip the dataset downloaded from kaggle

with zipfile.ZipFile("job_postings.csv.zip", "r") as zipref:
    zipref.extractall()

# Creating the streamlit web app using the kaggle dataset

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title("LinkedIn Jobs Analytics")
    st.text("Interactive analysis of jobs posting data from LinkedIn")

with dataset:
    st.title("2023 LinkedIn Jobs Posting dataset")
    st.text(
        'The dataset was derived from kaggle as contributed by user named "arshkon"'
    )

    jobs_data = pd.read_csv("job_postings.csv")
    st.write(jobs_data.head(5))

    st.subheader("Jobs ID distribution on the LinkedIn Jobs dataset")
    minsalary_dist = pd.DataFrame(jobs_data["min_salary"].value_counts()).head(50)
    st.bar_chart(minsalary_dist)


with features:
    st.header(
        "This section showcases an depth analytics and features of the jobs posting data"
    )

with model_training:
    st.header("This section trains our data model")
    st.text(
        "This section allows you to choose hyperparameters of the model and see performance changes:"
    )
