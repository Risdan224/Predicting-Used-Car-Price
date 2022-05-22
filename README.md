# Predicting Saudi Used Car Price using Machine Learning (Regression Model)
## Project Capstone Modul 3 Purwadhika : Machine Learning

**By: Risdan Kristori**


## Repository Structure
- <b>README.md:</b> Deskripsi Project
- <b>Project_Capstone3_Used_Car_Price_Prediction_byRisdan.ipynb:</b> Notebook Project

## Bussiness Problem and Data Understanding
**1. Saudi Arabia Market Opportunity**

Kerajaan Saudi Arabia merupakan salah satu negara yang memiliki proyeksi pertumbuhan bisnis jual beli mobil bekas. Dilansir dari [kenresearch.com (Aashima Mendiratta, 2020)](https://www.kenresearch.com/automotive-transportation-and-warehousing/automotive-and-automotive-components/saudi-arabia-used-car-market-outlook-to-2025/356552-100.html#details) dengan meningkatnya pendapatan yang dapat dibelanjakan, bertambahnya jumlah supir perempuan (yang sebelumnya dilarang) dan tumbunnya pasar online jual beli mobil bekas merupakan faktor-faktor yang meningkatkan penjualan mobil bekas di negara tersebut. Di proyeksikan dari tahun 2019-2025, nilai (Gross Transaction Value) penjualan mobil bekas akan naik hingga 4.5% sedangkan volume penjualan akan meningkat hingga 2%.

<img src="saudi_arabia_used_car_market_infographic.jpg" alt="isolated" width="700"/>

Dikutip dari [glasglowconsultinggroup.com (Ann Gracce, 2020)](http://glasgowconsultinggroup.com/market-opportunities-for-used-cars-in-saudi-arabia-2020/) pandemi covid-19 menyebabkan stok mobil bekas di negara tersebut melimpah dan pendapatan masyarakat berkurang. apalagi dengan dinaikkannya pajak pertambahan nilai dari 5% ke 15% di tahun 2020 menyebabkan calon pembeli mobil lebih akan tertarik untuk membeli mobil bekas. Pandemi covid-19 juga menyebabkan percepatan transaksi jual beli mobil ke arah platfrom online.

Salah satu contoh webite yang menyediakan platform jual beli mobil bekas di Saudi Arabia adalah Syarah.com. Website ini mempertemukan penjual mobil bekas dengan calon pembelinya, terdapat berbagai macam jenis mobil bekas yang tersedia di platform ini. Penjual yang akan menawarkan mobil bekas di website menentukan sendiri harga mobilnya yang sesuai dengan kualitas mobil tersebut.

**2. Used Car Price Problem**

Salah satu permasalahan yang sering terjadi dalam bisnis jual beli mobil bekas adalah ketidakpastian harga mobil tersebut. Hal ini menjadi masalah tidak hanya untuk pembeli tetapi juga untuk penjual mobil. Harga yang diberikan untuk mobil bekas tergantung dari berbagai macam faktor yang terkait dengan mobil itu sendiri, seperti misalnya model, tahun produksi mobil, ukuran mesin dan lain-lain. Tidak semua orang yang ingin menjual mobilnya mengetahui fluktuasi harga mobil bekas sesuai dengan spesifikasi yang dimiliki oleh mobilnya. Bagi penjual jika dia memasang harga yang terlalu tinggi yang terjadi adalah mobil tersebut tidak akan laku terjual, sebaliknya jika penjual memasang harga terlalu rendah kerugianlah yang akhirnya didapatkan. Sebaliknya bagi pembeli yang tidak memiliki pengetahuan yang memadai mengenai harga mobil akan sangat kesulitan untuk memutuskan membeli mobil bekas.

**Problem Statement**

Penjual dan pembeli mobil bekas yang tidak memiliki pengetahuan yang cukup mengenai mobil, akan kesulitan dalam menentukan harga mobil yang akan dijual. Hal ini dapat menyebabkan tidak lakunya mobil yang dijual atau kerugian bagi penjual, bagi pembeli kerugian yang didapat adalah sulitnya memutuskan untuk membeli sebuah mobil bekas.

**Goals**

Berdasarkan permasalahan tersebut, akan dibuatkan sebuah model yang dapat memprediksi harga mobil bekas berdasarkan spesifikasi yang dimiliki oleh mobil tersebut. Harga yang dihasilkan oleh model ini akan menjadi referensi bagi penjual dan pembeli mobil jika akan melakukan transaksi jual beli mobil bekas. Tujuannya adalah supaya penjual/ pembeli mobil bekas mengambil keputusan lebih cepat dalam melakukan transaksi (menjual/ membeli).

Model ini dapat digunakan oleh platform jual beli mobil bekas online seperti Syarah.com agar pengunjung website yang ingin menjual atau membeli tidak ragu dalam menentukan harga, hal ini akan berdampak pada naiknya jumlah transaksi pada platform dan menaikkan pertumbuhan bisnis mobil bekas.

**Analytic Approach**

Dalam membuat model yang dapat memprediksi harga sebuah mobil bekas, pertama-tama dianalisis terlebih dahulu spesifikasi apa saja yang dapat berpengaruh terhadap harga tersebut. Kemudian dibuat berbagai macam model regresi yang bertujuan untuk menentukan harga, dan melalui model-model tersebut ditentukan model terbaik yang memberikan matrix terbaik yang akan digunakan sebagai final model.

**Matrix Evalution**

Matrix yang akan digunakan untuk model ini adalah:
- Root Mean Squared Error (rmse)
- R-Squared
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)
- Mean Squared Log Error (MSLE)

Nilai matrix diatas dari setiap model akan kita bandingkan dan akan dipilih nilai matrix yang sesuai dengan karakteristik data sebagai pengambilan keputusan terhadap model terbaik.

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
