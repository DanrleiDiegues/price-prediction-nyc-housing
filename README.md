# 1. Para testar a predição com a feature:
{'id': 2595,
 'nome': 'Skylit Midtown Castle',
 'host_id': 2845,
 'host_name': 'Jennifer',
 'bairro_group': 'Manhattan',
 'bairro': 'Midtown',
 'latitude': 40.75362,
 'longitude': -73.98377,
 'room_type': 'Entire home/apt',
 'minimo_noites': 1,
 'numero_de_reviews': 45,
 'ultima_review': '2019-05-21',
 'reviews_por_mes': 0.38,
 'calculado_host_listings_count': 2,
 'disponibilidade_365': 355
 }


1. Entre em 'predict.ipynb' e rode o código completo;
2. Para trocar o modelo, basta substituir o path que leva o modelo. Onde está "model_path = 'models/catboost_model_20250208_131741.pkl'"

# 2. Para testar outras instâncias:
1. É preciso criar as instâncias em um arquivos csv. com as chaves:
{'id': int,
 'nome': object,
 'host_id': int,
 'host_name': object,
 'bairro_group': object,
 'bairro': object,
 'latitude': float,
 'longitude': float,
 'room_type': object,
 'minimo_noites': int,
 'numero_de_reviews': int,
 'ultima_review': data-time,
 'reviews_por_mes': int,
 'calculado_host_listings_count': int,
 'disponibilidade_365': int
 }

2. Carregar esta instância no arquivo "feature_engineering_and_preprocessing.ipynb"
3. Rodar todo o arquivo, para que as features desta instância passe por todo a criação de derivadas de novas feautres
4. Posteriormente, salve estas features em data/
5. Carregue a instância desejada em predict.ipynb para seguir o fluxo inicial de predição.

# 3. Trabalhos futuros:
1. Automatizar o preprocessamento e feature engineering das instâncias de entrada;
2. Criar uma aplicação no Streamlit para predição automática;
3. Investigar melhor onde meu modelo está errando, utilizando SHAP (SHapley Additive exPlanations), por exemplo, e fazer novos ajustes nos modelos para melhorar o desempenho das predições;
4. Buscar novos dados externos que ajudem a explicar a variabilidade dos preços das casas.
