#!/usr/bin/python
#
#
import sys
import re
import datetime
from collections import defaultdict

def test():
	response = "niet hier"
	return response

def datetostring(newdag, mnd, yr):
		newdatum = str(newdag)+"/"+mnd+"/"+yr
		return newdatum

def get_data(FILENAME):
	with open(FILENAME) as f:
		data = f.read().splitlines()
	f.close()
	return data

def get_compdic(data):
	compdic = defaultdict(dict)
	for item in data:
		d = item.split(';')
		competition = d[0]
		team1 = d[3]
		team2 = d[4]
		datum = d[1]
		try:
			compdic[competition][team1].append(datum)
		except KeyError:
			compdic[competition][team1] = [datum]
		try:
			compdic[competition][team2].append(datum)
		except KeyError:
			compdic[competition][team2] = [datum]
	return compdic

def loop_dic(compdic, research, datum):
	teamdic = defaultdict(list)
	dag,mnd,yr = datum.split("/")
	wd = datetime.datetime.strptime(datum, "%d/%m/%Y").weekday()
	if wd == 5:
		newdag = int(dag)+1
		newdatum = datetostring(newdag, mnd, yr)
		for key in compdic:
			if re.search(research, key):
				for x in compdic[key]:
					if (datum not in compdic[key][x] and newdatum not in compdic[key][x]):
						try:
							teamdic[key].append(x)
						
						except KeyError:
							teamdic[key] = [x]
		return teamdic
	elif wd == 6:
		newdag = int(dag)-1
		newdatum = datetostring(newdag, mnd, yr)
		for key in compdic:
			if re.search(research, key):
				for x in compdic[key]:
					if (datum not in compdic[key][x] and newdatum not in compdic[key][x]):
						try:
							teamdic[key].append(x)
						
						except KeyError:
							teamdic[key] = [x]
		return teamdic
	else :
		for key in compdic:
			if re.search(research, key):
				for x in compdic[key]:
					if datum not in compdic[key][x]:
						try:
							teamdic[key].append(x)
						
						except KeyError:
							teamdic[key] = [x]
	return teamdic



def searchteam(leeftijd, provintie, datum):
	leeftijd = leeftijd
	provintie = provintie
	datum = datum

	#global vars
	FILENAMEANT = "inputcsv/antresdownP-4.csv"
	FILENAMELIM = "inputcsv/limresdownP.csv"
	FILENAMEBRA = "inputcsv/braresdownP.csv"
	FILENAMEOVL = "inputcsv/ovlresdownP.csv"

	#REGEX per Prov - per leeftijd
	### Antwerpen ###

	RU6ANT = '^26'
	RU7ANT = '^27'
	RU8ANT = '^28'
	RU9ANT = '^29'
	RU10ANT = '^210'
	RU11ANT = '^211'
	RU12ANT = '^212'
	RU13ANT = '^213'
	RU15ANT = '^215'
	RU17ANT = '^217'

	### Limburg ###

	RU6LIM = '^6-' 
	RU7LIM = '^7-' 
	RU8LIM = '^8-([A-Z]$)' 
	RU9LIM = '^9-([A-Z]$)'
	RU10LIM = '^10-([A-Z]$)'
	RU11LIM = '^11-([A-Z]$)'
	RU12LIM = '^12-([A-Z]$)'
	RU13LIM = '^13-([A-Z]$)'
	RU15LIM = '^15-([A-Z]$)'
	RU17LIM = '^17-([A-Z]$)'

	### Brabant ###

	RU6BRA = '^N6[A-Z]2$' 
	RU7BRA = '^N7([A-Z]+)2$' 
	RU8BRA = '^N8[A-Z]2$' 
	RU9BRA = '^N9[A-Z]2$' 
	RU10BRA ='^N10[A-Z]2$' 
	RU11BRA ='^N11[A-Z]2$'
	RU12BRA ='^N12[A-Z]2$'
	RU13BRA ='^N13[A-Z]2$'
	RU15BRA ='^N15[A-Z]2$'
	RU17BRA ='^N17[A-Z]2$'


	### Oost Vlaanderen ###

	RU6OVL = '^6([A-Z]$)' 
	RU7OVL = '^7([A-Z]$)' 
	RU8OVL = '^8([A-Z]$)' 
	RU9OVL = '^9([A-Z]$)'
	RU10OVL = '^10([A-Z]$)'
	RU11OVL = '^11([A-Z]$)'
	RU12OVL = '^12([A-Z]$)'
	RU13OVL = '^13([A-Z]$)'
	RU15OVL = '^15([A-Z]$)'
	RU17OVL = '^17([A-Z]$)'


	if leeftijd == 'U6':
		researchant = RU6ANT
		researchlim = RU6LIM
		researchbra = RU6BRA
		researchovl = RU6OVL
	elif leeftijd == 'U7':
		researchant = RU7ANT
		researchlim = RU7LIM
		researchbra = RU7BRA
		researchovl = RU7OVL
	elif leeftijd == 'U8':
		researchant = RU8ANT
		researchlim = RU8LIM
		researchbra = RU8BRA
		researchovl = RU8OVL
	elif leeftijd == 'U9':
		researchant = RU9ANT
		researchlim = RU9LIM
		researchbra = RU9BRA
		researchovl = RU9OVL
	elif leeftijd == 'U10':
		researchant = RU10ANT
		researchlim = RU10LIM
		researchbra = RU10BRA
		researchovl = RU10OVL
	elif leeftijd == 'U11':
		researchant = RU11ANT
		researchlim = RU11LIM
		researchbra = RU11BRA
		researchovl = RU11OVL
	elif leeftijd == 'U12':
		researchant = RU12ANT
		researchlim = RU12LIM
		researchbra = RU12BRA
		researchovl = RU12OVL
	elif leeftijd == 'U13':
		researchant = RU13ANT
		researchlim = RU13LIM
		researchbra = RU13BRA
		researchovl = RU13OVL
	elif leeftijd == 'U15':
		researchant = RU15ANT
		researchlim = RU15LIM
		researchbra = RU15BRA
		researchovl = RU15OVL
	elif leeftijd == 'U17':
		researchant = RU17ANT
		researchlim = RU17LIM
		researchbra = RU17BRA
		researchovl = RU17OVL
	else: 
		return

#	raw_data_ant = get_data(FILENAMEANT)
#	raw_data_lim = get_data(FILENAMELIM)
#	raw_data_bra = get_data(FILENAMEBRA)
#	raw_data_ovl = get_data(FILENAMEOVL)
#	compdicant = get_compdic(raw_data_ant)
#	compdiclim = get_compdic(raw_data_lim)
#	compdicbra = get_compdic(raw_data_bra)
#	compdicovl = get_compdic(raw_data_ovl)

	if provintie == "antwerpen":
		raw_data_ant = get_data(FILENAMEANT)
		compdicant = get_compdic(raw_data_ant)
		returndic = loop_dic(compdicant, researchant, datum)
	elif provintie == "limburg":
		raw_data_lim = get_data(FILENAMELIM)
		compdiclim = get_compdic(raw_data_lim)
		returndic = loop_dic(compdiclim, researchlim, datum)
	elif provintie == "brabant":
		raw_data_bra = get_data(FILENAMEBRA)
		compdicbra = get_compdic(raw_data_bra)
		returndic = loop_dic(compdicbra, researchbra, datum)
	elif provintie == "ovlaanderen":
		raw_data_ovl = get_data(FILENAMEOVL)
		compdicovl = get_compdic(raw_data_ovl)
		returndic = loop_dic(compdicovl, researchovl, datum)


	return returndic
