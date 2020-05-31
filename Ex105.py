def notas(*x, sit=False):
    """->Notas - De acordo com notas informadas, calcula a média, a menor nota e a maior.
    Caso situação seja solicitada, apresenta qual situação do aluno.
    :param notas: notas informadas pelo programador.
    :param total: Quantidade de notas informadas.
    :param maior: Maior nota informada
    :param menor: Menor nota informada
    :param situação: Situação a que o aluno se encontra.
    :return Retorna o dicionário dic.
    """
    dic = dict()
    dic['total'] = len(x)
    dic['maior'] = max(x)
    dic['menor'] = min(x)
    dic['média'] = sum(x) / len(x)
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'Boa'
        if dic['média'] < 5:
            dic['situação'] = 'Ruim'
        else:
            dic['situação'] = 'Razoável'
    return dic


program = notas (8.5, 7.5, 9.5, 5, sit=True)
print(program)
help(notas)