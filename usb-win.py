#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import urllib.request
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def create_text_fajl():
    fajl = open('status.tsv','w')
    fajl.close()
def get_num_from_text():
    file_name = input('Enter the name of tsv fail, without tsv file extend\n')
    abc = 'ABCDEFGHIKLMNOPQRSTVXYZ'
    tmp_list = []
    noletter_list = []
    letter_list = []
    send_id = []
    send_idn = []
    with open('{}.tsv'.format(file_name),'r') as fajl:
        file_r = csv.reader(fajl, delimiter='\t')
        for row in file_r:
            tmp_list.append(row)

    for i in range(1,len(tmp_list)):
        try:
            if tmp_list[i][10].isupper():
                send_id.append(tmp_list[i][0])
                letter_list.append(tmp_list[i][10])
            else:
                send_idn.append(tmp_list[i][0])
                noletter_list.append(tmp_list[i][10])
        except:
            pass
    return noletter_list, letter_list, send_id, send_idn
    


def no_letter_numbers(nlet_list,idn):
    
    fajl = open('status.tsv','a')
    fieldnames = ['Send id', 'Tracking id' , 'Status']
    writer = csv.DictWriter(fajl, fieldnames = fieldnames, delimiter='\t')
    writer.writeheader()
    for x in range(len(nlet_list)):
        number = nlet_list[x]
        id_n = idn[x]


        url = 'https://tools.usps.com/go/TrackConfirmAction?tLabels={}'.format(number)

        header = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        req = urllib.request.Request(url, headers={'User-Agent':header})
        page = urllib.request.urlopen(req)

        soup = bs(page, 'html.parser')
        try:
            status = soup.find('span',{'class':'text_explanation'})
            print('{} ---STATUS --- {}\n'.format(number, status.text))
            writer.writerow({'Send id':id_n, 'Tracking id': number, 'Status': status.text})

            #fajl.write('{} ---STATUS --- {}\n'.format(number, status.text))
        except AttributeError:
            print('No Tracking ID number or bad number')
            
    fajl.close()


def letter_numbers(let_list, id_):
    url = 'https://wwwapps.ups.com/WebTracking/track'
    binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    #driver = webdriver.Firefox()
    webpage = driver.get(url)
    sleep(2)
    fajl = open('status.tsv','a')
    fieldnames = ['Send id', 'Tracking id' , 'Status']
    writer = csv.DictWriter(fajl, fieldnames = fieldnames, delimiter='\t')
    writer.writeheader()
    for x in range(len(let_list)):
        webpage
        num = let_list[x]
        iid = id_[x]
        form = driver.find_element_by_id('trackNums')
        form.clear()
        sleep(2)
        form.send_keys(num)
        sleep(3)
        try:
            button = driver.find_element_by_css_selector('input.ups-cta.ups-cta_primary')
        except:
            button = driver.find_element_by_css_selector('button.ups-cta.ups-cta_primary')
        driver.execute_script("arguments[0].scrollIntoView();", form)
        sleep(2)
        button.click()
        sleep(2)
            
        try:
            error = driver.find_element_by_id('tt_spStatus')
        except:
            error = driver.find_element_by_css_selector('p.error')

        error_txt = error.text
        writer.writerow({'Send id':iid, 'Tracking id': num, 'Status': error_txt})
        print('{} ---STATUS--- {}\n'.format(num, error_txt))
        sleep(5)
        driver.get(url)

    fajl.close()
    driver.close()
        
if __name__ == '__main__':
    nolet_list, let_list, id_send, idn_send = get_num_from_text()
    no_letter_numbers(nolet_list, idn_send)
    print('Opening webdriver')
    if len(let_list) == 0:
        print("No Tracking ID numbers with letters")
    else:
        sleep(10)
        letter_numbers(let_list, id_send)
