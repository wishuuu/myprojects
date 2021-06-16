Opis projektu:

Kreator sieci neuronowych wykorzystujący interfejs graficzny wykorzystujący napisany przy użyciu biblioteki PyQt5 oraz bibliotekę numpy do obliczeń matematycznych. Żeby uruchomić aplikację uruchom konsolę systemową w folderze z projektem, a następnie plik main.py.

Przyciski + oraz - pozwalają na dodawanie oraz usuwanie warstw neuronów.

Przycisk create net generuje sieć o ustawionej przyciskami + oraz - ilości wartw neurownów, ilości neuronów w każdej warstwie wpisanej w odpowiadających im polach, oraz parametrze szybkości uczenia wpisanym w polu learning rate.

Przyciski train oraz test pozwalają na trening oraz walidację poprawności wyników zwracanych przez sieć w oparciu o plik znajdujący się w ścieżce przekazanej w polu path.

Dane przekazywane do sieci muszą być przekazane jako plik txt w następującym formacie:
-atrybuty X odzielone przecinkami;docelowa klasa y w zapisie one hot vector odzielona przecinkami
-każdy kolejny zestaw danych odzielony znakiem nowej linii
-na końcu pliku pusta linia oznaczająca koniec danych