from google.cloud import storage

def upload_to_gcs(
    bucket_name: str, source_file_path: str, destination_blob_name: str
) -> str:
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_path)
    gcs_uri = f"gs://{bucket_name}/{destination_blob_name}"
    print(f"File uploaded to GCS: {gcs_uri}")
    return gcs_uri
