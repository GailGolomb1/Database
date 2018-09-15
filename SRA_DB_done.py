
import argparse
import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()


#this function is to query the SRA database to determine the run_accession # for a given
# input of taxon_id, library_source, instrument_model, and number_results
# output run accession #'s
def search_db(search_terms):
        # input...
    taxon_id = search_terms[0]  #integer # which references a taxon ex. homo sapiens has its own #
    library_source = search_terms[1] # ex. transcriptomic RNA, genomic DNA
    instrument_model = search_terms[2] # model of instrument used to perform analysis
    number_results = search_terms[3] # number of results wanted for search
         #sqlite3 query to find run accesions
    c.execute('SELECT run_accession FROM sra WHERE taxon_id == "{0}" AND library_source == "{1}" AND instrument_model == "{2}" LIMIT "{3}";'
    .format(taxon_id, library_source, instrument_model, number_results))
    return c.fetchall()


# arg function to define arguments and add "help" comment
# output is a return of search terms
def search_terms ():
    parser = argparse.ArgumentParser()

#search term arguments
    parser.add_argument('taxon_id', help= 'taxon id number will be an integer number referring to a species')
    parser.add_argument('library_source', help= 'library source is either genomic or transcriptomic')
    parser.add_argument('instrument_model', help= 'model name of instrument used')
    parser.add_argument('number_results', help= 'number of total results to be displayed for search')


    args = parser.parse_args()

    search_terms = [args.taxon_id, args.library_source, args.instrument_model, args.number_results]
    search_terms[0] # gives you args.taxon_id
    search_terms[1] # gives you args.library_source
    search_terms[2]# gives you args.instrument_model
    search_terms[3]# gives you args.number_results

    return search_terms


# main function to call results of search_terms, search_db
# output to print the run accession #'s that results from the SLQ query of the SRA database
def main ():
    results = search_terms()
    print(results)
    run_accession = search_db(results)
    print run_accession


# calling the main function
main()
