import boto3

s3 = boto3.client('s3')

try:
    bn = 'vgv.ftptest'
    response = s3.create_bucket(Bucket=bn)
    print('Bucket ' + bn + ' created successfully')

    fn = 'testfile.jpg'
    with open(fn, 'rb') as data:
        s3.upload_fileobj(data, bn, fn)
    print('File ' + fn + ' uploaded successfully' + ' to bucket ' + bn)

    with open(fn, 'wb') as data:
        s3.download_fileobj(bn, fn, data)
    print('File ' + fn + ' downloaded successfully' + ' from bucket ' + bn)

    print('Deleting ' + fn + ' from ' + bn)
    response = s3.delete_object(Bucket=bn, Key=fn)
    print(response)

except:
    print("Error:" + sys.exc_info()[0])
