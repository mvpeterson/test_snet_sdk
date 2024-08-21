from hyperon.atoms import *
from hyperon.ext import register_atoms
import os
import snet.sdk as sdk

TOKEN = "<YOUR-TOKEN>"
TOKEN_EXP_BLOCK = <EXPIRATION BLOCK>


class ServiceCall:
    def __init__(self, service_client):
        self.service_client = service_client
    def __call__(self, method, input_type, **kwargs):
        return self.service_client.call_rpc(method, input_type, **kwargs)


def import_service(org_id, service_id,
        private_key="<YOUR WALLET PRIVATE KEY>",
        eth_rpc_endpoint="<YOUR GRPC ENDPOINT URL>",
        email="<YOUR EMAIL>",
      ):
    config = {
        "private_key": private_key,
        "eth_rpc_endpoint": eth_rpc_endpoint,
        "email": email,
        "tokenToMakeFreeCall": TOKEN,
        "tokenExpirationBlock": TOKEN_EXP_BLOCK,
        "concurrency": False,
        "org_id": org_id,
        "service_id": service_id,
        "identity_name": "test",
        "identity_type": "key",
        "group_name": "default_group",
        "network": "mainnet",
        "force_update": False
    }
    snet_sdk = sdk.SnetSDK(config)
    service_client = snet_sdk.create_service_client(org_id, service_id, free_call_auth_token_bin=TOKEN,
                                                    free_call_token_expiry_block=TOKEN_EXP_BLOCK)
    return ServiceCall(service_client)

@register_atoms()
def snet_atoms():
    serviceAtom = OperationAtom("snet-service", import_service)
    return { 'snet-service': serviceAtom }
