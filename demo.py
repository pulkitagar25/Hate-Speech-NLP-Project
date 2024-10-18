from Hate_Speech_Project.logger import logging
from Hate_Speech_Project.exception import CustomException
import sys
from Hate_Speech_Project.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-speech-project-2024", "dataset.zip", "download/dataset.zip")



