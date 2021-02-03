from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import  Window
from kivy.network.urlrequest import UrlRequest
from functools import partial
Window.size= (350, 900)

# Builder String
class Home(Screen):
    pass
class Stat(Screen):
    pass
sm = ScreenManager()
## LIST SCREEN ##
sm.add_widget(Home(name='home'))
sm.add_widget(Stat(name='stat'))
#########################################
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.help_str = Builder.load_file('main.kv')
        screen.add_widget(self.help_str)
        return screen

    def proses_cari(self):
        try:
            self.database ={
                'warga': {'rezza':{'Umur': '18', 'TanggalLahir':'25/04/02', 'alamat': 'Jl.Terompetxxxxxxxx'}}
            }
            user = self.help_str.get_screen('search').ids.data_warga.text
            namaa = self.database['warga'][user]['Umur']
            lahir = self.database['warga'][user]['TanggalLahir']
            alamat = self.database['warga'][user]['alamat']
            user = self.help_str.get_screen('search').ids.data_warga.text
            self.help_str.get_screen('search').ids.nama.text = str(f'Nama : {user}\nTgl-Lahir: {lahir}\nAlamat: {alamat}')
            self.help_str.get_screen('search').ids.data_card.opacity = str(1)
        except KeyError:
            self.help_str.get_screen('search').ids.nama.text = str('Nama Tidak Terdaftar')
            self.help_str.get_screen('search').ids.data_card.opacity = str(1)
    def statcor(self):
        url = 'https://api.kawalcorona.com/indonesia/'
        self.request = UrlRequest(url, on_success=self.sucescor, verify=True)
        user = self.help_str.get_screen('stat').ids.positif.text
    def sucescor(self, *args):
        for data in self.request.result:
            print(data)
            self.help_str.get_screen('stat').ids.positif.text = data['positif']
            self.help_str.get_screen('stat').ids.sembuh.text = data['sembuh']
            self.help_str.get_screen('stat').ids.meninggal.text = data['meninggal']
            


DemoApp().run()