from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
from pyvirtualdisplay import Display

class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(Screenshot, self).__init__()

    def capture(self, url, output_file="webimg.jpg"):
        self.load(QUrl(url))

        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())

        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        
        frame.render(painter)
        painter.end()

        print 'saving', output_file
        image.save("img/" + output_file)

if __name__ == "__main__":
    display = Display()
    display.start()

    webview = QWebView()
    webview.app = QApplication(sys.argv)
    webview.load(QUrl('http://www.google.ca'))
    frame = webview.page().mainFrame()
    webview.page().setViewportSize(frame.contentsSize())

    image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
    painter = QPainter(image)

    frame.render(painter)
    painter.end()

    image.save("img/" + output_file)

    display.stop()
