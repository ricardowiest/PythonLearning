from uteis.utilidade import moeda
from uteis.utilidade import dado

p = dado.leiadin('Digite o preço R$')
moeda.resumo(p, 10, 15)
