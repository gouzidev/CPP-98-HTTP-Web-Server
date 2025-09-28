#!/bin/bash
# 10 MB of 'y'
head -c 10485760 < /dev/zero | tr '\0' 'y'