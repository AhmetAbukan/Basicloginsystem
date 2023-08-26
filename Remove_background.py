from rembg import remove 

input_path = "#Arka planını kaldırmak istediğiniz görselin dosya yolunu girin.jpeg#" 
output_path="#Arka planını kaldırmak istediğiniz görselin kaydetmek istediğiniz dosya yolunu girin.png#"

with open(input_path,"rb") as i:
    with open(output_path,"wb") as o:
        input_file=i.read()
        output_file=remove(input_file)
        o.write(output_file)











