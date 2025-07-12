PANDOC_SRC = presentation.md

PANDOC_OUT = $(PANDOC_SRC:%.md=%.pdf)

default: pandoc

pandoc:
	@echo -n "Compiling $(PANDOC_SRC) to $(PANDOC_OUT)... "
	@pandoc $(PANDOC_SRC) -t beamer+smart -s -o $(PANDOC_OUT) \
	-V theme:guadec -V classoption:aspectratio=169 --slide-level 2 --highlight-style kate
	@echo "Done!"

continuous: pandoc
	@echo "The PDF will be updated automatically when you save the $(PANDOC_SRC) document. Press Ctrl+C to abort."
	@while inotifywait -q $(PANDOC_SRC); do sleep 0.1; make --no-print-directory pandoc; done

clean:
	rm -Rf $(PANDOC_OUT)

watch:
	while true; do \
    		inotifywait -qr -e modify -e create -e delete -e move presentation.md; \
		make; \
	done

.PHONY: all clean watch

