1. Create Virtual Environment

	(Why? Using virtual environments allows you to avoid installing Python packages globally which could 				break system tools or other projects. It allows to manage separate package installations for     				different projects.)



	python3 -m venv DIR		

	source DIR/bin/activate 



2. Install Requirements

	pip install -r requirements.txt 



3. Install en_core_web_sm

	python -m spacy download en_core_web_sm 



4. Install Library

	Go to: https://test.pypi.org/project/ascentcoretagging/

	pip install -i https://test.pypi.org/simple/ascentcoretagging 



5. Import and Use the Library

	from ascentcoretagging import document_tagging 

											

	document_tagging.train(DIR) 

	document_tagging.test(DIR)  
