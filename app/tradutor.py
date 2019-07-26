
primeira = {0:'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove',
                 10: 'dez'}

segunda_parte1 = {10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis',
                       17: 'dezessete', 18: 'dezoito', 19: 'dezenove'}

segunda_parte2 = {20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
                       80: 'oitenta', 90: 'noventa'}

terceira = {100: 'cento', 200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos', 500: 'quinhentos', 600: 'seiscentos',
                 700: 'setecentos', 800: 'oitocentos', 900: 'novecentos'}


def transformar_dezena(valor):
    resposta = ''
    for i in segunda_parte2:
        if i < valor:
            resto = valor - i
            if 0 < resto < 10:
                resposta = str(segunda_parte2.get(i)) + ' e ' + str(primeira.get(resto))
                break
            else:
                continue
        elif i == valor:
            resposta = segunda_parte2.get(i)
            break
    return resposta


def transformar_centena(valor):
    resposta = ''
    for t in terceira:
        if t < valor:
            resto = valor - t
            if 0 < resto < 10:
                resposta = str(terceira.get(t)) + ' e ' + str(primeira.get(resto))
                break
            elif 10 <= resto < 20:
                resposta = str(terceira.get(t)) + ' e ' + str(segunda_parte1.get(resto))
                break
            elif 20 <= resto < 100:
                resposta = str(terceira.get(t)) + ' e ' + str(transformar_dezena(resto))
                break
            else:
                continue
        elif t == valor:
            if valor == 100:
                resposta = 'cem'
                break
            else:
                resposta = terceira.get(t)
                break
    return resposta


def transformar_milhar(valor):
    resposta = ''
    if 1000000 > valor >= 1000:
        valor_st = str(valor)
        if valor < 10000:
            total = int(valor_st[0])
            final = valor_st[1]+valor_st[2]+valor_st[3]
            final = int(final)
            if final != 0:
                res = transformar_numero_extenso(final)
                resposta = str(primeira.get(total)) + ' mil e ' + str(res)
            else:
                resposta = str(primeira.get(total)) + ' mil'
        elif valor < 20000:
            tmp = valor_st[0] + valor_st[1]
            final = valor_st[2] + valor_st[3] + valor_st[4]
            final = int(final)
            total = int(tmp)
            if final != 0:
                res = transformar_numero_extenso(final)
                resposta = str(segunda_parte1.get(total)) + ' mil e ' + str(res)
            else:
                resposta = str(segunda_parte1.get(total)) + ' mil'
        elif 20000 <= valor < 100000:
            tmp = valor_st[0] + valor_st[1]
            final = valor_st[2] + valor_st[3] + valor_st[4]
            final = int(final)
            total = int(tmp)
            if final != 0:
                res = transformar_numero_extenso(final)
                resposta = str(transformar_dezena(total)) + ' mil e ' + str(res)
            else:
                resposta = str(transformar_dezena(total)) + ' mil'
        elif 100000 <= valor < 1000000:
            tmp = valor_st[0] + valor_st[1] + valor_st[2]
            final = valor_st[3] + valor_st[4] + valor_st[5]
            final = int(final)
            total = int(tmp)
            if final != 0:
                res = transformar_numero_extenso(final)
                resposta = str(transformar_centena(total)) + ' mil e ' + str(res)
            else:
                resposta = str(transformar_centena(total)) + ' mil'
    return resposta


def transformar_numero_extenso(valor):
    try:
        valor = int(valor)
        if valor >= 0:
            if valor <= 10:
                return primeira.get(valor)
            elif valor < 20:
                return segunda_parte1.get(valor)
            elif 20 <= valor < 100:
                return transformar_dezena(valor)
            elif 100 <= valor < 1000:
                return transformar_centena(valor)
            elif 1000 <= valor < 1000000:
                return transformar_milhar(valor)
            else:
                return "Valor fora do intervalo 999999"
        else:
            valor = valor * (-1)
            if valor <= 10:
                return 'menos ' + str(primeira.get(valor))
            elif valor < 20:
                return 'menos ' + str(segunda_parte1.get(valor))
            elif 20 <= valor < 100:
                return 'menos ' + str(transformar_dezena(valor))
            elif 100 <= valor < 1000:
                return 'menos ' + str(transformar_centena(valor))
            elif 1000 <= valor < 1000000:
                return 'menos ' + str(transformar_milhar(valor))
            else:
                return "Valor fora do intervalo -999999"
    except (TypeError, ValueError):
        return "O valor informado é invalido!"
