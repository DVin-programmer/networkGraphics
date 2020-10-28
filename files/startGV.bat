@echo OFF
"files\Graphviz2.34\bin\dot.exe" -Tsvg %1 -o files\html\%~n1.svg
"files\Graphviz2.34\bin\dot.exe" -T jpg %1 -o files\html\%~n1.jpg
REM start %~n1.jpg
