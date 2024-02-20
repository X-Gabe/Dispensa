mac = input('Insira um endereço MAC: ')

mac = mac.upper()
grupos = mac.split(':')

valido = (len(grupos) == 6)

if valido:
    for grupo in grupos:
        if len(grupo) == 2:
            for c in grupo:
                if c not in '1234567890ABCDEF':
                    valido = False
                    break
            if not valido:
                break
        else:
            valido = False
            break
if valido:
    if grupos [0][1] in '13579BDF':
        broadcast = True
        for grupo in grupos:
            for c in grupo:
                if c != 'F':
                    broadcast = False
                    break
        if broadcast:
            print('MAC de Broadcast!')
        else:
            print('MAC de Multicast!')
    else:
        print('MAC de Unicast!')