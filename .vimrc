:let file_path = "/home/anurag/spoj-tools/"
:let lang = "! python3 "
command -nargs=1 SB execute lang.file_path."spoj-submitter.py % " string(<q-args>)
command -nargs=1 VW execute lang.file_path."spoj-viewer.py" string(<q-args>)
