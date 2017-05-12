function rand(low, high) {
    return Math.random() * (high + 1 - low) + low | 0;
}

module.exports = {
  /*
   * 0 -> scissors
   * 1 -> rock
   * 2 -> paper
   */
  run : (args, Client, msg) => {
    if (args[0]) {
      // get user choice && user choice
      let computer_choice = rand(0,2);
      let user_choice = args[0] == "rock" ? 1 : args[0] == "paper" ? 2 : 0;

      // if their choices are same its a draw :D
      if (computer_choice == user_choice) {
        msg.reply("Game Drawn!");
      }
      else if (computer_choice < user_choice || computer_choice == 0 && user_choice == 2) {
        msg.reply("Computer Won!");
      } else {
        msg.reply("You Won!");
      }
    }
  },
  usage : () => {
    return "rps rock/paper/scissors";
  },
  description : () => {
    return "Used for playing rock, paper, scissors against the bot.";
  }
}
