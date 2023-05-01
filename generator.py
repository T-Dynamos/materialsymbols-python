import shutil
import os
import requests
import json 

# Possible values
FONT_TYPE = ["Outlined", "Rounded", "Sharp"]
OPTICAL_SIZE = ["20", "24", "40", "48"]  # in px
GRAD = ["-25", "0", "200"]
WEIGHT = [str(num) for num in range(100, 800, 100)]  # max = 700, min = 100
FILL = [True, False]  # 1 or 0

# Save dir
DIR = "fonts"

# Headers
HEADERS = {
    "authority": "fonts.googleapis.com",
    "method": "GET",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-IN,en;q=0.9,hi;q=0.8",
    "cache-control": "max-age=0",
    "if-modified-since": "Mon, 01 May 2023 15:35:59 GMT",
    "sec-ch-ua": 'Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Linux",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}

def convert_font(file_name):
    if shutil.which("woff2_decompress"):
        os.system("woff2_decompress {}".format(file_name))
    else:
        raise OSError("woff2_decompress is not in PATH, consider installing!")

def get_url(font_type, optical_size, weight, grad, fill=False):
    fill_type = "1" if fill == True else "0"
    url = f"https://fonts.googleapis.com/css2?family=Material+Symbols+{font_type}:opsz,wght,FILL,GRAD@{optical_size},{weight},{fill_type},{grad}"
    return (
        requests.get(url, headers=HEADERS).text.split("url(")[1].split(")")[0], 
        DIR + "/Material_Symbols_"+font_type+"-"+optical_size+"-"+weight+"-"+fill_type+"_"+grad+".ttf"
    )

def generate_sha256sum():
    final_data = {}
    for file in os.listdir("fonts/"):
        final_data[file] = os.popen("sha256sum {}".format("fonts/"+file)).read().strip("\n").split(" ")[0]
    with open("checksum.json", "w") as file:
        json.dump(final_data , file)
        file.close()

def main():
    all_fonts =  []

    if os.path.exists(DIR) == False:
        os.mkdir(DIR)

    for font_type in FONT_TYPE:
        for size in OPTICAL_SIZE:
            for grad in GRAD:
                for weight in WEIGHT:
                    for fill in FILL:
                        temp, new_filename = get_url(font_type, size, weight, grad, fill=fill)
                        with open(new_filename[:-3]+"woff2" , "wb") as file:
                            file.write(requests.get(temp).content)
                            file.close() 
                        convert_font(new_filename[:-3]+"woff2")
                        os.remove(new_filename[:-3]+"woff2")
                        all_fonts.append(new_filename)
    
    generate_sha256sum()
    print("Total generated : ",len(all_fonts))

main()
