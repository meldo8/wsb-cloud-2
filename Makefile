.PHONY: prepare-env
prepare-env:
	pip3 install pipenv
	HOMEBREW_NO_AUTO_UPDATE=1 brew install node awscli
	npm install -g npm-check-updates
	ncu -u
	npm install -g serverless

.PHONY: install-plugins
install-plugins:
	serverless plugin install -n serverless-manifest-plugin
	serverless plugin install -n serverless-python-requirements

.PHONY: invoke
invoke:
	serverless invoke -f getPeople --log --stage ${name}

.PHONY: deploy-stage
deploy-stage:
	sls deploy --stage ${name}

.PHONY: remove-stage
remove-stage:
	sls remove --stage ${name}
