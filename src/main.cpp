#include <cstring>
#include <iostream>
#include "Container.hpp"
#include "SocketManager.hpp"
#include "parser.hpp"
#include "utils.hpp"

std::vector<ServerSocketInfo> convertServersToSocketInfo(
    const std::vector<Server> &servers);

int main(int argc, char **argv)
{
  // if no config file found ->> load default built-in config and print
  // "Warning: No config file provided. Using default configuration."
  const char *configFile = "config/default.conf";

  if (argc > 2)
  {
    std::cerr << "Usage: ./webserv [configuration file]" << std::endl;
    return 1;
  }

  if (argc == 2)
  {
    configFile = argv[1];
  }
  else
  {
    std::cout << "Warning: No config file provided. Using default configuration." << std::endl;
  }

  try
  {
    initValidation(argc, argv);
    std::string content = readFile(configFile);
    std::vector<Token> tokens = lexer(content);
    checks(tokens);
    Container container = parser(tokens);

    std::vector<ServerSocketInfo> socketInfos =
        convertServersToSocketInfo(container.getServers());

    SocketManager socketManager;
    socketManager.setServers(container.getServers());

    if (!socketManager.initSockets(socketInfos))
      throw std::runtime_error("Failed to initialize sockets.");

    // Check
    std::cout << "Server initialized. Waiting for clients..." << std::endl;
    socketManager.handleClients();
  }
  catch (const std::exception &e)
  {
    std::cerr << "Error: " << e.what() << std::endl;
    return 1;
  }

  return 0;
}
