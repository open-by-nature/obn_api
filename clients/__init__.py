import grpc

from .foster_home_pb2_grpc import FosterHomeServiceStub
from .foster_home_pb2 import (
    FosterHomeRequest
    , FosterHomeSearchRequest
    , FosterHome
    , FosterHomeSearchResult
    , FosterHomeDeleteResult
)

class GRPCClient(object):
    """
    Client for gRPC services
    """

    def __init__(self, host: str = 'localhost', port: int = 5052
        , channel: grpc.Channel = None, stub: object = None):
        self.host = host
        self.port = port

        if channel is None:
            self.channel = grpc.insecure_channel(
                f'{self.host}:{self.port}'
            )
        else:
            self.channel = channel 
        
        self.stub = stub(self.channel)


    def get(self, message: object) -> object:
        return self.stub.get(message)

    def search(self, message: object) -> object:
        return self.stub.search(message)

    def save(self, message: object) -> object:
        return self.stub.save(message)

    def delete(self, message: object) -> object:
        return self.stub.delete(message)

class FosterHomeClient(GRPCClient):
    """
    Client for Foster homes gRPC service
    """

    def __init__(self, host: str = 'localhost', port: int = 5052
        , channel: grpc.Channel = None):
        super().__init__(host=host, port=port, channel=channel, stub=FosterHomeServiceStub)


__all__ = [
    'GRPCClient'
    , 'FosterHomeClient'
    , 'FosterHomeRequest'
    , 'FosterHomeSearchRequest'
    , 'FosterHome'
    , 'FosterHomeSearchResult'
    , 'FosterHomeDeleteResult'
]