import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()

Taxon_id = raw_input("Enter taxon_id: ")

Library_source = raw_input("Enter library_source: ")

Instrument_model = raw_input("Enter instrument_model: ")

N = raw_input("Enter number of results to return: ")

c.execute ('SELECT run_accession FROM sra WHERE {0} and {1} and {2} LIMIT {3};'.format(Taxon_id, Library_source, Instrument_model, N))
print c.fetchall()
