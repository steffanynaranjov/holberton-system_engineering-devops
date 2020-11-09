#!/usr/bin/env ruby
# Regular expression match with phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
