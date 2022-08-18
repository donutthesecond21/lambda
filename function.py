import json
import boto3
import paramiko
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # downloading pem filr from S3
    s3.download_file("rezise", "migi.pem", "/tmp/file.pem")
    # reading pem file and creating key object
    key = paramiko.RSAKey.from_private_key_file("/tmp/file.pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    host = "54.167.189.214"
    print("Connecting to : " + host)
    client.connect(hostname=host, username="ubuntu", pkey=key)
    print("Connected to :" + host)
    bash = ["bash cash.sh"]
    for b in bash:
        print(f"Executing {b}")
        stdin, stdout, stderr = client.exec_command(b)
        print(stdout.read())
        print(stderr.read())
    client.close()
    return "client closed and done properly"
