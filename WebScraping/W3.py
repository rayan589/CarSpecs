from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup





my_url = 'https://www.caranddriver.com/lamborghini/urus/specs/2021/lamborghini_urus_lamborghini-urus_2021/417970'

#opening up connection, grabbing the page


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML Parser
page_soup = soup(page_html, "html.parser")

filename = "cars.csv"
f = open(filename, "a")



Year = page_soup.findAll("option", selected=True)[0].text
Trim = page_soup.find("div", {"class":"overview-text"}).div.text
Price = page_soup.findAll("div", {"class":"price"})[0].text

ct = page_soup.findAll("div", {"class":"spec-section-title-value"})

Drivetrain = ct[1].text
Engine = ct[3].text
FuelSystem = ct[5].text
HP = ct[6].text
Torque = ct[7].text
Transmission = ct[10].text
NumSpeed = ct[11].text
CO2 = ct[26].text
Range = ct[27].text
FuelConsumption = ct[28].text
FuelCapacity = ct[30].text
Length = ct[33].text
Width = ct[34].text
Height = ct[35].text
NumSeats = ct[42].text
BrakeType = ct[72].text
FrontTireSize = ct[79].text
RearTireSize = ct[82].text


print("Year: " + Year)
print("Trim: " + Trim)
print("Price: " + Price)
print("DriveTrain: " + Drivetrain)
print("Engine: " + Engine)
print("HorsePower: " + HP)
print("Torque: " + Torque)
print("Transmission: " + Transmission)
print("Number of Speed Transmission: " + NumSpeed)
print("CO2 Emission: " + CO2)
print("Range: " + Range)
print("Fuel Consumption: " + FuelConsumption)
print("Fuel System: " + FuelSystem)
print("Fuel Capacity: " + FuelCapacity)
print("Length: " + Length)
print("Width: " + Width)
print("Height: " + Height)
print("Number of Seats: " + NumSeats)
print("Brake Type: " + BrakeType)
print("Front Tire Size: " + FrontTireSize)
print("Rear Tire Size: " + RearTireSize)

Brand = page_soup.findAll("div", {"class":"specs-style-select-container"})[1].option.next_sibling.next_sibling.text.split(" ")[0]
Model = page_soup.findAll("div", {"class":"specs-style-select-container"})[1].option.next_sibling.next_sibling.text.split(" ")[1]
print("Brand: " + Brand)
print("Model: " + Model)
f.write(Brand + "," + Model + "," + Year + "," + Trim + "," + Price.replace(",", ".") + "," + Drivetrain + "," + Engine + "," + HP + "," + Torque + "," + Transmission + "," + NumSpeed + "," + CO2 + "," + Range + "," + FuelConsumption + "," + FuelSystem + "," + FuelCapacity + "," + Length + "," + Width + "," + Height + "," + NumSeats + "," + BrakeType + "," + FrontTireSize + "," + RearTireSize + "\n" )
	
f.close()