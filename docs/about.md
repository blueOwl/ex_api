# About AnnoQ

## Overview
This website ([link](http://annoq.org:4206/)) provides an interactive user interface for user to query variants and their annotations. The page is composed of two panels. The left panel is for the query input and filtering. The top of the panel allows user to input the query. There are four types of supported queries (see below for more details). The bottom of the panel are all the supported annotations organized in tree structure. User can check the type of annotation(s) to retrieve. The right panel is to display the search results.

## Annotations Description

 The backend of the system is a large collection of pre-annotated variants from the Haplotype Reference Consortium [HRC](http://www.haplotype-reference-consortium.org/))  (~39 million) with sequence features (by [WGSA](https://sites.google.com/site/jpopgen/wgsa) and functions (PANTHER and Gene Ontology [link](pantherdb.org)). The data is built in an Elasticsearch framework and an API was built to allow users to quickly access the annotation data. More details about the data and its format please refer to [detail page](http://annoq.org/detail.html)/

## Query Methods

### GUI Tutorial 

The GUI for variants annotation query is avaible at [http://annoq.org:4206/](http://annoq.org:4206/) .

Select a query type and input the query term. There 5 types of supported queries as described below.


#### 1. Genome Coordinates Query 
Chromosome location. A user can specify the chromosome number and the range. All data is based on hg19.

#### 2. Query by Upload VCF file
Variants List. A user can upload a VCF file of up to 10,000 variants. To do so, click the Populate from a File. A sample VCF file can be found at [here](http://annoq.org/static/main/sample.vcf).

Note that only first 50 rows of result will be displayed by our website. For retrieving the full result please using the download function.

#### 3. Gene Product Query
Gene Product. A user can input a gene or protein ID (e.g., ZMYND11). All variants located in the gene region will be returned. Currently, the system can only query one gene at a time. Gene name will be mapped to HGNC gene id by PANTHER gene mapping API.


#### 4. rsID query
A user can input a single rs ID and retrieve annotations.

#### 5. General Keyword Searech
AnnoQ also supports full-text search by using a keyword. This keyword can be a gene name, a phenotype name or a GO term (e.g. Signaling by GPCR). 

#### Result Download
All query results can be downloaded by using the download button on the upper right of the panel. It may take some time to generate the file for downloading.

## API Description

See API documents on github.

[link](https://github.com/blueOwl/ex_api/blob/master/docs/docs.md)

## R package 

See AnnoQR on github.

[AnnoQR](https://github.com/blueOwl/AnnoQR)