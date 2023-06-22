## Steps to setup mkdocs
* [Docs](https://www.mkdocs.org/getting-started/)
* [Step Docs](https://realpython.com/python-project-documentation-with-mkdocs/#toc)

* `pip3 install mkdocs`

```
mkdocs new mkdocs_for_doc
INFO     -  Writing config file: mkdocs_for_doc/mkdocs.yml
INFO     -  Writing initial docs: mkdocs_for_doc/docs/index.md
```

```
mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
WARNING  -  Both index.md and README.md found. Skipping README.md from
            /Users/shubham.h5/github/personal/OOPS-Python/Generic_Concepts/mkdocs_for_doc/docs
INFO     -  Documentation built in 0.26 seconds
INFO     -  [12:16:27] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [12:16:27] Serving on http://127.0.0.1:8000/
```

* `pip3 install mkdocs-material`
* `pip3 install mkdocstrings-python mkdocstrings`

`mkdocstrings-python`: mkdocstrings-python is the Python handler for mkdocstrings that allows mkdocstrings to parse Python code.


### Adding Code Docs:
<hr>
::: sample_code.main
::: sample_code.college