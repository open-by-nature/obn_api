from clients import FosterHomeClient
from clients.foster_home_pb2 import FosterHomeRequest

def test():
    client = FosterHomeClient('localhost', 50052)
    result = client.get(FosterHomeRequest(id=1))
    print(result)
    
if __name__ == '__main__':
    test()