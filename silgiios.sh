Userator+="\n ⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝💻- AVTOMATIK QURULUM �?"
MESAJ+="\n "
MESAJ+="\n✅Yeniliklər kanalımız: @silgiubplugin"
MESAJ+="\n✅Dəstək qrupumuz: @silgiub"
MESAJ+="\n "
KOMEK+="\n "
BOSLUQ="\n "
clear
echo -e $BOSLUQ
echo -e $BOSLUQ
apk update
clear
echo -e $BOSLUQ
apk upgrade
echo -e $BOSLUQ
echo -e $MESAJ
echo -e $BOSLUQ
echo "Python yüklənir..."
echo -e $BOSLUQ
apk add python3
python3 -m ensurepip --upgrade
pip3 install --upgrade pip
clear
echo -e $MESAJ
echo -e $BOSLUQ
echo "Git yüklənir..."
echo -e $BOSLUQ
apk add git
clear
echo -e $MESAJ
echo -e $BOSLUQ
echo "Telethon yüklənir..."
echo -e $BOSLUQ
pip3 install telethon
clear
echo -e $MESAJ
echo -e $BOSLUQ
echo "Faylları yükləyirəm..."
echo -e $BOSLUQ
rm -rf SilgiUbInstaller
git clone https://github.com/Silgimusicbot/SilgiUbInstaller
clear
echo -e $BOSLUQ
echo -e $MESAJ
echo -e $BOSLUQ
echo -e $BOSLUQ
cd SilgiUbInstaller
pip3 install -r requirements.txt
python3 -m silgi_installer
