# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkrds.v3.region.rds_region import RdsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkrds.v3 import *

def handler(event, context):
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
        request = StartResizeFlavorActionRequest()
        request.instance_id = context.getUserData('id_instancia', '').strip()
        resizeFlavorbody = ResizeFlavorObject(
            spec_code=context.getUserData('flavor', '').strip()
        )
        request.body = ResizeFlavorRequest(
            resize_flavor=resizeFlavorbody
        )
        response = client.start_resize_flavor_action(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
