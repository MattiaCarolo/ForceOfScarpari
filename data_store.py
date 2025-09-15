from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass
    # from board import Board
    # from board_list import BoardList
    # from user import User
    # from item import Item


class DataStore:

    def add_board(self, model) -> None:
        raise NotImplementedError

    def get_board(self, id) -> "Board":
        raise NotImplementedError

    def get_boards(self) -> list["Board"]:
        raise NotImplementedError

    def update_board(self, model, update):
        raise NotImplementedError

    def remove_board(self, board) -> None:
        raise NotImplementedError

    def add_user(self, model) -> None:
        raise NotImplementedError

    def get_users(self) -> list["User"]:
        raise NotImplementedError

    def get_user(self, id) -> "User":
        raise NotImplementedError

    def remove_user(self, id) -> None:
        raise NotImplementedError

    def add_list(self, board, model) -> None:
        raise NotImplementedError

    def get_lists(self) -> list["BoardList"]:
        raise NotImplementedError

    def get_list(self, id) -> "BoardList":
        raise NotImplementedError

    def get_lists_by_board(self, board) -> list["BoardList"]:
        raise NotImplementedError

    def remove_list(self, board, id) -> None:
        raise NotImplementedError

    def add_item(self, board_list, model) -> None:
        raise NotImplementedError

    def get_items(self, board_list) -> list["Item"]:
        raise NotImplementedError

    def get_item(self, id) -> "Item":
        raise NotImplementedError

    def get_items_by_board(self, board) -> list["Item"]:
        raise NotImplementedError

    def remove_item(self, board_list, id) -> None:
        raise NotImplementedError


class SimpleDataStore(DataStore):
    """Simple implementation of DataStore that doesn't raise NotImplementedError"""
    
    def __init__(self):
        pass

    def add_board(self, model) -> None:
        pass

    def get_board(self, id) -> "Board":
        return None

    def get_boards(self) -> list["Board"]:
        return []

    def update_board(self, model, update):
        pass

    def remove_board(self, board) -> None:
        pass

    def add_user(self, model) -> None:
        pass

    def get_users(self) -> list["User"]:
        return []

    def get_user(self, id) -> "User":
        return None

    def remove_user(self, id) -> None:
        pass

    def add_list(self, board, model) -> None:
        pass

    def get_lists(self) -> list["BoardList"]:
        return []

    def get_list(self, id) -> "BoardList":
        return None

    def get_lists_by_board(self, board) -> list["BoardList"]:
        return []

    def remove_list(self, board, id) -> None:
        pass

    def add_item(self, board_list, model) -> None:
        pass

    def get_items(self, board_list) -> list["Item"]:
        return []

    def get_item(self, id) -> "Item":
        return None

    def get_items_by_board(self, board) -> list["Item"]:
        return []

    def remove_item(self, board_list, id) -> None:
        pass