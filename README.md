**QC-Database**
**Title:** QC Database Prototype\
**Contributors:** August Guang, Ashok Ragavendran, and Gail Golomb Mello\
**Description:**  The QCDatabase would form part of the QCKit suite. One component of the QCKit suite is quality control tools to run on Next Generation Sequencing (and perhaps Third Generation Sequencing) data. Another component is visualization of the results of the quality control tools. The final component is the QC Database, containing quality control results from public repositories such as NCBI, such that the results of the quality control tools can be compared and visualized against other similar sequencing runs. This allows the researcher to get a quantitative sense of the quality of their sequences, rather than relying on the researcher’s experiential knowledge about what constitutes high quality sequences or not for their particular organism or protocol. Users running the QCKit suite will also have the option to upload their quality control results into the database as another data point. The entire suite will be incorporated into bioflows, a bioinformatics workflow management tool, which will run quality control at all appropriate intervals, ideally each component of a workflow.

**SRA_DB.py SRA_DB.py**
Description: This python version 2.7 file takes in arguments of taxon_id (species), library_source (sequence type (genomic, etc.), instrument_model (sequencing machine used to perform analysis), and the number of results wanted to be returned. This query returns the run accession numbers(s) from the SRA database query using sqlite3.

**License:** Licensed under GNU GPLv3 (LICENSE)
#Database
