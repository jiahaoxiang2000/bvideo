F2_DIR=./f2
VENV=.venv

f2-init:
	uv venv $(VENV)
	. $(VENV)/bin/activate && \
	uv pip install -e .

f2-download:
	$(VENV)/bin/f2 dy -c down/like.yaml

combine-videos:
	$(VENV)/bin/python combine_videos.py

bilibili-upload-deps:
	$(VENV)/bin/uv pip install bilibili-api-python 
