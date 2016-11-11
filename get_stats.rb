#! /usr/bin/ruby

require 'githubstats'
require 'matrix'
require 'json'

config = JSON.parse(File.read('config.json'))
user = config['github_user']

stats = GithubStats.new(user).data
matrix = Matrix[*stats.pad(-1).each_slice(7).to_a.transpose].minor(0, 7, -7, 7)
grid = Array.new(7) { Array.new(7) }
matrix.each_with_index do |point, y, x|
  grid[x][y] = { 
    date: point.date.to_s,
    score: point.score,
    quartile: stats.quartile(point.score)
  }
end
puts grid.to_json
