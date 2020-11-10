#!/usr/bin/env ruby
# [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(',')
