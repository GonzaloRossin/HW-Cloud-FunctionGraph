from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcce.v3.region.cce_region import CceRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcce.v3 import *

def handler (event, context):
    region = context.getUserData('region', '').strip()
    clusterId = context.getUserData('clusterId', '').strip()
    ak = context.getAccessKey().strip()
    sk = context.getSecretKey().strip()
    logger = context.getLogger()

    if not region:
        raise Exception("'region' not configured")

    if not ak or not sk:
        ak = context.getUserData('ak', '').strip()
        sk = context.getUserData('sk', '').strip()
        if not ak or not sk:
            raise Exception("ak/sk empty")

    credentials = BasicCredentials(ak, sk)
    
    client = CceClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(CceRegion.value_of(region)) \
        .build()

    try:
        request = HibernateClusterRequest()
        request.cluster_id = clusterId
        response = client.hibernate_cluster(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)