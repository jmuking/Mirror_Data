import sys
from PyQt4 import QtGui, QtCore
from Mirror_Data import *

# Must show windows using controller
class Controller( QtGui.QMainWindow ):
        def __init__( self, *args, **kwargs ):
                super( Controller, self ).__init__()
                self.container = QtGui.QMainWindow( self )
                
                # Dictionary to hold all the windows
                self.windows = {}

        # Initializes each page (prevent recursion with StartPage)
        def initializeWindows( self ):
                i0 = StartPage( self.container, self )
                self.windows[ "StartPage" ] = i0
                i1 = WeatherPage( self.container, self )
                self.windows[ "WeatherPage" ] = i1
                i2 = NewsPage( self.container, self )
                self.windows[ "NewsPage" ] = i2

        # Shows the frame using the dictionary keyword initialized above
        def show_frame(self, cont):
                #if cont not in self.windows:
                #        self.windows[cont] = cont(self.container, self)
                frame = self.windows[cont]              
                # frame.showFullScreen()
                frame.show()
                
# Page you will see when program is first ran
class StartPage( QtGui.QDialog ):
        def __init__( self, parent, controller ):
                super( StartPage, self ).__init__()
                QtGui.QMainWindow.__init__( self, parent )

                self.controllerObject = Controller()

                # Set background color
                palette = QtGui.QPalette()
                palette.setColor( QtGui.QPalette.Background, QtCore.Qt.black )
                self.setPalette( palette )

                # Set text label color
                palette1 = QtGui.QPalette()
                palette1.setColor( QtGui.QPalette.Foreground, QtCore.Qt.white )

                # Pushbutton objects initializations
                lbl1 = QtGui.QLabel( "Weather" )
                lbl1.setPalette( palette1 )
                lbl2 = QtGui.QLabel( "News" )
                lbl2.setPalette( palette1 )
                # btn3 = QtGui.QPushButton( "Three" )
                # btn4 = QtGui.QPushButton( "Four" )

                # Window layout initialization
                vbox = QtGui.QVBoxLayout()
                hbox1 = QtGui.QHBoxLayout()
                hbox2 = QtGui.QHBoxLayout()

                # Window layout implementation
                # hbox1.addWidget( btn1 )
                hbox1.addStretch()
                # hbox1.addWidget( btn2 )
                hbox2.addWidget( lbl1 )
                hbox2.addStretch()
                hbox2.addWidget( lbl2 )
                vbox.addLayout( hbox1 )
                vbox.addStretch()
                vbox.addLayout( hbox2 )
                self.setLayout( vbox )

# Shows weather
class WeatherPage( QtGui.QDialog ):
        def __init__( self, parent, controller ):
                super( WeatherPage, self ).__init__()
                QtGui.QMainWindow.__init__( self, parent )

                # External interface objects
                self.controllerObject = Controller()
                self.dataObject = Mirror_Data( 1 )
                self.dataObject.refreshWeather()

                # Set background color
                palette = QtGui.QPalette()
                palette.setColor( QtGui.QPalette.Background, QtCore.Qt.black )
                self.setPalette( palette )

                # Label Palettes
                palette1 = QtGui.QPalette()
                palette1.setColor( QtGui.QPalette.Foreground, QtCore.Qt.white )

                # Weather objects initializations
                lbl1 = QtGui.QLabel()                                                                   # lbl: Label
                pm = QtGui.QPixmap( 'weatherSymbol.png' )                                               # pm: Pixel Map
                spm = pm.scaled( 64, 64, QtCore.Qt.KeepAspectRatio )                    # spm: Scaled Pixel Map
                lbl1.setPixmap( spm )
                lbl2 = QtGui.QLabel()
                temp = self.dataObject.getTemp()
                lbl2.setText( str( int( temp[ 0 ] ) ) )                                         # Pull Request: Weather
                palette2 = QtGui.QPalette()
                palette2.setColor( QtGui.QPalette.Foreground, QtCore.Qt.white )
                lbl2.setPalette( palette2 )

                # Back Button
                backLbl = QtGui.QLabel( "Back" )
                backLbl.setPalette( palette1 )

                # Window layout initialization
                vbox = QtGui.QVBoxLayout()
                vbox_in = QtGui.QVBoxLayout()
                hbox = QtGui.QHBoxLayout()

                # Window layout implementation
                vbox.addStretch()
                vbox.addWidget( lbl1 )
                vbox.addWidget( lbl2 )
                vbox.addStretch()
                hbox.addStretch()
                hbox.addLayout( vbox )
                hbox.addStretch()
                vbox_in.addStretch()
                vbox_in.addWidget( backLbl )
                hbox.addLayout( vbox_in )
                self.setLayout( hbox )

class NewsPage( QtGui.QDialog ):
        def __init__( self, parent, controller ):
                super( NewsPage, self ).__init__()
                QtGui.QMainWindow.__init__( self, parent )

                self.controllerObject = Controller()
                self.dataObject = Mirror_Data( 1 )
                self.dataObject.refreshNews()
                # self.updateNews()

                # Set background color
                palette = QtGui.QPalette()
                palette.setColor( QtGui.QPalette.Background, QtCore.Qt.black )
                self.setPalette( palette )

                # Set text label color
                palette1 = QtGui.QPalette()
                palette1.setColor( QtGui.QPalette.Foreground, QtCore.Qt.white )

                # Buttons
                backLbl = QtGui.QLabel( "Back" )
                backLbl.setPalette( palette1 )
                nextStoryLbl = QtGui.QLabel( "Next Story" )
                nextStoryLbl.setPalette( palette1 )

                # Labels
                self.titleLbl = QtGui.QLabel()
                palette2 = QtGui.QPalette()
                palette2.setColor( QtGui.QPalette.Foreground, QtCore.Qt.white )
                self.titleLbl.setPalette( palette2 )
                self.descrLbl = QtGui.QLabel()
                palette3 = QtGui.QPalette()
                palette3.setColor( QtGui.QPalette.Foreground, QtCore.Qt.white )
                self.descrLbl.setPalette( palette3 )

                # Window layout initialization
                hbox0 = QtGui.QHBoxLayout()
                vbox0 = QtGui.QVBoxLayout()
                vbox1 = QtGui.QVBoxLayout()
                vbox2 = QtGui.QVBoxLayout()

                # Window layout implementation
                vbox0.addStretch()
                vbox0.addWidget( nextStoryLbl )
                vbox1.addStretch()
                vbox1.addWidget( self.titleLbl )
                vbox1.addWidget( self.descrLbl )
                vbox1.addStretch()
                vbox2.addStretch()
                vbox2.addWidget( backLbl )
                hbox0.addLayout( vbox0 )
                hbox0.addStretch()
                hbox0.addLayout( vbox1 )
                hbox0.addStretch()
                hbox0.addLayout( vbox2 )
                self.setLayout( hbox0 )

                def updateNews( self ):
                        data = self.dataObject.nextArticle()
                        self.titleLbl.setText( data[ 0 ] )
                        self.descrLbl.setText( data[ 1 ] )


app = QtGui.QApplication( sys.argv )
# app.exec_() # Makes running program freeze ( qt infinite loop? )
