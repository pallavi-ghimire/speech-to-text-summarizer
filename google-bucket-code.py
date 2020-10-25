import google.cloud
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "fyp_project_bucket"
    # source_file_name = "resources/covid19.flac"
    # destination_blob_name = "covid19.flac"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

upload_blob("fyp_project_bucket", "resources/covid19.flac", "covid19")
