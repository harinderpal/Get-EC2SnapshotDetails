import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2Resource = boto3.resource("ec2")  
    now = datetime.now()
    snapshots = ec2Resource.snapshots.all()
    for snapshot in snapshots:
        if snapshot.volume_id != "vol-ffffffff":
            creationdate = (str(snapshot.start_time).split())[0]
            print("snapshot id :" + snapshot.id + ", Size : " + snapshot.volume_size + ", Description: " + snapshot.description + ", Creation time: " + creationdate + " Age(in days): " + (now - (datetime.strptime(creationdate,'%Y-%m-%d'))).days +  " VolumeID: " + snapshot.volume_id + " State: " + snapshot.state + ", Encrypted: " + snapshot.encrypted + " Owner Alias: " + snapshot.owner_alias + ", Owner ID: " +  snapshot.owner_id)
  
