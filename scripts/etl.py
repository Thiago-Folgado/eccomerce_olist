# Bibliotecas
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq


# Var caminhos csv
customers= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_customers_dataset.csv"
geolocation= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_geolocation_dataset.csv"
order_items= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_order_items_dataset.csv"
payments= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_order_payments_dataset.csv"
reviews= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_order_reviews_dataset.csv"
orders= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_orders_dataset.csv"
products= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_products_dataset.csv"
sellers= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\olist_sellers_dataset.csv"
product_category_name= r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Projetos\project_olist_eccom\data\raw\product_category_name_translation.csv"


# var data frames
df_customers = pd.read_csv(customers,sep=",")
df_geolocation = pd.read_csv(geolocation,sep=",")
df_order_items = pd.read_csv(order_items,sep=",")
df_payments = pd.read_csv(payments,sep=",")
df_reviews = pd.read_csv(reviews,sep=",")
df_orders = pd.read_csv(orders,sep=",")
df_products = pd.read_csv(products,sep=",")
df_sellers = pd.read_csv(sellers,sep=",")
df_product_category_name = pd.read_csv(product_category_name,sep=",")


# Credenciais
credencial = service_account.Credentials.from_service_account_file(
    r"C:\Users\Thiag\Documents\Data_analytics\Projetos Data\Outros\analytics-463320-3bc0f7f4d1b9.json",
    scopes=['https://www.googleapis.com/auth/bigquery']
)


# Var para inserção de dados bq
projeto     ='analytics-463320'
dataset     ='bronze'
parameretro ='replace'


# Inserção de dados bq
to_gbq(df_customers, destination_table=f'{projeto}.{dataset}.olist_customers', project_id=projeto, if_exists=parameretro)
to_gbq(df_geolocation, destination_table=f'{projeto}.{dataset}.olist_geolocation', project_id=projeto, if_exists=parameretro)
to_gbq(df_order_items, destination_table=f'{projeto}.{dataset}.olist_order_items', project_id=projeto, if_exists=parameretro)
to_gbq(df_payments, destination_table=f'{projeto}.{dataset}.olist_payments', project_id=projeto, if_exists=parameretro)
to_gbq(df_reviews, destination_table=f'{projeto}.{dataset}.olist_reviews', project_id=projeto, if_exists=parameretro)
to_gbq(df_orders, destination_table=f'{projeto}.{dataset}.olist_orders', project_id=projeto, if_exists=parameretro)
to_gbq(df_products, destination_table=f'{projeto}.{dataset}.olist_products', project_id=projeto, if_exists=parameretro)
to_gbq(df_sellers, destination_table=f'{projeto}.{dataset}.olist_sellers', project_id=projeto, if_exists=parameretro)
to_gbq(df_product_category_name, destination_table=f'{projeto}.{dataset}.olist_product_category_name', project_id=projeto, if_exists=parameretro)


