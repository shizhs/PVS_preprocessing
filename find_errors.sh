#!/bin/bash

rm errors
for i in $(ls arrayJob.pbs.o2561686.*); do if [ $(cat $i | grep sitk::ERROR: | wc -l) -ne 0 ]; then echo $(echo $i | cut -d '.' -f 4) $(cat $i | head -2 | tail -1 | cut -d ' ' -f 1); fi; done >> errors
