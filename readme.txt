Python packge

	numpy
	pandas
	sklearn
	xgboost (requires cmake 3.1.3 or higher as of 6/25/2021)
	tqdm

Program Usage

	python3 Regression.py 	-i <input filename (please specify .csv file format)>
			        -o <feature output filename>

Datasets
	sample data files were provided to test the efficacy of the Regression program. Please unzip the Regression files using the following command:

Example command:
	(Simple run using default command; assume running on the ampicillin.csv dataset)
	$ python3 Regression.py -i ampicillin.csv -o ampicillin.csv

The CD-HIT files for mapping the gene clusters back to the genomes is available at https://figshare.com/articles/dataset/Salmonella_enterica_pan-genome/21913689

License
MIT License

Copyright (c) 2023 Ming-Ren Yang and Yu-Wei Wu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Contributing authors
Ming-Ren Yang , Shun-Feng Su, Yu-Wei Wu
Graduate Institute of Biomedical Informatics, Taipei Medical University, Taipei, Taiwan

Version
0.1
