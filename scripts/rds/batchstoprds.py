# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkrds.v3.region.rds_region import RdsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkrds.v3 import *


def handler (event, context):
    projectId = context.getUserData('projectId', '').strip()
    region = context.getUserData('region', '').strip()
    ak = context.getAccessKey().strip()
    sk = context.getSecretKey().strip()
    logger = context.getLogger()

    if not projectId:
        raise Exception("'projectId' not configured")

    if not region:
        raise Exception("'region' not configured")

    if not ak or not sk:
        ak = context.getUserData('ak', '').strip()
        sk = context.getUserData('sk', '').strip()
        if not ak or not sk:
            raise Exception("ak/sk empty")

    credentials = BasicCredentials(ak, sk).with_project_id(projectId)

    client = RdsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(RdsRegion.value_of(region)) \
        .build()

    try:
        request = BatchStopInstanceRequest()
        listInstanceIdsbody = [
            "id_instancia1",
            "id_instancia2" #Continuar agregando segun se requiera...
        ]
        request.body = BatchShutdownInsReq(
            instance_ids=listInstanceIdsbody
        )
        response = client.batch_stop_instance(request)
        print(response)

    except exceptions.ClientRequestException as e:
        logger.error(e.status_code)
        logger.error(e.request_id)
        logger.error(e.error_code)
        logger.error(e.error_msg)