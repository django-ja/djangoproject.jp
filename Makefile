build:
	@miyadaiku-build miya
	@cp -r miya/outputs/* docs/
	@cp -r static/* ./docs/
