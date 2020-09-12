URL = ""


def go(request):
    import os
    import tempfile
    import json
    import base64
    from datetime import datetime
    from google.cloud import storage
    import requests

    # Get the latest data from the sensor
    r = requests.get(url=URL)
    data = r.json()

    # initialize Google Cloud Storage
    storage_client = storage.Client()
    _, temp_local_filename = tempfile.mkstemp()

    # let's save it to temp Google Storage
    with open(temp_local_filename, "w") as tmp_file:
        tmp_file.write(json.dumps(data))

    # upload it
    filename_image = str(datetime.now())+'.json'
    blur_bucket = storage_client.bucket('airquality_111')
    new_blob = blur_bucket.blob(filename_image)
    new_blob.upload_from_filename(temp_local_filename)

    # Show the results
    data_json = json.loads(open(temp_local_filename, 'rb').read())

    # Delete the temporary file.
    os.remove(temp_local_filename)

    return json.dumps(data_json)
