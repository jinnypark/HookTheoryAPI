#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  14 2019
@author: Jinny Park
"""
# import csv file of the chord types, RN, and chord members as python dictionary (based on HookTheory database)
import csv
import ast
import os

cwd = os.getcwd()
chord_symbols_path = cwd + "/Data/json_dictionary_RN_to_Chord_symbols.csv"
pc_dict_path = cwd + "/Data/pc_dictionary.txt"
output_path = cwd + "/Data/json_dictionary_RN_Chord_symbols_pcs.csv"

#create a list of pitches to store spelled chord members
pitches = []
with open(chord_symbols_path, mode ='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
        #if it's the first row, it is header
            line_count += 1
        pitches.append(row['chord_members_spelled'])

# First, load RN -> pc dictionary from text file
with open(pc_dict_path, "r") as data:
    pc_dict = ast.literal_eval(data.read())

#This funciton returns pc integer values of pitch members, given dictionary (pitches -> pc integers) and a list of pitches.
def integefy (listOfPitches, dictionary):
    newList = []
    for chords in listOfPitches:
        # returns string "C, E, G"
        chord = []
        pitches = chords.split(', ') #returns single pitch

        for pitch in pitches:
            chord.append(dictionary[pitch])
            # converts pitch into pc
        newList.append(chord)
    return newList

#Test integefy function
#print(integefy(['C, E, G','G, B, D'], pc_dict))

#Create a new list of pitch classes by using integefy function
pcs = (integefy(pitches, pc_dict))
#add header
pcs.insert(0, "pitch_clases")

# Write a new csv file with additional information of pc integers as a new column.
with open(chord_symbols_path, 'r') as csvInput:
    with open(output_path, 'w') as csvOutput:
        writer = csv.writer(csvOutput, lineterminator = '\n')
        reader = csv.reader(csvInput)

        all = []
        row = next(reader)
        line_counter = 0
        for thing in pcs:
            line_counter += 1
            #print("This is current row: ", row)
            #print("This is what I will append: ", thing)
            row.append(thing)
            all.append(row)

            if line_counter < len(pcs):
                row = next(reader)
            else:
                print("end of the list.")
        writer.writerows(all)
