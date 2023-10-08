from abc import ABC

class Telegram:
    def __init__(self, token):
        self.token = token
    
    def send_message(self, text):
        print(f"Send {text} to Telegram")
	
class ConsoleOutputAbstract(ABC):
    def output(self, text: str, *args) -> str:
        ...


class TerminalOutput(ConsoleOutputAbstract):
    def output(self, text: str, *args) -> None:
        print(f"Send {text} to console")


class TelegramOutput(ConsoleOutputAbstract):
    def __init__(self, token) -> None:
        self.telegram_client = Telegram(token)
    
    def output(self, text: str, *args) -> None:
        self.telegram_client.send_message(text)
		
				
class Commands_Handler:
    def __init__(self, command_output: ConsoleOutputAbstract):
        self.__output_processor = command_output
        
    def send_message(self, message) -> None:
        self.__output_processor.output(message)


if __name__ == "__main__":

    terminal_out = TerminalOutput()
    telegram_out = TelegramOutput("token")

    terminal_handler = Commands_Handler(terminal_out)
    telegram_handler = Commands_Handler(telegram_out)
    
    terminal_handler.send_message("Hello guys")
    telegram_handler.send_message("Hello guys")