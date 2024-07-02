from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView



class ListWidget(RecycleView): 
	pass


class RootWidget(BoxLayout):
	inputbutton = ObjectProperty(None)
	inputcontent = ObjectProperty(None)
	outputcontent = ObjectProperty(None)

class MyApp(App): 
	def build(self):
		return RootWidget()

 MyApp().run()
