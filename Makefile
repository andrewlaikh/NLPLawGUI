.PHONY: run run-container gcloud-deploy

run:
	@streamlit run main.py --server.port=8080 --server.address=0.0.0.0

run-container:
	@docker build . -t nlplaw
	@docker run -p 8080:8080 nlplaw

gcloud-deploy:
	@gcloud app deploy app.yaml
