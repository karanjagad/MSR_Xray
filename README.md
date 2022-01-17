
MSR_Xray
=================

Note This is a reproduction project as part of the MSR course 2021/22 at UniKo, CS department, SoftLang Team
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Names of team/students Team: Xray
----------------------------------------------------------------------------------------------------------------------------

Members:
-------------------------------------------------------------------------

-   Karan Jagad 
-   Disha Hegde 
-   Allwin Noble

Baseline study:
---------------------------------------------------------------------------------------

For the given Theisis  perform Data collection to reproduce table 4.7  and get similar output

### Input data:

The java code Application.java (Line66) aims at mining GitHub repositories with following criteria for the selected 19 dependency pairs

-   A repository with 100 stars and 100 commits
-   A repository with more than two contributors
-   A repository with at least one source directory
-   Dependency  Limit 25
-   Files Limit 800

### Output data:

Collected repositories
    
- The CSV files containing the list of selected repositories for each of the 19 dependency pairs is generated under /output/repositories_selected folder
- Please find Temp folder which contains all the output jar files for the collected repo - https://liveunikoblenz-my.sharepoint.com/:u:/g/personal/karanjagad_live_uni-koblenz_de/EVYiwpXLGdZMjQCUmP5wM1cBWRtZMqQxLMb1EHLBDrSzQg?e=t3bupU 

Findings of replication
--------------------------------------------------------------------------------------------------------

### Process delta:

Collecting all the repositories based on above input data criteria and then Parsing the csv files under */output/repositories_selected folder* and finding the count of the selected repositories for each dependency pair 

### Output delta:

Selected repository results after changing parameters was similar for all dependency pairs except for one pair which is *org.apache.lucene_lucene-analyzers-common_org.apache.lucene_lucene-core* 
The orginal table had 27 selected repositories but the reproduced table has only 9 repositories.(Reason can be the repository does not exist or during the collection program timed out/403 Forbiden Error)
All the other 18 dependency pair showed similar selected repository count like the orginalt table

### Implementation of replication:

-   Hardware requirements:
    -   OS: Windows, Linux or MacOS
    -   Memory: 16 GB RAM recommended
    -   Processor : Ryzen 7 Core(TM) i7
-   Software requirements
-   -   Intellij
    -   Java 11 (Maven project)
    -   Python 3.9.6 (plotly==5.1.0, pyspark==3.1.2)
-   Validation
    -   One can compare the above output folder with the original work, the reproduciblity is clearly noticable there.
    -   One can directly run the python file under process/Repo_Selection_Count_for_DependencyPairs.py and check the desired output.
    -   *User needs to be in  /output/repositeries_selected   folder before running the python code
-   Data
    -  Data replication have successfully generate the csv files listed in the output delta section, as well as a temp folder (uploaded in onedrive)containing the files required for the generation of the csv files.
