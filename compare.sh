#!/bin/bash

echo "C++:"
time ./nm1_cpp

echo "Java:"
time java -jar nm1_java.jar

echo "Python:"
time python nm1.py