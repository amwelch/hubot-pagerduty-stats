# Description
#   Periodically collect/report on room statistics
#
# Configuration:
#   LIST_OF_ENV_VARS_TO_SET
#
# Commands:
#   hubot hello - <what the respond trigger does>
#   orly - <what the hear trigger does>
#
# Notes:
#   <optional notes required for the script>
#
# Author:
#   Sandy <amwelch@umich.edu>

python_shell = require("python-shell")

module.exports = (robot) ->
  robot.hear /stats/, (msg) ->
    msg.reply "hello!"
    console.log(python_shell)
    options = 
      args: [
        '--token'  
        'HIPCHAT TOKEN HERE'
        '--room' 
        'ROOM NAME HERE'
      ]
      scriptPath: "#{__dirname}/python"
    python_shell.run('readroom.py', options, (err, results) ->
      if err 
        console.log(err)
        throw err
      console.log(results)
      res = JSON.parse(results)
    )
  robot.hear /orly/, (msg)->
    msg.send "yarly"
