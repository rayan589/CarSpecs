from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup





my_url = 'https://www.caranddriver.com/lamborghini/urus/specs/2021/lamborghini_urus_lamborghini-urus_2021/417969'

#opening up connection, grabbing the page


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML Parser
page_soup = soup(page_html, "html.parser")



headers = "Brand, Model, Year, Trim, Price, DriveTrain, Engine, HorsePower_@_rpm, Torque_@_rpm, Transmission, Number_of_Speed, CO2_Emissions_15K_mi/year_(tons), Range_city/highway_(miles), Fuel_Consumption_combined/city/highway(mpg), Fuel_System, Fuel_Capacity, Length(inches), Width_Without_Mirrors(inches), Height(inches), Number_of_Seats, Brake_Type, Front_Tire_Size, Rear_Tire_Size\n"


Brand = page_soup.findAll("div", {"class":"specs-style-select-container"})[1].option.next_sibling.next_sibling.text.split(" ")[0]
Model = page_soup.findAll("div", {"class":"specs-style-select-container"})[1].option.next_sibling.next_sibling.text.split(" ")[1]
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

print("Brand: " + Brand)
print("Model: " + Model)
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

filename = "cars.csv"
f = open(filename, "w")
f.write(headers)
f.write(Brand + "," + Model + "," + Year + "," + Trim + "," + Price.replace(",", ".") + "," + Drivetrain + "," + Engine + "," + HP + "," + Torque + "," + Transmission + "," + NumSpeed + "," + CO2 + "," + Range + "," + FuelConsumption + "," + FuelSystem + "," + FuelCapacity + "," + Length + "," + Width + "," + Height + "," + NumSeats + "," + BrakeType + "," + FrontTireSize + "," + RearTireSize + "\n" )
f.close()



