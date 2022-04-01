.PHONY: prepare-env
prepare-env:
	HOMEBREW_NO_AUTO_UPDATE=1 brew install node awscli
	npm install -g serverless

.PHONY: install-plugins
install-plugins:
	serverless plugin install -n serverless-manifest-plugin
	serverless plugin install -n serverless-python-requirements

.PHONY: invoke
invoke:
	serverless invoke -f getPeople --log

.PHONY: deploy-stage
deploy-stage:
	sls deploy --stage ${name}

.PHONY: remove-stage
remove-stage:
	sls remove --stage ${name}
