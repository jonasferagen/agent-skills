# Report rendering

Research owns title/layout files, SQL transforms and Python extension scripts in definitions/. Render owns renderer.py. Today renderer.py branches on report ID and reads files from definitions/. It writes compiled templates beside those source files. A saved title edit reaches the next render; an unsupported chart type requires modifying renderer.py. Reports A and B already run this way.

We are considering a read-only volume holding a selected report collection, passed with a config file to the same renderer environment. No delivery or compatibility format is selected. SQL transforms and Python scripts currently run with the renderer process's privileges. Selected output and logs are retained separately from disposable rendered pages.
