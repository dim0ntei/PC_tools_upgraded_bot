from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Выбор языка
# Language select
ru = InlineKeyboardButton(text="Русский", callback_data="select_language_ru")
en = InlineKeyboardButton(text="English", callback_data="select_language_en")
language_select_keyboard = InlineKeyboardMarkup().row(ru, en)

# Русская версия
# Часто используемые кнопки
btn_back_ru = InlineKeyboardButton(text="Назад", callback_data="back")
btn_back_en = InlineKeyboardButton(text="Back", callback_data="back")

# Клавиатура "меню"
main_menu_keyboard_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
btn_create_screenshot_ru = KeyboardButton(text="Сделать скриншот")
btn_mouse_control_ru = KeyboardButton(text="Управление мышкой")
btn_files_and_processes_ru = KeyboardButton(text="Файлы и процессы")
btn_additional_ru = KeyboardButton(text="Дополнительно")
btn_send_notification_ru = KeyboardButton(text="Отправка уведомления")
btn_information_ru = KeyboardButton(text="Информация")
main_menu_keyboard_ru.row(btn_create_screenshot_ru, btn_mouse_control_ru)
main_menu_keyboard_ru.row(btn_files_and_processes_ru, btn_send_notification_ru)
main_menu_keyboard_ru.row(btn_additional_ru)

# Клавиатура "файлы и процессы"
files_and_processes_keyboard = InlineKeyboardMarkup()
btn_start_process_ru = InlineKeyboardButton(text="Запустить процесс", callback_data="start_process")
btn_kill_process_ru = InlineKeyboardButton(text="", callback_data="kill_process")
btn_download_file_ru = InlineKeyboardButton(text="", callback_data="download_file")
btn_upload_file_ru = InlineKeyboardButton(text="", callback_data="upload_file")
btn_url_down_ru = InlineKeyboardButton(text="", callback_data="url_down")
files_and_processes_keyboard.row(btn_start_process_ru, btn_kill_process_ru)
files_and_processes_keyboard.row(btn_download_file_ru, btn_upload_file_ru)
files_and_processes_keyboard.row(btn_url_down_ru)
files_and_processes_keyboard.row(btn_back_ru)

# "Дополнительная" клавиатура
additional_keyboard_ru = InlineKeyboardMarkup()
btn_web_ru = InlineKeyboardButton(text="", callback_data="go_url")
btn_run_command_ru = InlineKeyboardButton(text="", callback_data="run_command")
btn_shut_down_ru = InlineKeyboardButton(text="", callback_data="shut_down")
btn_restart_ru = InlineKeyboardButton(text="", callback_data="restart")

# Клавиатура "управление мышью"


# English version
# "menu" Keyboard
main_menu_keyboard_en = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
btn_create_screenshot_en = KeyboardButton(text="Create screenshoot")
btn_mouse_control_en = KeyboardButton(text="Mouse control")
btn_files_and_processes_en = KeyboardButton(text="Files and processes")
btn_additional_en = KeyboardButton(text="Additional")
btn_send_notification_en = KeyboardButton(text="Send notification")
btn_information_en = KeyboardButton(text="Information")
main_menu_keyboard_en.row(btn_create_screenshot_en, btn_mouse_control_en)
main_menu_keyboard_en.row(btn_files_and_processes_en, btn_send_notification_en)
main_menu_keyboard_en.row(btn_additional_en)

# "files and processes" menu
files_and_processes_keyboard_en = InlineKeyboardMarkup()
btn_start_process_en = InlineKeyboardButton(text="start process", callback_data="start_process")
btn_kill_process_en = InlineKeyboardButton(text="kill process", callback_data="kill_process")
btn_download_file_en = InlineKeyboardButton(text="download file", callback_data="download_file")
btn_upload_file_en = InlineKeyboardButton(text="upload file", callback_data="upload_file")
btn_url_down_en = InlineKeyboardButton(text="url download", callback_data="url_down")
files_and_processes_keyboard_en.row(btn_start_process_en, btn_kill_process_en)
files_and_processes_keyboard_en.row(btn_download_file_en, btn_upload_file_en)
files_and_processes_keyboard_en.row(btn_url_down_en)
files_and_processes_keyboard_en.row(btn_back_en)

# "Additional" menu

# "Mouse control" menu
