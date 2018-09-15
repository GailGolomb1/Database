import sqlite3
conn = sqlite3.connect ('SRAmetadb.sqlite')
c = conn.cursor()

        #experiment_ID:
        #How many experiments are there with single runs? 3471647
c.execute('SELECT experiment_ID, COUNT(*) AS RecordCount FROM sra GROUP BY experiment_ID HAVING COUNT(*)==1;')
print len(c.fetchall())
    #How many experiments are there with multiple runs? 164200
c.execute('SELECT experiment_ID, COUNT(*) AS RecordCount FROM sra GROUP BY experiment_ID HAVING COUNT(*)>1;')
print len(c.fetchall())


    #study_ID:
    #How many studies are there with single experiments? 36530
c.execute('SELECT study_ID, COUNT(*) AS RecordCount FROM sra GROUP BY study_ID HAVING COUNT(*)==1;')
print len(c.fetchall())
    # How many studies are there with multiple experiments? 76453
c.execute('SELECT study_ID, COUNT(*) AS RecordCount FROM sra GROUP BY study_ID HAVING COUNT(*)>1;')
print len(c.fetchall())


    #submission_ID:
    #How many studies are there with single submissions?  311564
c.execute('SELECT submission_ID, COUNT(*) AS RecordCount FROM sra GROUP BY submission_ID HAVING COUNT(*)==1;')
print len(c.fetchall())
    # How many submissions are there with multiple submissions? 89892
c.execute('SELECT submission_ID, COUNT(*) AS RecordCount FROM sra GROUP BY submission_ID HAVING COUNT(*)>1;')
print len(c.fetchall())


##output of program:
#3471647
#164200
#36530
#76453
#311564
#89892
