#!/usr/bin/env python

# Genarate rails fixtures for Hospital and City clasess from 3 csv files

with open("import/cities.csv") as city_file:
    cities_content = city_file.readlines()

with open("import/states.csv") as state_file:
    states_content = state_file.readlines()

with open("import/ubs.csv") as hospital_file:
    hospitals_content = hospital_file.readlines()

cities_fixture = open('fixtures/cities.yml', 'r+')
hospitals_fixture = open('fixtures/hospitals.yml', 'r+')

cities_content = [x.strip() for x in cities_content]
states_content = [x.strip() for x in states_content]
hospitals_content = [x.strip() for x in hospitals_content]

states = {}
cities = {}

# Parse states
for line in states_content:
    code, name = line.split(',');
    states[code] = name

# Parse and write cities fixture using states
i = 0
for line in cities_content:
    code, name, pretty_name = line.split(',');
    # Save id to use in the hospital fixture
    cities[code] = i

    cities_fixture.write("city"+code+":\n")
    cities_fixture.write("  id: " + str(i)+"\n")
    cities_fixture.write("  code: " + code+"\n")
    cities_fixture.write("  name: " + name+"\n")
    # First two chars from the city code represent the state code
    cities_fixture.write("  state: " + states[code[:2]] +"\n\n")
    i+=1

# Parse and write hospitals fixture
for line in hospitals_content:
    latitude, longitude, code, phone, name, address, a, city, b, c, d, e = line.split(',');

    hospitals_fixture.write("hospital"+name+code+":\n")
    hospitals_fixture.write("  latitude: " + latitude +"\n")
    hospitals_fixture.write("  longitude: " + longitude +"\n")
    hospitals_fixture.write("  name: " + name +"\n")
    hospitals_fixture.write("  city_id: " + str(cities[code]) +"\n")
    hospitals_fixture.write("  phone: " + phone +"\n\n")


cities_fixture.close()
hospitals_fixture.close()
