from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import requests
from lxml import html
import json

class udemy:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'cookie': '__cfduid=d36951e57c6a9c3c2d20de5960f121f361614185616; ud_cache_language=es; ud_cache_modern_browser=1; ud_cache_version=1; ud_cache_release=870ce6051b2a9e467f7d; ud_cache_marketplace_country=VE; ud_cache_campaign_code=KEEPGOING21; ud_cache_price_country=VE; ud_firstvisit=2021-02-24T16:53:36.254256+00:00:1lExPs:NzJxZ2trHFjuJ1MuW7JxrKgZDps; __udmy_2_v57r=68f2b4c1e2004e75aa45c91f7e47dd83; ud_cache_brand=VEes_ES; seen=1; __cfruid=28eacbef6fea32f847469d6bd0e3098a36ab5418-1614185616; __cf_bm=46b92f011329fc116841e055a8bae2f48e82a67a-1614185624-1800-AQuMB9Eut2uzcIqfCp0NNYqNWeQi2/G8NP9VI4EhD5MaShEK2rEAPMy7/aFCG/mo+eHUoIS/V7T0aB7Ixs9gXbvf7j8WrOUwaBRuGQmHgfobVokDy9A18i0s9P+WZV1CIpkwJ+6cYM3TPgW+IFK7ycVSz7FzfCQjQS7urCq5rgzS; EUCookieMessageShown=true; EUCookieMessageState=initial; __ssid=0e8afecb62febcb1ff7a50959fdca17; _gcl_au=1.1.1314726463.1614185640; blisspoint_fpc=8f73ac4b-98f0-4820-b70f-2ccc2891989c; _gid=GA1.2.1055655191.1614185641; _pxhd=9b9761c309952a3870fdb0de59302d7d8ef2ea12728a8741178a7fd1bc2de004:e789d3a1-76c0-11eb-a202-4f281c11097b; _rdt_uuid=1614185671216.61ebe44d-f3de-42e1-916b-94cf1b48eec4; IR_gbd=udemy.com; ki_r=; _pxvid=e789d3a1-76c0-11eb-a202-4f281c11097b; _fbp=fb.1.1614185674325.722870776; client_id=bd2565cb7b0c313f5e9bae44961e8db2; ki_t=1614185673187%3B1614185673187%3B1614185800296%3B1%3B4; _px2=eyJ1IjoiNDE4ZDdmNTAtNzZjMS0xMWViLTkzODUtNzFjYjA0Nzk0ODQxIiwidiI6ImU3ODlkM2ExLTc2YzAtMTFlYi1hMjAyLTRmMjgxYzExMDk3YiIsInQiOjE2MTQxODY3MDA0NjQsImgiOiJmZTU5MzExOGQzMzdkMzRmOWU4ODA0ZGQ4NTRlMTJhY2I2MTE2Y2JjNzQ1ZTlmZDg4OTBlZTI5MzRmYzdkYTA3In0=; _px3=b22660b47d5dd70a5221e880f09a53bb9d26546cd1d6b80d6d03c8159c2bc0ca:7KFjrGiT2756av0vfgX3k9+S63nsBTc8F/0s/eul9GgB2JCTR7Ce35MIv97ku6nEKETvgZC7jD1bJZHsauiZDw==:1000:LGUBTx5EmXzdJo6yguxwHApEnb/kapf3KeJsnu1QmQLBdo88qa6PQquMk7N5FQ/VdBB1O92nHW7SivNZNqkMswzkvZpUyiQ+hLuEJV6RGi6z41skmahMciXhJ6NH8UMgMT2bt0XxMaKXyfEZrB+kCy89M7TvRaOpDWQXF41V6xY=; ud_cache_user=106452026; ud_user_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc19zdXBlcnVzZXIiOmZhbHNlLCJlbWFpbCI6ImZlZGVyaWNvZWxicm9kZXJAZ21haWwuY29tIiwiaWQiOjEwNjQ1MjAyNiwiZ3JvdXBfaWRzIjpbXX0.JvwD9yajVg70iFQxsh5Hmih68Y7jeQF3WTOk4NA3Xfg; ud_cache_logged_in=1; dj_session_id=ndfkfpcb6tr2vrqhe19qgduha69qsz9f; ud_credit_last_seen=None; ud_credit_unseen=0; access_token=WbUJmfwgdcxXSOEmPh1QGaw2L2p6LA1r7xcDPSlN; ud_last_auth_information="{\"suggested_user_name\": \"Federico Alexander David\"\054 \"suggested_user_email\": \"federicoelbroder@gmail.com\"\054 \"backend\": \"udemy-auth\"\054 \"suggested_user_avatar\": \"https://img-a.udemycdn.com/user/50x50/anonymous_3.png?QbHlvIKm8tii_fRvvIzLPsyKPisT0bmIbMZzsDYeM72G6jq18BmKYiWMknv558nSn4D32qfOiAgh3voZAdz8vIRUaVGr8bPvHNIxQKI056bRsdK2KVgBBps\"}:1lExdd:F6LKgZsepIMoPH79A37VEqtz7ns"; csrftoken=TtlwALATPx69nwvBsz6Avrsv4ok7RmVstrUEvK87T2C2vEKeW8AIR6lp1cliuU8x; ud_cache_device=desktop; _gat=1; eventing_session_id=0PaLyhvLQWiB2V6DsCwMdQ-1614188272376; IR_5420=1614186474944%7C0%7C1614185671373%7C%7C; IR_PI=06009827-76c1-11eb-ad2c-42010a246d2d%7C1614272874944; _ga_7YMFEFLR6Q=GS1.1.1614185640.1.1.1614186474.0; _ga=GA1.1.70325949.1614185641; stc111655=tsa:1614185670904.553375530.6155357.8550080862580169.9:20210224173755|env:1%7C20210327165430%7C20210224173755%7C7%7C1014624:20220224170755|uid:1614185670904.1671943636.798306.111655.1489363879.:20220224170755|srchist:1014624%3A1%3A20210327165430:20220224170755; evi="SlFYNkxYDm4DQRJ5TFgObkcSCXtbWkR6HVFdY1RTCGATQR54VkBPNxMFSmNUVEB6CV8JN0xYRDFMDg=="; ud_rule_vars="eJyFjssOgjAURH-FdKuYvov9libNpdxio7GxFDaEf5corl3NYnLmzEoqlBErDn5JU6q5WN1F3svAkFMq0SgAqcKVRYPSDEMnbMj5npDYhqyOPGCqvuBrxj0HqOj2whFOOWspb7lsmLZKWKEvWkhl9IlSS6kj5-aAa57DzdcCMabgpzyXgH6BkqB_HGu5jPBM4QvFVHbq8_aPkEvVCfkTbmR7A999SA8=:1lExdn:Vm0B-7TD3ELEnljZ2mTTQwPN70U"'
        }
        self.s = requests.session()
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
        driver = webdriver.Chrome('./driver/chromedriver.exe', chrome_options=self.opts)
        driver.maximize_window()
        driver.get('https://udemy.linkhide.xyz')
        self.driver = driver

    def Get_curso(self, url_curso):
        #obtener id del curso
        self.s.headers = self.headers
        r = self.s.get(url_curso)
        soup = html.fromstring(r.text)
        id_curso = soup.xpath('//body/@data-clp-course-id')[0]
        return id_curso

    def Get_all_videos(self, id_curso):
        self.s.headers['authorization'] = 'Bearer WbUJmfwgdcxXSOEmPh1QGaw2L2p6LA1r7xcDPSlN'
        r = self.s.get(f'https://www.udemy.com/api-2.0/courses/{id_curso}/subscriber-curriculum-items/?page_size=1400&fields[lecture]=title,object_index,is_published,sort_order,created,asset,supplementary_assets,is_free&fields[quiz]=title,object_index,is_published,sort_order,type&fields[practice]=title,object_index,is_published,sort_order&fields[chapter]=title,object_index,is_published,sort_order&fields[asset]=title,filename,asset_type,status,time_estimation,is_external&caching_intent=True')
        data = r.json()
        capitulos_curso = data['results']
        return capitulos_curso

    def Descargar_video(self, id_curso, capitulo):
        if capitulo['_class'] == 'lecture':
            print('Obteniendo capitulo', capitulo['title'])
            id = capitulo['id']
            r = self.s.get(f'https://www.udemy.com/api-2.0/users/me/subscribed-courses/{id_curso}/lectures/{id}/?fields[lecture]=asset,description,download_url,is_free,last_watched_second&fields[asset]=asset_type,length,media_license_token,media_sources,captions,thumbnail_sprite,slides,slide_urls,download_urls&q=0.27194179700788634')
            data_cap = r.json()
            titulo = capitulo['title']
            chapter = capitulo['object_index']
            titulo = chapter+' - '+titulo
            url = data_cap['asset']['media_sources'][0]['src']
            self.driver.find_element_by_xpath('//input[@name="titulo"]').clear()
            self.driver.find_element_by_xpath('//input[@name="url_udemy"]').clear()
            sleep(1)
            self.driver.find_element_by_xpath('//input[@name="titulo"]').send_keys(titulo)
            self.driver.find_element_by_xpath('//input[@name="url_udemy"]').send_keys(url)
            self.driver.find_element_by_xpath('//input[@id="down_here"]').click()
