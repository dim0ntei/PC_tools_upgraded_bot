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
btn_send_notification_ru = KeyboardButton(text="Отправить уведомление")
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

# Клавиатура "дополнительно"
additional_keyboard_ru = InlineKeyboardMarkup()
btn_web_ru = InlineKeyboardButton(text="Открыть веб-страницу", callback_data="go_url")
btn_run_command_ru = InlineKeyboardButton(text="Выполнить команду в CMD", callback_data="run_command")
btn_shut_down_ru = InlineKeyboardButton(text="Выключить компьютер", callback_data="shut_down")
btn_restart_ru = InlineKeyboardButton(text="перезапустить компьютер", callback_data="restart")
btn_info_ru = InlineKeyboardButton(text="О компьютере", callback_data="info")
additional_keyboard_ru.row(btn_web_ru, btn_run_command_ru)
additional_keyboard_ru.row(btn_shut_down_ru, btn_restart_ru)
additional_keyboard_ru.row(btn_restart_ru, btn_info_ru)
additional_keyboard_ru.row(btn_back_ru)

# Клавиатура "управление мышью"
mouse_control_keyboard_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_up_ru = KeyboardButton(text="⬆")
btn_down_ru = KeyboardButton(text="⬇")
btn_left_ru = KeyboardButton(text="⬅")
btn_click_ru = KeyboardButton(text="🆗")
btn_right_ru = KeyboardButton(text="➡")
btn_curs_ru = KeyboardButton(text="Размах курсора")
mouse_control_keyboard_ru.row(btn_up_ru)
mouse_control_keyboard_ru.row(btn_left_ru, btn_click_ru, btn_right_ru)
mouse_control_keyboard_ru.row(btn_down_ru)
mouse_control_keyboard_ru.row(btn_curs_ru, btn_back_ru)

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
additional_keyboard_en = InlineKeyboardMarkup()
btn_web_en = InlineKeyboardButton(text="Go URL", callback_data="go_url")
btn_run_command_en = InlineKeyboardButton(text="Run CMD command", callback_data="run_command")
btn_shut_down_en = InlineKeyboardButton(text="Shutdown PC", callback_data="shut_down")
btn_restart_en = InlineKeyboardButton(text="Restart PC", callback_data="restart")
btn_info_en = InlineKeyboardButton(text="About PC", callback_data="info")
additional_keyboard_en.row(btn_web_en, btn_run_command_en)
additional_keyboard_en.row(btn_shut_down_en, btn_restart_en)
additional_keyboard_en.row(btn_restart_en, btn_info_en)
additional_keyboard_en.row(btn_back_en)

# "Mouse control" menu
mouse_control_keyboard_en = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_up_en = KeyboardButton(text="⬆")
btn_down_en = KeyboardButton(text="⬇")
btn_left_en = KeyboardButton(text="⬅")
btn_click_en = KeyboardButton(text="🆗")
btn_right_en = KeyboardButton(text="➡")
btn_curs_en = KeyboardButton(text="Размах курсора")
mouse_control_keyboard_en.row(btn_up_en)
mouse_control_keyboard_en.row(btn_left_en, btn_click_en, btn_right_en)
mouse_control_keyboard_en.row(btn_down_en)
mouse_control_keyboard_en.row(btn_curs_en, btn_back_en)
