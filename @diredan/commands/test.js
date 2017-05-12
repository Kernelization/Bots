module.exports = {
  /*
   * just a basic command, almost like a template
   * whenever the user calls a command, for example
   * "<prefix>test" then the run() function will be called
   * and whenever the user runs the help command, the usage()
   * and decription() are called, so use this as a template for
   * future comands
   */
  run : (args, Client, msg) => {
    // code ran here
  },
  usage : () => {
    return "<prefix>test <arguments>";
  },
  description : () => {
    return "Used as a test command.";
  }
}
