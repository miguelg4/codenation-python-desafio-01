from datetime import datetime
#arredondandamento de numero para baixo. 
# exemplo: math.floor(função)
import math

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

    #preços da ligações, definindo tempo de ligações.
def calcular_preco(initial, end):
    #convertendo para o formato de data e hora padrão internacional
    initial = datetime.fromtimestamp(initial)
    end = datetime.fromtimestamp(end)
    
    #Ligações entre 22h e 06h, Taxa permanente: R $ 0.36
    # os demais horários, cobrar taxa de R$ 0.36 centavos + R$ 0.09 por minuto cheio.
    if (initial.hour >= 22 or end.hour < 6):
        return 0.36
    
    if (end.hour >= 22):
        end = datetime(end.year, end.month, end.day, 22)
    
    if (initial.hour < 6):
        initial = datetime(initial.year, initial.month, initial.day, 6)
    
    duracao = math.floor((end - initial).seconds/60)
    preco_final = (duracao * 0.09) + 0.36
    return preco_final

    # definindo lista de entrada por origem.
def classify_by_phone_number(records):
    
    results = []

    for record in records:
        i = 0

        for result in results:

            if result['source'] == record['source']:
                i = 1
                #calculando ligações da mesma origem
                valor_inicial = result['total']
                preco = calcular_preco(record['start'], record['end'])
                valor_atualizado = round((valor_inicial + preco), 2)
                result['total'] = valor_atualizado

        if i == 0:
            preco = calcular_preco(record['start'], record['end'])
            preco_decimal_2 = round(preco, 2)
            results.append({'source': record['source'], 'total': preco_decimal_2})

    #resultado final ordenação decrescente.
    resultado_final = sorted(
        results, key=lambda result: result['total'], reverse=True
    )
    return resultado_final

#classify_by_phone_number(records)