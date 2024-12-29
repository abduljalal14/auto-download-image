import os
import pandas as pd
import requests

csv_file = "produk_terlaris.csv"  
data = pd.read_csv(csv_file)

product_names = data['Nama Item']  
image_links = data['Link'] 

if not os.path.exists("downloaded_images"):
    os.makedirs("downloaded_images")

def download_image(image_url, file_name):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(file_name, 'wb') as out_file:
                out_file.write(response.content)
            print(f"Berhasil mendownload: {file_name}")
        else:
            print(f"Gagal mendownload {file_name}: {response.status_code}")
    except Exception as e:
        print(f"Error mendownload {file_name}: {e}")

for product, link in zip(product_names, image_links):
    file_name = f"downloaded_images/{product.replace(' ', '_')}.jpg"
    if isinstance(link, str) and link.startswith("http"):
        download_image(link, file_name)
    else:
        print(f"Link tidak valid untuk {product}: {link}")

print("Proses selesai.")
