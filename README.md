# Conway's Game of Life

Bu proje, John Conway'in ünlü "Hayat Oyunu"nun (Game of Life) Python ve `curses` kütüphanesi kullanılarak terminalde çalışan bir uygulamasıdır. Oyun, hücrelerin belirli kurallara göre canlanıp öldüğü bir hücresel otomat simülasyonudur.

---

## :clipboard: İçindekiler

1. [Özellikler](https://github.com/thealper2/game-of-life/tree/main?tab=readme-ov-file#%C3%B6zellikler)
2. [Kurulum](https://github.com/thealper2/game-of-life/tree/main?tab=readme-ov-file#kurulum)
3. [Kullanım](https://github.com/thealper2/game-of-life/tree/main?tab=readme-ov-file#kullan%C4%B1m)
4. [Katkıda Bulunma](https://github.com/thealper2/game-of-life/tree/main?tab=readme-ov-file#katk%C4%B1da-bulunma)
5. [Lisans](https://github.com/thealper2/game-of-life/tree/main?tab=readme-ov-file#lisans)

## :dart: Özellikler

- Terminal boyutunu otomatik olarak kontrol eder ve uygun olmayan boyutlarda hata verir.
- Farklı başlangıç desenleri (örneğin, glider, blinker, block, beehive) içerir.
- Rastgele canlı hücreler ekleyerek dinamik bir başlangıç sağlar.
- Her nesil sonunda hücrelerin durumunu günceller ve ekrana çizer.
- Kullanıcı dostu kontroller (çıkış için `q` tuşu).

## :hammer_and_wrench: Kurulum

Projeyi kullanmak için Python 3.7 veya üzeri bir sürüm gereklidir.

1. Projeyi klonlayın:
```bash
git clone https://github.com/thealper2/game-of-life.git
cd game-of-life
```

2. Gerekli bağımlılıkları yükleyin (bu proje için ek bir bağımlılık yoktur, `curses` Python standart kütüphanesinin bir parçasıdır).
3. Projeyi çalıştırın:

```bash
python3 run.py
```

## :joystick: Kullanım

- Programı çalıştırdığınızda, terminal boyutu kontrol edilir ve uygun değilse bir hata mesajı gösterilir.
- Oyun başladıktan sonra, her nesil otomatik olarak güncellenir ve ekrana çizilir.
- Çıkmak için `q` tuşuna basın.

## :handshake: Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. Bu depoyu forklayın.
2. Yeni bir branch oluşturun (`git checkout -b feature/AmazingFeature`).
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`).
4. Branch'inizi pushlayın (`git push origin feature/AmazingFeature`).
5. Bir Pull Request açın.

## :scroll: Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
