# Predicting Saudi Used Car Price using Machine Learning (Regression Model)
## Project Capstone Modul 3 Purwadhika : Machine Learning

**By: Risdan Kristori**


## Repository Structure
- <b>README.md:</b> Deskripsi Project
- <b>Project_Capstone3_Used_Car_Price_Prediction_byRisdan.ipynb:</b> Notebook Project

## Introduction
**Saudi Arabia Market Opportunity**

Kerajaan Saudi Arabia merupakan salah satu negara yang memiliki proyeksi pertumbuhan bisnis jual beli mobil bekas. Dilansir dari [kenresearch.com (Aashima Mendiratta, 2020)](https://www.kenresearch.com/automotive-transportation-and-warehousing/automotive-and-automotive-components/saudi-arabia-used-car-market-outlook-to-2025/356552-100.html#details) dengan meningkatnya pendapatan yang dapat dibelanjakan, bertambahnya jumlah supir perempuan (yang sebelumnya dilarang) dan tumbunnya pasar online jual beli mobil bekas merupakan faktor-faktor yang meningkatkan penjualan mobil bekas di negara tersebut. Di proyeksikan dari tahun 2019-2025, nilai (Gross Transaction Value) penjualan mobil bekas akan naik hingga 4.5% sedangkan volume penjualan akan meningkat hingga 2%.

<img src="saudi_arabia_used_car_market_infographic.jpg" alt="isolated" width="700"/>

Salah satu permasalahan yang sering terjadi dalam bisnis jual beli mobil bekas adalah ketidakpastian harga mobil tersebut. Hal ini menjadi masalah tidak hanya untuk pembeli tetapi juga untuk penjual mobil. Harga yang diberikan untuk mobil bekas tergantung dari berbagai macam faktor yang terkait dengan mobil itu sendiri, seperti misalnya model, tahun produksi mobil, ukuran mesin dan lain-lain. Tidak semua orang yang ingin menjual mobilnya mengetahui fluktuasi harga mobil bekas sesuai dengan spesifikasi yang dimiliki oleh mobilnya. Bagi penjual jika dia memasang harga yang terlalu tinggi yang terjadi adalah mobil tersebut tidak akan laku terjual, sebaliknya jika penjual memasang harga terlalu rendah kerugianlah yang akhirnya didapatkan. Sebaliknya bagi pembeli yang tidak memiliki pengetahuan yang memadai mengenai harga mobil akan sangat kesulitan untuk memutuskan membeli mobil bekas.

**Goals**

Membuat sebuah model yang dapat memprediksi harga mobil bekas berdasarkan spesifikasi yang dimiliki oleh mobil tersebut. Harga yang dihasilkan oleh model ini akan menjadi referensi bagi penjual dan pembeli mobil jika akan melakukan transaksi jual beli mobil bekas. Tujuannya adalah supaya penjual/ pembeli mobil bekas mengambil keputusan lebih cepat dalam melakukan transaksi (menjual/ membeli).

Model ini dapat digunakan oleh platform jual beli mobil bekas online seperti Syarah.com agar pengunjung website yang ingin menjual atau membeli tidak ragu dalam menentukan harga, hal ini akan berdampak pada naiknya jumlah transaksi pada platform dan menaikkan pertumbuhan bisnis mobil bekas.

**Matrix Evalution**

Matrix yang akan digunakan untuk model ini adalah:
- Root Mean Squared Error (rmse)
- R-Squared
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)
- Mean Squared Log Error (MSLE)

**Data Information**
- Data yang digunakan merupakan data spesifikasi/fitur mobil bekas beserta beserta harga jualnya yang telah disediakan oleh Purwadhika. Dilihat dari bentuk dan pola data, diasumsikan bahwa data ini diambil dari website Syarah.com yang menjual mobil bekas di Saudi Arabia.
- Data 'price'/harga untuk mobil bekas yang sifatnya 'negotiable' bernilai 0 (nol). Harga berdasarkan kesepakatan antara penjual dan pembeli.

#### Attribute Information

| Attribute | Data Type| Description |
| --- | --- | --- |
| Type | Object | Type of used car |
| Region | Object | The region in which the used car was offered for sale |
| Make | Object | Name of the car company |
| Gear_Type | Object | Automatic / Manual |
| Origin | Object | Country of importer (Gulf / Saudi / Other) |
| Options | Object | Full Options / Semi-Full / Standard |
| Year | Int | Year of Manufacturing |
| Enginee_Size | Float | The engine size of used car |
| Mileage | Int | The distance that used car have travelled, measured in miles |
| Negotiable | Bool | If True, the price is 0. This means the price is negotiable (not set) |
| Price | int | Price of the used car (in SAR) |

## Exploratory Data Analysis

<img src="=EDA1.png" alt="isolated" width="700"/>

<img src="=EDA2.png" alt="isolated" width="700"/>

<img src="=EDA3.png" alt="isolated" width="700"/>
