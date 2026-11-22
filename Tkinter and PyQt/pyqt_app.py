import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox)

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Конвертер температур (PyQt)")
        self.resize(350, 250)

        main_layout = QVBoxLayout()

        self.lbl_title = QLabel("Введите температуру:")
        main_layout.addWidget(self.lbl_title)

        self.entry = QLineEdit()
        main_layout.addWidget(self.entry)

        h_layout = QHBoxLayout()
        self.combo_from = QComboBox()
        self.combo_from.addItems(["Цельсий", "Фаренгейт", "Кельвин"])
        self.combo_to = QComboBox()
        self.combo_to.addItems(["Цельсий", "Фаренгейт", "Кельвин"])
        self.combo_to.setCurrentText("Фаренгейт")
        
        h_layout.addWidget(self.combo_from)
        h_layout.addWidget(self.combo_to)
        main_layout.addLayout(h_layout)

        self.btn_convert = QPushButton("Конвертировать")
        self.btn_convert.clicked.connect(self.convert_temperature)
        main_layout.addWidget(self.btn_convert)

        self.lbl_result = QLabel("Результат: ")
        self.lbl_result.setStyleSheet("font-weight: bold; font-size: 14px;")
        main_layout.addWidget(self.lbl_result)

        self.setLayout(main_layout)

    def convert_temperature(self):
        try:
            val = float(self.entry.text())
            from_unit = self.combo_from.currentText()
            to_unit = self.combo_to.currentText()

            if from_unit == to_unit:
                result = val
            elif from_unit == "Цельсий":
                if to_unit == "Фаренгейт":
                    result = val * 9 / 5 + 32
                else:
                    result = val + 273.15
            elif from_unit == "Фаренгейт":
                if to_unit == "Цельсий":
                    result = (val - 32) * 5 / 9
                else:
                    result = (val - 32) * 5 / 9 + 273.15
            else:
                if to_unit == "Цельсий":
                    result = val - 273.15
                else:
                    result = (val - 273.15) * 9 / 5 + 32

            self.lbl_result.setText(f"Результат: {result:.2f} {to_unit}")

        except ValueError:
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите корректное число.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    ex.show()
    sys.exit(app.exec())
