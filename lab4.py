class Flights:
    def __init__(self,FlightId,From,To,Price):
        self.flightId = FlightId
        self.From = From
        self.to = To
        self.price = Price
    def byCity(self,city):
        flights =[]
        for i in range(len(self.From)):
            if(self.From[i] == city or self.to[i] == city):
                flights.append((self.flightId[i],self.From[i], self.to[i], self.price[i]))
        return flights
    def fromCity(self,city):
        flights =[]
        for i in range(len(self.From)):
            if(self.From[i] == city):
                flights.append((self.flightId[i],self.From[i], self.to[i], self.price[i]))
        return flights
    def betCities(self, from_city, to_city):
        flights=[]
        for i in range(len(self.From)):
            if(self.From[i] == from_city and self.to[i] == to_city):
                flights.append((self.flightId[i],self.From[i], self.to[i], self.price[i]))
                # flights.append(self.flightId[i])
                

        return flights
            



FlightId = ["AI161E90" ,"BR161F91","AI161F99","VS171E20","AS171G30","AI131F49"]    
FROM = ["BLR","BOM", " BBI", "JLR", "HYD","HYD"]
TO = ["BOM","BBI", "BLR","BBI","JLR", "BOM"]
PRICE = [5600, 6750, 8210, 5500, 4400, 3499]

flights = Flights(FlightId,FROM, TO, PRICE)

print("Search Options:")
print("1. Flights for a particular City")
print("2. Flights From a city")
print("3. Flights between two given cities")

choice = int(input("Enter your choice: "))


if choice == 1:
    city = input("Enter the city: ")
    results = flights.byCity(city)
elif choice ==2:
    city = input("Enter the city: ")
    results = flights.fromCity(city)
elif choice == 3:
    from_city = input("Enter the source city: ")
    to_city = input("Enter the destination city: ")
    results = flights.betCities(from_city, to_city)

if not results:
        print("No flights found.")
else:
    print("Flights found are:\n")
    print("Flight ID\tFrom\tTo\tPrice")
    for flight in results:
        print("\t".join(str(i) for i in flight))
# print(results)