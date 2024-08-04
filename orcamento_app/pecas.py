def calcular(largura_peca, altura_peca):
    # Calcula quantas peças cabem horizontalmente e verticalmente
    largura_papel = 66
    altura_papel = 96
    hor_hor = largura_papel // (int(largura_peca)+1)
    ver_ver = altura_papel // (int(altura_peca)+1)
    largxlarg = hor_hor * ver_ver
    print(f'Peça na direção normal da {largxlarg} peças')
    ver_hor = largura_papel // (int(altura_peca)+1)
    hor_ver = altura_papel // (int(largura_peca)+1)
    largxcom = ver_hor * hor_ver
    print(f'Peça invertida da {largxcom} peças')
    if largxlarg > largxcom:
        total_folhas = largxlarg
    else:
        total_folhas = largxcom

    return total_folhas

