# End-to-End Hate Speech Classification Project using LSTM

This repository contains the code for a complete end-to-end hate speech classification project, built using Python and deploying to AWS. This project demonstrates best practices for building robust and deployable NLP pipelines.

## Project Overview

The goal of this project is to build a model capable of classifying text as hate speech or not hate speech. We leverage an LSTM (Long Short-Term Memory) network, a type of recurrent neural network (RNN), well-suited for sequential data like text. The project is structured in a modular fashion, making it easy to understand, maintain, and extend.

## Project Structure

The project is organized into several key components:

* **`constants.py`**: Defines project-wide constants and configuration parameters.
* **`config/`**: Contains configuration files (e.g., GCP or AWS credentials - these should *not* be committed to the repository).
* **`components/`**:  Houses the core components of the pipeline:
    * `data_ingestion.py`: Downloads data from a cloud storage bucket (originally GCP, modified to AWS in this deployment).
    * `data_transformation.py`: Preprocesses and transforms the raw data (cleaning, handling imbalances, feature engineering).
    * `model_trainer.py`: Trains the LSTM model and saves the trained model and tokenizer.
    * `model_evaluation.py`: Evaluates the trained model and determines whether to deploy the new model.
    * `model_pusher.py`: Uploads the trained model to AWS S3.
* **`entity/`**: Defines data structures for configuration and artifacts.
* **`exceptions.py`**: Custom exception classes for better error handling.
* **`logger.py`**: Custom logging functionality for tracking the pipeline's progress.
* **`pipeline/`**: Contains pipeline orchestration scripts:
    * `training_pipeline.py`: Runs the training pipeline.
    * `prediction_pipeline.py`: Runs the prediction pipeline.
* **`ml/`**: Contains model architecture definition.
    * `model.py`: Defines the LSTM model architecture.
* **`app.py`**: FastAPI application for making predictions via a simple web interface.
* **`notebook/`**: Jupyter Notebook used for initial experimentation and data exploration.
* **`.circleci/`**: Contains the CircleCI configuration for continuous integration and deployment.
    * `config.yml`: CircleCI configuration file.
* **`Dockerfile`**: Dockerfile for building the application image.
* **`requirements.txt`**: Project dependencies.
* **`setup.py`**: Setup file for installing local packages.

## Setup

1. **Install Dependencies:**  Create a virtual environment and install the required packages listed in `requirements.txt`.
2. **AWS Configuration:**  Configure your AWS credentials (access key ID and secret access key) as environment variables.  **Do not** hardcode these in your code.
3. **CircleCI Setup:**
    * Create a CircleCI account and connect it to your GitHub repository.
    * Configure a self-hosted runner on an AWS EC2 instance.  Instructions are provided in the README.
    * Configure the CircleCI project with the necessary environment variables (AWS credentials, ECR repository details).  The `config.yml` file provides a template.
4. **Data:** Download the dataset.  It is recommended to upload your data to an AWS S3 bucket.  Update the relevant paths in the configuration files to reflect this.

## Running the Project

1. **Training:** Run `python app.py` with the `train` endpoint to train the model. The training process is logged to the console and files are saved to the project's `artifacts` directory.  This will also deploy the model to AWS S3 if it performs better than the existing model.
2. **Prediction:** Run `python app.py` and use the prediction endpoint (default route) to make predictions with your own text input.

## Deployment (CircleCI)

Commit your code changes to GitHub. This will trigger the CircleCI pipeline, which will build a Docker image, push it to AWS ECR, and deploy it to AWS EC2.

## License

[MIT License]
