#!/bin/sh
echo '"name","count"' > hh_uniq_positions.csv
J=`grep "Junior" ../ex03/hh_positions.csv | wc -l`
M=`grep "Middle" ../ex03/hh_positions.csv | wc -l`
S=`grep "Senior" ../ex03/hh_positions.csv | wc -l`
echo "\"Junior\",$J" | sed 's/ //g' >> hh_uniq_positions.csv
echo "\"Middle\",$M" | sed 's/ //g' >> hh_uniq_positions.csv
echo "\"Senior\",$S" | sed 's/ //g' >> hh_uniq_positions.csv
