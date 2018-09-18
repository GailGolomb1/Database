import sqlite3
conn = sqlite3.connect('QCDB.sqlite')
c = conn.cursor()

file = open('fastqc_data.txt', 'r')
i = 0
for line in file.readlines():
    perBase = '#Base	Mean	Median	Lower Quartile   Upper Quartile    10th Percentile    90th Percentile'
    perBase.split("\t")
    print line
    i = i + 1
    if i==20:
        break

    if '>>Per base sequence quality' in line:
        print ("Module 1")

        c.execute("""INSERT INTO '>>Per base sequence quality   pass'('#Base',    'Mean',    'Median',    'Lower Quartile',   'Upper Quartile',   '10th Percentile',  '90th Percentile') Values(
        '#Base',    'Mean',    'Median',   'Lower Quartile',    'Upper Quartile',   '10th Percentile',  '90th Percentile');""")

        print c.fetchall()
    elif line != '>>Per base sequence quality' in line:
        file.close()
    #else:
    #    print ("Error")
file.close()
####################################
#file = open('fastqc_data.txt', 'r')
i=0
for line in file.readlines():
    perBase = '#Tile	Base	Mean'
    perBase.split("\t")
    print line
    i = i + 1
    if i==20:
        break

    if '>>Per tile sequence quality' in line:
        print ("Module 2")

        c.execute("""INSERT INTO '>>Per base sequence quality    pass'('#Tile',    'Base',	'Mean') Values ('#Tile',  'Base',   'Mean');""")
        print c.fetchall()
    elif line != '>>Per tile sequence quality' in line:
        file.close()
    #else:
    #    print("Error")


#######################
#file = open('fastqc_data.txt', 'r')
for line in file.readlines():
    perBase = 'Quality  Count'
    perBase.split("\t")
    print line
    i = i + 1
    if i==20:
        break

    if line == '>>Per sequence quality scores' in lines:
        print("Module 3")
        c.execute("""INSERT INTO 'Per base sequence quality    pass' ('Quality', 'Count') Values('Quality', 'Count');""")
        print c.fetchall()
    elif line != '>>Per sequence quality scores' in lines:
        file.close()



    #else:
    #    print ("Error")

for line in file.readlines():
    perBase = '#Base	G	A	T	C'
    perBase.split("\t")
    print line
    i = i + 1
    if i==20:
        break

    if line == '>>Per base sequence content' in line:
        c.execute("""INSERT INTO Per base sequence quality ("#Base",	"G",	"A",	"T",	"C") Values (
        "#Base",	"G",	"A",	"T",	"C");""")
        print ("Module 4")
        print c.fetchall()
    elif line != '>>Per base sequence content' in line:
        file.close()


perBase = '#GC Content Count'
perBase.split("\t")

if line == '>>Per sequence GC content':
    c.execute("""INSERT INTO Per base sequence quality ("#GC Content", "Count") Values ("GC Content", "Count");""")
    print c.fetchall()
else:
    print("Error")


perBase = '#Base	N-Count'
perBase.split("\t")

if line == '>>Per base N content':
    c.execute("""INSERT INTO Per base sequence quality ("#Base",	"N-Count") Values("#Base",	"N-Count");""")
    print c.fetchall()
else:
    print("Error")


perBase = '#Duplication Level	Percentage of deduplicated	Percentage of total'
perBase.split("\t")



if line == '>>Sequence Duplication Levels':
    c.execute("""INSERT INTO Per base sequence quality("#Duplication Level",    "Percentage of deduplicated",   "Percentage of total Values") Values(
    "#Duplication Level",	"Percentage of deduplicated",	"Percentage of total");""")
    print c.fetchall()
else:
    print("Error")


                                #3' how to get '
perBase = '#Position	Illumina Universal Adapter	"Illumina Small RNA 3 Adapter"	"Illumina Small RNA 5 Adapter"	Nextera Transposase Sequence	SOLID Small RNA Adapter'
perBase.split("\t")

if line == '>>Adapter Content':
    c.execute ("""INSERT INTO Per base sequence quality ("#Position",	"Illumina Universal",  "Adapter	Illumina Small RNA 3' Adapter",	"Illumina Small RNA 5' Adapter",	"Nextera Transposase Sequence", "SOLID Small RNA Adapter") Values(
    "#Position",	"Illumina Universal Adapter",	"Illumina Small RNA 3' Adapter",	"Illumina Small RNA 5' Adapter",	"Nextera Transposase Sequence",  "SOLID Small RNA Adapter");""")
    print c.fetchall()
else:
    print("Error")


perBase = '#Sequence	Count	PValue	Obs/Exp Max   Max Obs/Exp Position'
perBase.split("\t")

if line == '>>Kmer Content':
    c.execute("""INSERT INTO Per base sequence quality ("#Sequence",	"Count",	"PValue",	"Obs/Exp Max",	"Max Obs/Exp Position") Values(
    "#Sequence",	"Count",	"PValue",	"Obs/Exp Max",	"Max Obs/Exp Position");""")
    print c.fetchall()
else:
    print("Error")
