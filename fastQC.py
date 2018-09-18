import sqlite3
conn = sqlite3.connect('QC_DB.sqlite')
c = conn.cursor()

file = open('fastqc_data.txt', 'r')
for line in file.readlines():
    perBase = '#Base	Mean	Median	Lower Quartile   Upper Quartile    10th Percentile    90th Percentile'
    perBase.split("\t")

    if line == '>>module Per base sequence quality':
        c.execute("""INSERT INTO Per base sequence quality ("#Base",    "Mean",    "Median",    "Lower Quartile",   "Upper Quartile",   "10th Percentile",  "90th Percentile") Values (
        "#Base",    "Mean",    "Median",   "Lower Quartile",    "Upper Quartile",   "10th Percentile",  "90th Percentile");""")

        print c.fetchall(file.readlines())
    elif line != '>>module Per base sequence quality':
        file.close()
    else:
        print ("Error")
file.close()


perBase = '#Tile	Base	Mean'
perBase.split("\t")
if line == ">>Per tile sequence quality":
    c.execute("""INSERT INTO Per base sequence quality ("#Tile",    "Base",	"Mean") Values ("#Tile",  "Base",   "Mean");""")
    print c.fetchall()
else:
    print("Error")



perBase = 'Quality Count'
perBase.split("\t")

if line == '>>Per sequence quality scores':
    c.execute("""INSERT INTO Per base sequence quality ("Quality", "Count") Values ("Quality", "Count");""")
    print c.fetchall()
else:
    print ("Error")


perBase = '#Base	G	A	T	C'
perBase.split("\t")

if line == '>>Per base sequence content':
    c.execute("""INSERT INTO Per base sequence quality ("#Base",	"G",	"A",	"T",	"C") Values (
    "#Base",	"G",	"A",	"T",	"C");""")
    print c.fetchall()
else:
    print("Error")


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
