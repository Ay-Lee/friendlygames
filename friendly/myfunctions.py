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
	newdate = datetime.datetime.strptime(str(newdag)+"/"+mnd+"/"+yr, "%d/%m/%Y")
	newdatum = newdate.strftime("%d")+"/"+mnd+"/"+yr
	return newdatum

def get_data(FILENAME):
	with open(FILENAME) as f:
		data = f.read().splitlines()
	f.close()
	return data

def get_compdic(data,seiz_deel):
	compdic = defaultdict(dict)
	for item in data:
		d = item.split(';')
		competition = d[0]
		team1 = d[3]
		team2 = d[4]
		datum = d[1]
		if re.search(seiz_deel,datum):
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
	sd = datum.split('/')
	seiz_deel = sd[2]

	#global vars
	FILENAMEANT = "inputcsv/antresdownP-4.csv"
	FILENAMELIM = "inputcsv/limresdownP.csv"
	FILENAMEBRA = "inputcsv/braresdownP.csv"
	FILENAMEOVL = "inputcsv/ovlresdownP.csv"
	FILENAMEWVL = "inputcsv/wvlresdownP.csv"
	FILENAMENAT = "inputcsv/natresdownP.csv"

	#REGEX per Prov - per leeftijd
	### Antwerpen ###

	RU6ANT = '^.6'
	RU7ANT = '^.7'
	RU8ANT = '^[^P]8'
	RU9ANT = '^[^P]9'
	RU10ANT = '^.10'
	RU11ANT = '^[^G]11'
	RU12ANT = '^.12'
	RU13ANT = '^([^G]13|13)'
	RU14ANT = '^14'
	RU15ANT = '^([^G]15|15)'
	RU17ANT = '^([^G]17|17)'

	### Limburg ###

	RU6LIM = '^6-' 
	RU7LIM = '^7-' 
	RU8LIM = '^8-' 
	RU9LIM = '^9-'
	RU10LIM = '^10'
	RU11LIM = '^11'
	RU12LIM = '^([^U]12|12)'
	RU13LIM = '^([^U]13|13)'
	RU14LIM = '^14'
	RU15LIM = '^([^U]15|15)'
	RU17LIM = '^([^U]17|15)'

	### Brabant ###

	RU6BRA = '^N6' 
	RU7BRA = '^N7' 
	RU8BRA = '^N8' 
	RU9BRA = '^N9' 
	RU10BRA ='^N10' 
	RU11BRA ='^N11'
	RU12BRA ='^N12'
	RU13BRA ='^N13'
	RU14BRA ='^14'
	RU15BRA ='^N15'
	RU17BRA ='^N17'


	### Oost Vlaanderen ###

	RU6OVL = '^6([A-Z])' 
	RU7OVL = '^7([A-Z])' 
	RU8OVL = '^8([A-Z])' 
	RU9OVL = '^9([A-Z])'
	RU10OVL = '^10([A-Z])'
	RU11OVL = '^11([A-Z])'
	RU12OVL = '^12([A-Z])'
	RU13OVL = '^13([A-Z])'
	RU14OVL = '^14'
	RU15OVL = '^15([A-Z])'
	RU17OVL = '^17([A-Z])'

	### West Vlaanderen ###

	RU6WVL = '^2/([A-Z])U6' 
	RU7WVL = '^2/([A-Z])U7' 
	RU8WVL = '^2/([A-Z])U8' 
	RU9WVL = '^2/([A-Z])U9'
	RU10WVL = '^2/([A-Z])U10'
	RU11WVL = '^2/([A-Z])U11'
	RU12WVL = '^2/([A-Z])U12'
	RU13WVL = '^2/([A-Z])U13'
	RU14WVL = '^14'
	RU15WVL = '^2/([A-Z])U15'
	RU17WVL = '^2/([A-Z])U17'

	### Nationaal + Inter provenciaal

	RU6NAT = '^6' 
	RU7NAT = '^7' 
	RU8NAT = '^8' 
	RU9NAT = '^9'
	RU10NAT = '^([^A-Z]10|10)'
	RU11NAT = '^([^A-Z]11|11)'
	RU12NAT = '^([^A-Z]12|12)'
	RU13NAT = '^([^A-Z]13|13)'
	RU14NAT = '^([^A-Z]14|14)'
	RU15NAT = '^([^A-Z]15|15)'
	RU17NAT = '^([^A-Z]17|17)'


	if leeftijd == 'U6':
		researchant = RU6ANT
		researchlim = RU6LIM
		researchbra = RU6BRA
		researchovl = RU6OVL
		researchwvl = RU6WVL
		researchnat = RU6NAT
	elif leeftijd == 'U7':
		researchant = RU7ANT
		researchlim = RU7LIM
		researchbra = RU7BRA
		researchovl = RU7OVL
		researchwvl = RU7WVL
		researchnat = RU7NAT
	elif leeftijd == 'U8':
		researchant = RU8ANT
		researchlim = RU8LIM
		researchbra = RU8BRA
		researchovl = RU8OVL
		researchwvl = RU8WVL
		researchnat = RU8NAT
	elif leeftijd == 'U9':
		researchant = RU9ANT
		researchlim = RU9LIM
		researchbra = RU9BRA
		researchovl = RU9OVL
		researchwvl = RU9WVL
		researchnat = RU9NAT
	elif leeftijd == 'U10':
		researchant = RU10ANT
		researchlim = RU10LIM
		researchbra = RU10BRA
		researchovl = RU10OVL
		researchwvl = RU10WVL
		researchnat = RU10NAT
	elif leeftijd == 'U11':
		researchant = RU11ANT
		researchlim = RU11LIM
		researchbra = RU11BRA
		researchovl = RU11OVL
		researchwvl = RU11WVL
		researchnat = RU11NAT
	elif leeftijd == 'U12':
		researchant = RU12ANT
		researchlim = RU12LIM
		researchbra = RU12BRA
		researchovl = RU12OVL
		researchwvl = RU12WVL
		researchnat = RU12NAT
	elif leeftijd == 'U13':
		researchant = RU13ANT
		researchlim = RU13LIM
		researchbra = RU13BRA
		researchovl = RU13OVL
		researchwvl = RU13WVL
		researchnat = RU13NAT
	elif leeftijd == 'U14':
		researchant = RU14ANT
		researchlim = RU14LIM
		researchbra = RU14BRA
		researchovl = RU14OVL
		researchwvl = RU14WVL
		researchnat = RU14NAT
	elif leeftijd == 'U15':
		researchant = RU15ANT
		researchlim = RU15LIM
		researchbra = RU15BRA
		researchovl = RU15OVL
		researchwvl = RU15WVL
		researchnat = RU15NAT
	elif leeftijd == 'U17':
		researchant = RU17ANT
		researchlim = RU17LIM
		researchbra = RU17BRA
		researchovl = RU17OVL
		researchwvl = RU17WVL
		researchnat = RU17NAT
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
		compdicant = get_compdic(raw_data_ant,seiz_deel)
		returndic = loop_dic(compdicant, researchant, datum)
	elif provintie == "limburg":
		raw_data_lim = get_data(FILENAMELIM)
		compdiclim = get_compdic(raw_data_lim,seiz_deel)
		returndic = loop_dic(compdiclim, researchlim, datum)
	elif provintie == "brabant":
		raw_data_bra = get_data(FILENAMEBRA)
		compdicbra = get_compdic(raw_data_bra,seiz_deel)
		returndic = loop_dic(compdicbra, researchbra, datum)
	elif provintie == "ovlaanderen":
		raw_data_ovl = get_data(FILENAMEOVL)
		compdicovl = get_compdic(raw_data_ovl,seiz_deel)
		returndic = loop_dic(compdicovl, researchovl, datum)
	elif provintie == "wvlaanderen":
		raw_data_wvl = get_data(FILENAMEWVL)
		compdicwvl = get_compdic(raw_data_wvl,seiz_deel)
		returndic = loop_dic(compdicwvl, researchwvl, datum)
	elif provintie == "nationaal":
		raw_data_nat = get_data(FILENAMENAT)
		compdicnat = get_compdic(raw_data_nat,seiz_deel)
		returndic = loop_dic(compdicnat, researchnat, datum)


	return returndic
