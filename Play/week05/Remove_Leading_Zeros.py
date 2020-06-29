def remove_leading(ip):
    lista = ip.split('.')
    new_ip = []

    for i in lista:
        aux = int(i)
        new_ip.append(str(aux))

    return ".".join(new_ip)

print(remove_leading('255.024.01.01'))