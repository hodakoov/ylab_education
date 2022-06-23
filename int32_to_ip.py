def int32_to_ip(int32):
    ip = []
    for i in range(1, 5):
        ip.insert(0, str(int32 % 256))
        int32 //= 256
    result = '.'.join(ip)
    return result
