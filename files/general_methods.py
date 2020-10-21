from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image

class StyleWidgets(object):
    # Стиль кнопки
    def properties_button(self, n, bg_color, border_color, color,
                          bg_color_h, border_color_h, color_h,
                          bg_color_p, border_color_p, color_p,
                          border_width, border_radius):
        # self.n = n
        # self.setupUi(self)
        n.bg_color = bg_color
        n.border_color = border_color
        n.color = color
        n.bg_color_h = bg_color_h
        n.border_color_h = border_color_h
        n.color_h = color_h
        n.bg_color_p = bg_color_p
        n.border_color_p = border_color_p
        n.color_p = color_p
        n.border_width = border_width
        n.border_radius = border_radius
        n.setStyleSheet('''
                QPushButton:!hover
                {
                  background-color: ''' + bg_color + ''';
                  border-style: solid;
                  border-color: ''' + border_color + ''';
                  border-width: ''' + border_width + '''; 
                  border-radius: ''' + border_radius + '''; 
                  color: ''' + color + ''';
                }
                QPushButton:hover
                {
                  background-color: ''' + bg_color_h + ''';
                  border-style: solid;
                  border-color: ''' + border_color_h + ''';
                  border-width: ''' + border_width + '''; 
                  border-radius: ''' + border_radius + '''; 
                  color: ''' + color_h + ''';
                }
                QPushButton:pressed
                {
                  background-color: ''' + bg_color_p + ''';
                  border-style: solid;
                  border-color: ''' + border_color_p + ''';
                  border-width: ''' + border_width + '''; 
                  border-radius:  ''' + border_radius + '''; 
                  color: ''' + color_p + ''';
                }''')

    # Стиль надписи
    def properties_label(self, n, bg_color, border_color, color,
                         bg_color_h, border_color_h, color_h,
                         bg_color_p, border_color_p, color_p,
                         border_width, border_radius):
        n.bg_color = bg_color
        n.border_color = border_color
        n.color = color
        n.bg_color_h = bg_color_h
        n.border_color_h = border_color_h
        n.color_h = color_h
        n.bg_color_p = bg_color_p
        n.border_color_p = border_color_p
        n.color_p = color_p
        n.border_width = border_width
        n.border_radius = border_radius
        n.setStyleSheet('''
                    QLabel
                    {
                      background-color: ''' + bg_color + ''';
                      border-style: solid;
                      border-color: ''' + border_color + ''';
                      border-width: ''' + border_width + '''; 
                      border-radius: ''' + border_radius + '''; 
                      color: ''' + color + ''';
                    }''')

    def image_settings(self, place, x, y, path):
        '''
        Метод размещает изображение, размещенное в path в координатах x, y
        с размерами width, height
        '''
        self.label_pixmap = QtWidgets.QLabel(place)
        pixmap = QtGui.QPixmap(path)
        image_size = Image.open(path)
        (width, height) = image_size.size
        self.label_pixmap.setGeometry(QtCore.QRect(x, y, width, height))
        self.label_pixmap.setPixmap(pixmap)