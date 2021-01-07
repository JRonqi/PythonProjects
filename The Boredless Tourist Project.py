#List of destionations for our travellers
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

#Test traveller
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#Function to get the index of destionation for destinations list
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#testing the get_destionation_index
print(get_destination_index("Los Angeles, USA")) #finding the index, should equal to 2
print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India")) #receive value error since its not in the list of destionations

#Function to get the travel location from traveller list
def get_traveler_location(traveler):
  traveler_destination = traveler[1] #Preloaded information, destionation is always at index 1
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#testing the get_traveler_location function
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)


#list of attraction sites
#attractions = [[], [], []. [], []] # creating an empty list for each number of destionations.

attractions = [[] for attraction in destinations] #creates an empty list based of the values in destionations
print(attractions)

#Function to add attractions to the list
def add_attraction(destination, attraction):
  try: #if the destination does exist
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    
    #Appending the attraction passed in the function to a new list
    attractions_for_destination.append(attraction)
    return
  
  except ValueError: #if the destination does not exist
    print("Error Caught!")
    return

#Testing the add_attraction function (Destination, attraction)
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)

#function to find attractions for travellers
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    
    for any_interest in interests:
      if any_interest in attraction_tags: #if interest is in attraction tags append
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#Testing the find attractions function
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)

#Function to connect travellers with attractions
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "

  #If last attraction in list add a period, else add a comma plus a space

  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      #extra logic check to see if attraction we are on is the last one < if it is format the interest_string differently
      interests_string += "the " + traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string

#testing get_attractions_for_traveler()
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)






