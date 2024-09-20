from hfc.fabric import Client

class PencilContract:
    def __init__(self, channel_name, chaincode_name):
        self.client = Client(net_profile="network.json")
        self.channel = self.client.get_channel(channel_name)
        self.chaincode = chaincode_name

    def list_pencil(self, pencil_id, owner, price):
        args = [pencil_id, owner, price]
        response = self.channel.chaincode_invoke(
            chaincode_name=self.chaincode, fcn='listPencil', args=args)
        return response

    def buy_pencil(self, pencil_id, buyer):
        args = [pencil_id, buyer]
        response = self.channel.chaincode_invoke(
            chaincode_name=self.chaincode, fcn='buyPencil', args=args)
        return response

    def get_pencils(self):
        response = self.channel.chaincode_query(
            chaincode_name=self.chaincode, fcn='getAllPencils')
        return response
