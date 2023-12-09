from abc import ABC, abstractmethod


class InfoOutput(ABC):

    @abstractmethod
    def info_output(self, data) -> str:
        pass


class ContactInfoOutput(InfoOutput):
    def info_output(self, data) -> str:
        return "_" * 50 + "\n" + f"Name: {data['name']} \nPhones: {', '.join(data['phones'])} \nBirthday: {BirthdayInfoOutput().info_output(data)} \nEmail: {data['email']} \nStatus: {data['status']} \nNote: {data['note']}\n" + "_" * 50


class BirthdayInfoOutput(InfoOutput):
    def info_output(self, data) -> str:
        return data['birthday'].strftime("%d/%m/%Y") if data['birthday'] else ''


class NotesInfoOutput(InfoOutput):
    def info_output(self, data) -> str:
        return super().info_output(data)


class CommandInfoOutput(InfoOutput):
    def info_output(self, data) -> str:
        format_str = str('{:%s%d}' % ('^',20))
        for command in data:
            print(format_str.format(command))
