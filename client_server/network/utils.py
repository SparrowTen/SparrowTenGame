import pickle


def packet_serializer(data):
    # 把 data 的 dict 進行打包
    packet = pickle.dumps(data)
    return packet


def packet_deserializer(packet):
    # 把 packet 解開
    data = pickle.loads(packet)
    return data
