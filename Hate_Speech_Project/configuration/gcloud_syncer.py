import os
import subprocess
import logging

class GCloudSync:
    
    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):
        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        logging.info(f"Executing command: {command}")

        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            logging.info(f"Command output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error occurred while syncing to GCloud: {e.stderr}")
            raise

    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
        # Ensure destination directory exists
        os.makedirs(destination, exist_ok=True)

        # Construct the destination file path with double quotes
        destination_file_path = os.path.join(destination, filename)  # Full path for the file
        destination_file_path_quoted = f'"{destination_file_path}"'  # Quoted for command

        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination_file_path_quoted}"
        logging.info(f"Executing command: {command}")

        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            logging.info(f"Command output: {result.stdout}")

            # Verify that the file was downloaded
            if os.path.exists(destination_file_path):
                logging.info(f"Successfully downloaded file to: {destination_file_path}")
            else:
                logging.error(f"Downloaded file not found at: {destination_file_path}")
                raise FileNotFoundError(f"Downloaded file not found at: {destination_file_path}")
                
        except subprocess.CalledProcessError as e:
            logging.error(f"Error occurred while syncing from GCloud: {e.stderr}")
            raise

