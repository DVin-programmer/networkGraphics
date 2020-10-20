@echo OFF
"Graphviz2.34\bin\dot.exe" -Tsvg %1 -o %~n1.svg
"Graphviz2.34\bin\dot.exe" -T jpg %1 -o %~n1.jpg
REM start %~n1.jpg
