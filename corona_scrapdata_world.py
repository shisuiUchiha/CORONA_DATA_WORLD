# data scraped from https://www.worldometers.info/coronavirus/ and https://www.mygov.in/covid-19/
from bs4 import BeautifulSoup	
import requests
url="https://www.worldometers.info/coronavirus"
print ("Gathering Data from "+url)
response = requests.get(url).text
soup=BeautifulSoup(response,"html.parser")
#f=open("data_world.txt","w+")
#f.write(soup.prettify())
#f.close
mytrs=soup.findAll("tr",{"class":"total_row"})
mytd=mytrs[0].findAll("td",{"style":""})
data_num=[]
i=0
for mytds in mytd:
	if i==0:
		i=i+1
	else:
		data_num.append(mytds.get_text())

print("Total Corona Cases   "+data_num[0])
print("\n")
print("Total Deaths   "+data_num[1])
print("\n")
print("Total Recovered Cases   "+data_num[2])
print("\n")
print("Total Active Cases   "+data_num[3])
print("\n")
print("Total Serious Active Cases   "+data_num[4])
print("\n")

mycountry=soup.findAll("a",{"class":"mt_a"})
list_of_countries=[]
for mycountrys in mycountry:
	country_string=mycountrys.get_text()
	if country_string not in list_of_countries:
		list_of_countries.append(country_string)

list_of_countries.append("Ïndia")

print("If you want to find data on individual countries type Y else N")
j=0
continuing=input()
if(continuing=="Y"):
	j=0
	print("List of countries whose individual data is available")
	print("\n")
	for list_of_country in list_of_countries:
		print(list_of_country)
	print("\n")
else:
	j=1


	
while j==0:
	print("Enter the name of country from the list you want to view")
	print("\n")
	name_country=input()
	if name_country=="India":
		print("Gathering Data from https://www.mygov.in/covid-19/")
		print("\n")
		html=requests.get("https://www.mygov.in/covid-19/").text
		india_soup=BeautifulSoup(html,"html.parser")
		india_words=[]
		india_num=[]
		india_divs=india_soup.findAll("div",{"class": "info_label"})
		india_spans=india_soup.findAll("span",{"class": "icount"})
		for i in range(len(india_divs)):
			print (india_divs[i].get_text(),india_spans[i].get_text())
			print("\n")
		print("If you want to see data of another country, Type Y else N")
		print("\n")
		yes_no=input()
		if yes_no=="Y":
			j=0
		else:
			j=1
	else:
		country_url=url+"/country/"+name_country+"/"
		print("Gathering Data from "+country_url)
		print("\n")
		c_response=requests.get(country_url).text
		c_soup=BeautifulSoup(c_response,"html.parser")
		title_data=c_soup.findAll("title")
		for t_data in title_data:
			print(t_data.get_text())
			print("\n")
		print("If you want to see data of another country, Type Y else N")
		print("\n")
		yes_no=input()
		if yes_no=="Y":
			j=0
		else:
			j=1
	

